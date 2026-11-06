from logger import Logger


class ParenthesesValidator:
    def __init__(self):
        self._logger = Logger("Parentheses")

    def is_valid(self, input_string: str) -> bool:
        if not isinstance(input_string, str):
            raise TypeError("The input must be a string")

        balance = 0
        for position, character in enumerate(input_string):
            if character == "(":
                balance += 1
                self._logger.trace(
                    f"Opening parenthesis at index {position}; balance={balance}"
                )
            elif character == ")":
                if balance == 0:
                    self._logger.warn(f"Unmatched closing parenthesis at index {position}")
                    return self._finish(
                        input_string, False,
                        f"closing parenthesis at index {position} has no opening match",
                    )
                balance -= 1
                self._logger.info(f"Matching pair found at index {position}; balance={balance}")
            else:
                return self._finish(
                    input_string, False,
                    f"unexpected character {character!r} at index {position}",
                )

        if balance:
            return self._finish(input_string, False, f"{balance} opening parenthesis(es) remain unmatched")
        return self._finish(input_string, True)

    def _finish(self, input_string: str, valid: bool, reason: str = "") -> bool:
        if not valid:
            self._logger.error(f"Invalid input {input_string!r}: {reason}")
        self._logger.info(f"Validation result for {input_string!r}: {str(valid).lower()}")
        return valid
