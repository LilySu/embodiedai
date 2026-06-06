from embodied_agents.tools.pii_regex import pii_regex_scan, scrub_text


def test_pii_regex_finds_common_identifiers() -> None:
    findings = pii_regex_scan("Email me at mary@example.com or call 415-555-1212 from 123 Main St.")
    assert {finding.kind for finding in findings} >= {"email", "phone", "street_address"}


def test_pre_match_scrubs_first_names_and_times() -> None:
    scrubbed, findings = scrub_text("I am Mary and I walk at 7am.", pre_match=True)
    assert "Mary" not in scrubbed
    assert "7am" not in scrubbed
    assert {finding.kind for finding in findings} >= {"first_name", "specific_time"}
