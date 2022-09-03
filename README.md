# procmon

<img src="https://github.com/sebdah/procmon/blob/main/images/process-list.jpg?raw=true">

`procmon` is a small utility for checking whether certain processes are found in the `ps -ef` process list. The utility is not a daemon, meaning it will run once and then die. So to monitor that a certain process is running, you would for example have `procmon` in cron.

## Configuration

The configuration of `procmon` happens at two levels; 

1. In a configuration file (this is where SMTP settings etc are)
2. In the CLI (command line interface)

### Configuration file

#### Paths

`procmon` is looking for configuration files in the following paths:

- `/etc/procmon.cfg`
- `./procmon.cfg`

#### Example configuration file

A full example of a configuration file can be found under [https://github.com/sebdah/procmon/blob/main/examples/procmon.cfg](https://github.com/sebdah/procmon/blob/main/examples/procmon.cfg)

### CLI

    procmon [OPTIONS] <filter string>

    Options:
        -c, --config string         Path for configuration file (default: /etc/procmon.cfg, ./procmon.cfg)
        -h, --help                  Print this help text
        -i, --insensitive           Case insensitive process matching
        -l, --log-level string      Log level; debug, info, warning, error (default: info)
        -m, --match-count int       Number of matches required for a successful result (default: 1)   

#### Example

The below command would be looking for a process called `python bpytop` (case insensitive). It would expect to find _at least_ 2 matches. And it would be logging on the debug level.

    procmon -i --log-level debug -m 2 python bpytop

## Running tests

The `Makefile` is configured for running tests unless you want to run it in your editor. Simply execute:

    make test

This assumes that Python and `pytest` are available on your host.
