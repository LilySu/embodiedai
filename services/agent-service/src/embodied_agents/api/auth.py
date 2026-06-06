from dataclasses import dataclass
import os
import time
from typing import Any

import httpx
import jwt
from fastapi import Header, HTTPException
from jwt import PyJWKClientError
from jwt.algorithms import RSAAlgorithm


@dataclass(frozen=True)
class AuthContext:
    clerk_user_id: str
    pseudo_id: str | None


_JWKS_CACHE: dict[str, Any] = {"expires_at": 0.0, "keys": []}


async def require_auth(authorization: str | None = Header(default=None)) -> AuthContext:
    if os.getenv("AGENT_SERVICE_AUTH_DISABLED") == "1":
        return AuthContext(clerk_user_id="dev", pseudo_id=None)

    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="missing_bearer_token")

    token = authorization.removeprefix("Bearer ").strip()
    try:
        claims = await verify_clerk_jwt(token)
    except (jwt.PyJWTError, PyJWKClientError, ValueError, httpx.HTTPError) as exc:
        raise HTTPException(status_code=401, detail="invalid_token") from exc

    subject = claims.get("sub")
    if not subject:
        raise HTTPException(status_code=401, detail="missing_subject")

    return AuthContext(clerk_user_id=subject, pseudo_id=claims.get("pseudo_id"))


async def verify_clerk_jwt(token: str) -> dict[str, Any]:
    issuer = os.getenv("CLERK_ISSUER")
    if not issuer:
        raise ValueError("missing_clerk_issuer")
    audience = os.getenv("CLERK_AUDIENCE")
    jwks_url = os.getenv("CLERK_JWKS_URL", issuer.rstrip("/") + "/.well-known/jwks.json")

    unverified_header = jwt.get_unverified_header(token)
    key_id = unverified_header.get("kid")
    if not key_id:
        raise ValueError("missing_kid")

    jwk = await _get_jwk(jwks_url, key_id)
    public_key = RSAAlgorithm.from_jwk(jwk)
    decode_kwargs: dict[str, Any] = {
        "algorithms": ["RS256"],
        "issuer": issuer,
        "options": {"require": ["exp", "iat", "sub"]},
    }
    if audience:
        decode_kwargs["audience"] = audience
    else:
        decode_kwargs["options"]["verify_aud"] = False

    return jwt.decode(token, public_key, **decode_kwargs)


async def _get_jwk(jwks_url: str, key_id: str) -> dict[str, Any]:
    keys = await _get_jwks_keys(jwks_url)
    for key in keys:
        if key.get("kid") == key_id:
            return key
    _JWKS_CACHE["expires_at"] = 0.0
    keys = await _get_jwks_keys(jwks_url)
    for key in keys:
        if key.get("kid") == key_id:
            return key
    raise ValueError("unknown_kid")


async def _get_jwks_keys(jwks_url: str) -> list[dict[str, Any]]:
    now = time.time()
    if _JWKS_CACHE["expires_at"] > now:
        return list(_JWKS_CACHE["keys"])

    async with httpx.AsyncClient(timeout=5.0) as client:
        response = await client.get(jwks_url)
        response.raise_for_status()
    body = response.json()
    keys = body.get("keys")
    if not isinstance(keys, list):
        raise ValueError("invalid_jwks")
    _JWKS_CACHE.update({"keys": keys, "expires_at": now + 300})
    return list(keys)
