"""Custom errors for the email composition API."""


class ComposerError(Exception):
    """Base error for composition failures."""

    status_code = 400

    def to_dict(self) -> dict:
        return {"error": self.__class__.__name__, "message": str(self)}


class ValidationError(ComposerError):
    """Raised when the request payload is invalid."""


class NotFoundError(ComposerError):
    """Raised when a requested family or component does not exist."""

    status_code = 404
