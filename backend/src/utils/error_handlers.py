from fastapi import HTTPException, Request, status
from fastapi.responses import JSONResponse
from typing import Dict, Any
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class APIError(Exception):
    """Base API exception class"""
    def __init__(self, message: str, status_code: int = status.HTTP_400_BAD_REQUEST, details: Dict[str, Any] = None):
        self.message = message
        self.status_code = status_code
        self.details = details or {}
        super().__init__(self.message)

class ValidationError(APIError):
    """Exception raised for validation errors"""
    def __init__(self, message: str, details: Dict[str, Any] = None):
        super().__init__(message, status.HTTP_422_UNPROCESSABLE_ENTITY, details)

class AuthenticationError(APIError):
    """Exception raised for authentication errors"""
    def __init__(self, message: str = "Authentication failed", details: Dict[str, Any] = None):
        super().__init__(message, status.HTTP_401_UNAUTHORIZED, details)

class AuthorizationError(APIError):
    """Exception raised for authorization errors"""
    def __init__(self, message: str = "Access denied", details: Dict[str, Any] = None):
        super().__init__(message, status.HTTP_403_FORBIDDEN, details)

class NotFoundError(APIError):
    """Exception raised when a resource is not found"""
    def __init__(self, message: str = "Resource not found", details: Dict[str, Any] = None):
        super().__init__(message, status.HTTP_404_NOT_FOUND, details)

async def global_exception_handler(request: Request, exc: Exception):
    """Global exception handler for API errors"""
    if isinstance(exc, APIError):
        logger.error(f"API Error: {exc.message} - Status: {exc.status_code}")
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "detail": exc.message,
                "status_code": exc.status_code,
                "details": exc.details
            }
        )
    elif isinstance(exc, HTTPException):
        logger.error(f"HTTP Error: {exc.detail} - Status: {exc.status_code}")
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "detail": str(exc.detail),
                "status_code": exc.status_code
            }
        )
    else:
        logger.error(f"Unexpected error: {str(exc)}")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "detail": "Internal server error",
                "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR
            }
        )

def setup_error_handlers(app):
    """Setup error handlers for the FastAPI app"""
    app.add_exception_handler(Exception, global_exception_handler)
    app.add_exception_handler(HTTPException, global_exception_handler)
    app.add_exception_handler(APIError, global_exception_handler)