from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlmodel import Session
from typing import Annotated
from datetime import timedelta
from ..database.session import get_session
from ..models import User
from ..schemas import UserCreate, UserResponse, Token
from ..auth.utils import verify_password, get_password_hash
from ..auth.token import create_user_token
from ..services.user_service import validate_user_data, check_email_exists, get_user_by_email

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register_user(user: UserCreate, session: Session = Depends(get_session)):
    """Register a new user."""
    # Validate user data
    validation_errors = validate_user_data(user)
    if validation_errors:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=validation_errors
        )

    # Check if user already exists
    if check_email_exists(session, user.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    # Create new user
    hashed_password = get_password_hash(user.password)
    db_user = User(email=user.email, hashed_password=hashed_password)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user

@router.post("/login", response_model=Token)
def login_user(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
               session: Session = Depends(get_session)):
    """Login a user and return access token."""
    user = get_user_by_email(session, form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_user_token(str(user.id))
    token_data = {
        "access_token": access_token,
        "token_type": "bearer",
        "user": UserResponse(
            id=user.id,
            email=user.email,
            created_at=user.created_at
        )
    }

    return token_data

@router.get("/me", response_model=UserResponse)
def read_users_me(token: str = Depends(oauth2_scheme),
                  session: Session = Depends(get_session)):
    """Get current user info."""
    from ..auth.utils import verify_token
    payload = verify_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user_id = payload.get("sub")
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user = session.get(User, user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user