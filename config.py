import configparser
import os.path


config = configparser.ConfigParser()
config.read([
    '/etc/procmon.cfg',
    os.path.join(os.getcwd(), 'procmon.cfg')
])
