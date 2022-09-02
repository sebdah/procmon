import configparser
import os.path

from logger import log


config = configparser.ConfigParser()


def read(paths=None):
    """ Read configuration file(s)

    Parameters
    ----------
    paths : list[str]
        Paths to look for the configuration files in.
    """
    if paths is None:
        paths = [
            '/etc/procmon.cfg',
            os.path.join(os.getcwd(), 'procmon.cfg')
        ]

    log.debug(f'Reading configuration from: %s', ', '.join(paths))
    config.read(paths)
