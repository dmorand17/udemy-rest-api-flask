import logging
import sys
from enum import Enum, auto
from typing import List
from logging.handlers import TimedRotatingFileHandler


class LogHandler(Enum):
    FILE = auto()
    CONSOLE = auto()


DEFAULT_FORMATTER = logging.Formatter(
    "%(asctime)s — %(module)s — %(name)s - %(levelname)s — %(message)s"
)
DEFAULT_LOG_FILE = "app.log"
DEFAULT_HANDLERS = [LogHandler.FILE, LogHandler.CONSOLE]


class AppLogger:
    def __init__(
        self,
        name,
        formatter=None,
        log_file=None,
        log_level=logging.DEBUG,
        handlers: List[LogHandler] = DEFAULT_HANDLERS,
    ):
        if formatter is None:
            self.formatter = DEFAULT_FORMATTER
        if log_file is None:
            self.log_file = DEFAULT_LOG_FILE
        self.logger = logging.getLogger(name)
        # with this pattern, it's rarely necessary to propagate the error up to parent
        self.logger.propagate = False
        self.handlers = handlers

        self.set_log_level(log_level)
        self._add_handlers()

    def _get_console_handler(self):
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(self.formatter)
        return console_handler

    def _get_file_handler(self):
        file_handler = TimedRotatingFileHandler(self.log_file, when="midnight")
        file_handler.setFormatter(self.formatter)
        return file_handler

    def _add_handlers(self):
        handlers = {
            LogHandler.FILE: self._get_file_handler,
            LogHandler.CONSOLE: self._get_console_handler,
        }

        for handler in self.handlers:
            self.logger.addHandler(handlers.get(handler)())

    def set_log_level(self, log_level):
        self.logger.setLevel(log_level)

    def get_logger(self):
        return self.logger
