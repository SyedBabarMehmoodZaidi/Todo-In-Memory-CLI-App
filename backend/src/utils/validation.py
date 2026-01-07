import re
from typing import Optional

def sanitize_input(input_str: str) -> str:
    """Sanitize input string by removing potentially harmful characters."""
    if not input_str:
        return input_str
    # Remove potentially harmful characters/sequences
    sanitized = re.sub(r'<script[^>]*>.*?</script>', '', input_str, flags=re.IGNORECASE)
    sanitized = re.sub(r'javascript:', '', sanitized, flags=re.IGNORECASE)
    sanitized = re.sub(r'vbscript:', '', sanitized, flags=re.IGNORECASE)
    sanitized = re.sub(r'on\w+\s*=', '', sanitized, flags=re.IGNORECASE)
    return sanitized.strip()

def validate_email(email: str) -> bool:
    """Validate email format."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_password_strength(password: str) -> tuple[bool, str]:
    """Validate password strength and return (is_valid, error_message)."""
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"

    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter"

    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter"

    if not re.search(r"\d", password):
        return False, "Password must contain at least one number"

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain at least one special character"

    return True, ""

def validate_title(title: str) -> tuple[bool, str]:
    """Validate todo title and return (is_valid, error_message)."""
    if not title or len(title.strip()) == 0:
        return False, "Title is required"

    if len(title) > 100:
        return False, "Title must be less than 100 characters"

    # Check for potentially harmful content
    if '<' in title or '>' in title:
        return False, "Title contains invalid characters"

    return True, ""

def validate_description(description: Optional[str]) -> tuple[bool, str]:
    """Validate todo description and return (is_valid, error_message)."""
    if description is None:
        return True, ""

    if len(description) > 1000:
        return False, "Description must be less than 1000 characters"

    # Check for potentially harmful content
    if '<' in description or '>' in description:
        return False, "Description contains invalid characters"

    return True, ""

def validate_priority(priority: Optional[int]) -> tuple[bool, str]:
    """Validate priority value and return (is_valid, error_message)."""
    if priority is None:
        return True, ""

    if priority < 1 or priority > 3:
        return False, "Priority must be between 1 and 3"

    return True, ""