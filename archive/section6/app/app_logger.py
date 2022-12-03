import logging
import sys
from enum import Enum, auto
from typing import List
from logging.handlers import TimedRotatingFileHandler


class LogHandler(Enum):
    FILE = auto()
    CONSOLE = auto()


DEFAULT_HANDLERS = [LogHandler.FILE, LogHandler.CONSOLE]


class AppLogger:
    DEFAULT_LOG_FILE = "logs/app.log"
    DEFAULT_FORMATTER = logging.Formatter(
        "%(asctime)s — %(name)20s - [%(threadName)s] - %(levelname)s — %(message)s "
    )

    def __init__(
        self,
        name,
        formatter=None,
        log_file=None,
        level=logging.DEBUG,
        handlers: List[LogHandler] = DEFAULT_HANDLERS,
    ):
        self.formatter = (
            AppLogger.DEFAULT_FORMATTER if formatter is None else formatter
        )
        self.log_file = (
            AppLogger.DEFAULT_LOG_FILE if log_file is None else log_file
        )
        self.logger = logging.getLogger(name)

        # with this pattern, it's rarely necessary to propagate the error up to parent
        self.logger.propagate = False

        self.set_level(level)
        self.handlers = handlers
        self._add_handlers()

    def _add_handlers(self):
        handlers = {
            LogHandler.FILE: AppLogger.file_handler,
            LogHandler.CONSOLE: AppLogger.console_handler,
        }

        handler_args = {"log_file": self.log_file, "formatter": self.formatter}

        for handler in self.handlers:
            self.logger.addHandler(handlers.get(handler)(**handler_args))

    def set_level(self, level):
        self.logger.setLevel(level)

    @classmethod
    def get_logger(cls, name, **kwargs):
        return cls(name, **kwargs).logger

    @staticmethod
    def file_handler(**kwargs):
        formatter = (
            kwargs["formatter"]
            if kwargs.get("formatter")
            else AppLogger.DEFAULT_FORMATTER
        )
        log_file = (
            kwargs["log_file"]
            if kwargs.get("log_file")
            else AppLogger.DEFAULT_LOG_FILE
        )

        file_handler = TimedRotatingFileHandler(log_file, when="midnight")
        file_handler.setFormatter(formatter)
        return file_handler

    @staticmethod
    def console_handler(**kwargs):
        formatter = (
            kwargs["formatter"]
            if kwargs.get("formatter")
            else AppLogger.DEFAULT_FORMATTER
        )
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        return console_handler
