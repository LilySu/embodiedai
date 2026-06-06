import asyncio
import time

import jwt
from cryptography.hazmat.primitives.asymmetric import rsa
from jwt.algorithms import RSAAlgorithm

from embodied_agents.api import auth


def test_verify_clerk_jwt_uses_cached_jwks_and_issuer(monkeypatch) -> None:
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_jwk = RSAAlgorithm.to_jwk(private_key.public_key(), as_dict=True)
    public_jwk["kid"] = "kid_123"
    public_jwk["use"] = "sig"
    public_jwk["alg"] = "RS256"
    auth._JWKS_CACHE.update({"keys": [public_jwk], "expires_at": time.time() + 300})

    monkeypatch.setenv("CLERK_ISSUER", "https://clerk.example.test")
    monkeypatch.delenv("CLERK_AUDIENCE", raising=False)

    token = jwt.encode(
        {
            "sub": "user_123",
            "pseudo_id": "pseudo_123",
            "iss": "https://clerk.example.test",
            "iat": int(time.time()),
            "exp": int(time.time()) + 300,
        },
        private_key,
        algorithm="RS256",
        headers={"kid": "kid_123"},
    )

    claims = asyncio.run(auth.verify_clerk_jwt(token))

    assert claims["sub"] == "user_123"
    assert claims["pseudo_id"] == "pseudo_123"


def test_verify_clerk_jwt_rejects_forged_unsigned_token(monkeypatch) -> None:
    auth._JWKS_CACHE.update({"keys": [], "expires_at": time.time() + 300})
    monkeypatch.setenv("CLERK_ISSUER", "https://clerk.example.test")
    token = jwt.encode(
        {
            "sub": "attacker",
            "iss": "https://clerk.example.test",
            "iat": int(time.time()),
            "exp": int(time.time()) + 300,
        },
        key="",
        algorithm="none",
    )

    try:
        asyncio.run(auth.verify_clerk_jwt(token))
    except ValueError as exc:
        assert str(exc) == "missing_kid"
    else:
        raise AssertionError("forged unsigned token was accepted")
