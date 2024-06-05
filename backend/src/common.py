import logging

LOGGER = logging.getLogger("SudokuApp")


class AppError(Exception):
    """Application error, e.g. problem with implementation or config."""

    @staticmethod
    def config_error(message: str) -> "AppError":
        LOGGER.error("[CONFIG_ERROR] %s", message)
        return AppError(message, http_code=500)

    @staticmethod
    def input_error(message: str) -> "AppError":
        return AppError(message, http_code=400)

    def __init__(self, message, http_code):
        self.message = message
        self.http_code = http_code
        super().__init__(message)
