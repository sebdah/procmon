# procmon

`procmon` is a small utility for checking whether certain processes are found in the `ps -ef` process list. The utility is not a daemon, meaning it will run once and then die. So to monitor that a certain process is running, you would for example have `procmon` in cron.

## Configuration

### Configuration file locations

`procmon` is looking for configuration files in the following paths:

- `/etc/procmon.cfg`
- `./procmon.cfg`

### Example configuration file

A full example of a configuration file can be found under [https://github.com/sebdah/procmon/blob/main/examples/procmon.cfg](https://github.com/sebdah/procmon/blob/main/examples/procmon.cfg)
