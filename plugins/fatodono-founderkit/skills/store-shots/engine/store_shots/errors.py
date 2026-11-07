"""The one error type a stage raises: its message is the console line."""


class StageError(Exception):
    """A failure the console reports on one line; the stage stops there."""
