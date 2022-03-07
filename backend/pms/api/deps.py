from contextlib import contextmanager
from fastapi import Depends
from pms.security.auth import get_current_user, TokenUser
from pms.db.session import SessionLocal

@contextmanager
def session_scope():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_db():
    with session_scope() as s:
        yield s

def current_user(user: TokenUser = Depends(get_current_user)) -> TokenUser:
    return user
