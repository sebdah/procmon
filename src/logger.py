from io import StringIO
import logging
import sys

log_levels = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR
}

basic_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setFormatter(basic_formatter)

log_stream = StringIO()
string_handler = logging.StreamHandler(log_stream)
string_handler.setFormatter(basic_formatter)

log = logging.getLogger()
log.setLevel(logging.INFO)
log.addHandler(stdout_handler)
log.addHandler(string_handler)


def set_log_level(level: str):
    """ set_log_level of the logger

    Parameters
    ----------
    level : str
        Log level (info, debug, warning, error)
    """
    log.setLevel(log_levels[level])
