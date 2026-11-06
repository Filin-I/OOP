from datetime import datetime
from enum import IntEnum
import random
import re


class LogLevel(IntEnum):
    TRACE = 10
    INFO = 20
    WARN = 30
    ERROR = 40


class Logger:

    level = LogLevel.INFO
    format = "[%t] [%l] %n: %m"

    _random_messages = {
        LogLevel.TRACE: ("Following the next step", "Inspecting program state"),
        LogLevel.INFO: ("Operation completed", "Here is your result"),
        LogLevel.WARN: ("Please check the input", "Something needs attention"),
        LogLevel.ERROR: ("Operation failed", "Invalid input detected"),
    }

    def __init__(self, name: str):
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    @staticmethod
    def set_level(new_level: LogLevel) -> None:
        if not isinstance(new_level, LogLevel):
            raise TypeError("The level must be a LogLevel value")
        Logger.level = new_level

    @staticmethod
    def set_format(new_format: str) -> None:
        if not isinstance(new_format, str):
            raise TypeError("The format must be a string")
        Logger.format = new_format

    def log(self, msg_level: LogLevel, message: str) -> None:
        if not isinstance(msg_level, LogLevel):
            raise TypeError("The message level must be a LogLevel value")
        if msg_level < Logger.level:
            return

        values = {
            "%t": datetime.now().strftime("%H:%M:%S"),
            "%m": str(message),
            "%n": self.name,
            "%l": msg_level.name,
        }
        if "%r" in Logger.format:
            values["%r"] = random.choice(self._random_messages[msg_level])
        print(re.sub(r"%[tmnlr]", lambda match: values[match.group()], Logger.format))

    def trace(self, message: str) -> None:
        self.log(LogLevel.TRACE, message)

    def info(self, message: str) -> None:
        self.log(LogLevel.INFO, message)

    def warn(self, message: str) -> None:
        self.log(LogLevel.WARN, message)

    def error(self, message: str) -> None:
        self.log(LogLevel.ERROR, message)
