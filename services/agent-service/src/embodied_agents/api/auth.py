from dataclasses import dataclass
import os

import jwt
from fastapi import Header, HTTPException


@dataclass(frozen=True)
class AuthContext:
    clerk_user_id: str
    pseudo_id: str | None


async def require_auth(authorization: str | None = Header(default=None)) -> AuthContext:
    if os.getenv("AGENT_SERVICE_AUTH_DISABLED") == "1":
        return AuthContext(clerk_user_id="dev", pseudo_id=None)

    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="missing_bearer_token")

    token = authorization.removeprefix("Bearer ").strip()
    try:
        claims = jwt.decode(token, options={"verify_signature": False, "verify_aud": False})
    except jwt.PyJWTError as exc:
        raise HTTPException(status_code=401, detail="invalid_token") from exc

    subject = claims.get("sub")
    if not subject:
        raise HTTPException(status_code=401, detail="missing_subject")

    return AuthContext(clerk_user_id=subject, pseudo_id=claims.get("pseudo_id"))
