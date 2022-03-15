from fastapi import Depends, HTTPException, status
from pms.security.auth import TokenUser, get_current_user

ROLE_ORDER = {"admin": 3, "reviewer": 2, "submitter": 1}

def require_role(min_role: str):
    def _dep(user: TokenUser = Depends(get_current_user)) -> TokenUser:
        user_level = max((ROLE_ORDER.get(r, 0) for r in user.roles), default=0)
        if user_level < ROLE_ORDER[min_role]:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
        return user
    return _dep
