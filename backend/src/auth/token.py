from datetime import datetime, timedelta
from typing import Optional
from .utils import create_access_token

def create_user_token(user_id: str) -> str:
    """Create a JWT token for a user."""
    data = {"sub": user_id, "type": "access"}
    expire = timedelta(minutes=30)
    return create_access_token(data, expires_delta=expire)

def create_refresh_token(user_id: str) -> str:
    """Create a refresh token for a user."""
    data = {"sub": user_id, "type": "refresh"}
    expire = timedelta(days=7)
    return create_access_token(data, expires_delta=expire)

def create_access_token_from_refresh(refresh_token: str) -> Optional[str]:
    """Create a new access token from a refresh token."""
    from .utils import verify_token

    payload = verify_token(refresh_token)
    if not payload:
        return None

    # Check if this is a refresh token
    token_type = payload.get("type")
    if token_type != "refresh":
        return None

    user_id = payload.get("sub")
    if not user_id:
        return None

    # Create new access token
    return create_user_token(user_id)