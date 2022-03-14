from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
import httpx, jwt
from pms.config import settings

bearer = HTTPBearer(auto_error=False)

class TokenUser(BaseModel):
    sub: str
    email: str | None = None
    roles: list[str] = []

async def get_current_user(creds: HTTPAuthorizationCredentials = Depends(bearer)) -> TokenUser:
    if not creds:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="No credentials")
    token = creds.credentials
    async with httpx.AsyncClient() as client:
        jwks = (await client.get(f"{settings.oidc_issuer_url}/protocol/openid-connect/certs")).json()
    try:
        header = jwt.get_unverified_header(token)
        key = next(k for k in jwks["keys"] if k["kid"] == header["kid"])
        public_key = jwt.algorithms.RSAAlgorithm.from_jwk(key)
        payload = jwt.decode(
            token,
            key=public_key,
            audience=settings.oidc_audience,
            algorithms=[header["alg"]],
            options={"verify_exp": True},
        )
    except Exception as e:  # noqa
        raise HTTPException(status_code=401, detail=f"Invalid token: {e}")
    roles = payload.get("realm_access", {}).get("roles", []) or payload.get("roles", [])
    return TokenUser(sub=payload["sub"], email=payload.get("email"), roles=roles)
