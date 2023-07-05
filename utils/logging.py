"""
author: Maxim Van den Abeele
06/05/2023
"""
import logging


def enable_console_log(log_level=logging.INFO):
    """Enable console logging using our custom formatter
    """
    logging.basicConfig(level=log_level)
    handler = logging.getLogger().handlers[0]
    handler.setFormatter(CustomFormatter(use_colors=True))

class CustomFormatter(logging.Formatter):
    """Basic formatting class
    """
    def __init__(self, *args, use_colors=True, **kwargs):
        """Initialiser

        Args:
            use_colors (bool, optional): Use color mode or just basic formatting. Defaults to True.
        """
        super().__init__(*args, **kwargs)

        self.use_colors = use_colors

        grey = "\x1b[38;20m"
        yellow = "\x1b[33;20m"
        green = "\x1b[32;20m"
        red = "\x1b[31;20m"
        blue = "\x1b[34;20m"
        bold_red = "\x1b[31;1m"
        reset = "\x1b[0m"
        pre_fix = "%(asctime)s\n"
        format_style = "%(levelname)s:%(name)s - %(message)s"

        self._formats = {
            logging.DEBUG: grey + pre_fix + blue + format_style + reset,
            logging.INFO: grey + pre_fix + green + format_style + reset,
            logging.WARNING: grey + pre_fix + yellow + format_style + reset,
            logging.ERROR: grey + pre_fix + red + format_style + reset,
            logging.CRITICAL: grey + pre_fix + bold_red + format_style + reset
        }

    def format(self, record):
        """Format a logging record, just applying styling
        """
        if self.use_colors:
            log_fmt = self._formats.get(record.levelno)
            formatter = logging.Formatter(log_fmt, "%Y-%m-%d %H:%M:%S")
        else:
            formatter = logging.Formatter("%(asctime)s\n%(levelname)s:%(name)s - %(message)s",
                                       "%Y-%m-%d %H:%M:%S")
        return formatter.format(record)