from dataclasses import dataclass
import re


@dataclass(frozen=True)
class PiiFinding:
    kind: str
    value: str


PII_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("email", re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE)),
    ("phone", re.compile(r"(?<!\d)(?:\+?1[\s.-]?)?(?:\(?\d{3}\)?[\s.-]?)\d{3}[\s.-]?\d{4}(?!\d)")),
    ("ssn", re.compile(r"\b\d{3}-\d{2}-\d{4}\b")),
    ("coordinate", re.compile(r"\b-?\d{1,2}\.\d{4,}\s*,\s*-?\d{1,3}\.\d{4,}\b")),
    ("street_address", re.compile(r"\b\d{1,6}\s+[A-Za-z0-9.'-]+(?:\s+[A-Za-z0-9.'-]+){0,4}\s+(?:Street|St|Avenue|Ave|Road|Rd|Drive|Dr|Lane|Ln|Boulevard|Blvd|Court|Ct|Way|Place|Pl)\b", re.IGNORECASE)),
    ("unit", re.compile(r"\b(?:apt|apartment|unit|suite|ste)\s*#?\s*[A-Z0-9-]+\b", re.IGNORECASE)),
    ("social_handle", re.compile(r"(?<!\w)@[A-Za-z0-9_]{3,30}\b")),
)

PROMPT_INJECTION_PATTERN = re.compile(
    r"\b(ignore (?:all )?(?:previous|above) instructions|system prompt|developer message|jailbreak|do not scrub|forward my number)\b",
    re.IGNORECASE,
)

FIRST_NAME_PATTERN = re.compile(
    r"\b(?:Alice|Barbara|Betty|Carol|Deborah|Diane|Donna|Elizabeth|Jane|Janet|Joan|Judith|Linda|Mary|Nancy|Patricia|Susan)\b"
)

FULL_NAME_PATTERN = re.compile(r"\b[A-Z][a-z]{2,}\s+[A-Z][a-z]{2,}\b")

TIME_SPECIFIC_PATTERN = re.compile(r"\b(?:[01]?\d|2[0-3])(?::[0-5]\d)?\s*(?:am|pm|AM|PM)?\b")


def pii_regex_scan(text: str, *, include_names: bool = False, include_time: bool = False) -> list[PiiFinding]:
    findings: list[PiiFinding] = []
    for kind, pattern in PII_PATTERNS:
        findings.extend(PiiFinding(kind=kind, value=match.group(0)) for match in pattern.finditer(text))

    findings.extend(PiiFinding(kind="full_name", value=match.group(0)) for match in FULL_NAME_PATTERN.finditer(text))

    if include_names:
        findings.extend(PiiFinding(kind="first_name", value=match.group(0)) for match in FIRST_NAME_PATTERN.finditer(text))

    if include_time:
        findings.extend(PiiFinding(kind="specific_time", value=match.group(0)) for match in TIME_SPECIFIC_PATTERN.finditer(text))

    return _dedupe(findings)


def scrub_text(text: str, *, pre_match: bool) -> tuple[str, list[PiiFinding]]:
    findings = pii_regex_scan(text, include_names=pre_match, include_time=pre_match)
    scrubbed = text
    for finding in sorted(findings, key=lambda item: len(item.value), reverse=True):
        scrubbed = scrubbed.replace(finding.value, f"[removed {finding.kind}]")
    return _normalize_spaces(scrubbed), findings


def contains_prompt_injection(text: str) -> bool:
    return bool(PROMPT_INJECTION_PATTERN.search(text))


def _dedupe(findings: list[PiiFinding]) -> list[PiiFinding]:
    seen: set[tuple[str, str]] = set()
    deduped: list[PiiFinding] = []
    for finding in findings:
        key = (finding.kind, finding.value)
        if key not in seen:
            seen.add(key)
            deduped.append(finding)
    return deduped


def _normalize_spaces(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()
