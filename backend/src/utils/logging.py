import logging
import sys
from datetime import datetime
from typing import Any, Dict

# Create custom logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create handlers
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.DEBUG)

# Create formatters and add to handlers
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
console_handler.setFormatter(formatter)

# Add handlers to logger
logger.addHandler(console_handler)

class AppLogger:
    """Application logger with structured logging capabilities."""

    @staticmethod
    def _log_structured(level: str, message: str, **kwargs) -> None:
        """Log a structured message with additional context."""
        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": level,
            "message": message,
            **kwargs
        }
        getattr(logger, level.lower())(str(log_entry))

    @classmethod
    def info(cls, message: str, **kwargs) -> None:
        """Log an info message."""
        cls._log_structured("INFO", message, **kwargs)

    @classmethod
    def error(cls, message: str, **kwargs) -> None:
        """Log an error message."""
        cls._log_structured("ERROR", message, **kwargs)

    @classmethod
    def warning(cls, message: str, **kwargs) -> None:
        """Log a warning message."""
        cls._log_structured("WARNING", message, **kwargs)

    @classmethod
    def debug(cls, message: str, **kwargs) -> None:
        """Log a debug message."""
        cls._log_structured("DEBUG", message, **kwargs)

    @classmethod
    def critical(cls, message: str, **kwargs) -> None:
        """Log a critical message."""
        cls._log_structured("CRITICAL", message, **kwargs)

# Initialize the logger
app_logger = AppLogger()

def get_logger() -> AppLogger:
    """Get the application logger instance."""
    return app_logger