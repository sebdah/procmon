<center>
<img src="https://github.com/sebdah/procmon/blob/main/images/procmon.png?raw=true" alt="procmon logo"><br /><br />
<img src="https://github.com/sebdah/procmon/actions/workflows/python-package.yml/badge.svg" alt="Python tests badge">
</center>

`procmon` is a small utility for checking whether certain processes are found in the `ps -ef` process list. The utility is not a daemon, meaning it will run once and then die. So to monitor that a certain process is running, you would for example have `procmon` in cron.

## Configuration

The configuration of `procmon` happens at two levels; 

1. In the CLI (command line interface)
2. In a configuration file (this is where SMTP settings etc are)

### CLI

The below is a copy of the `procmon --help` output. It shows available configuration parameters and their meaning.

    usage: procmon [-h] [-c CONFIG] [-e EXPECTED_MATCHES] [-i] [--send-email] [--log-level LOG_LEVEL] [--version] [filter]

    positional arguments:
      filter                Filter string to match processes for
    
    options:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            Path for configuration file (default: /etc/procmon.cfg, ./procmon.cfg)
      -e EXPECTED_MATCHES, --expected-matches EXPECTED_MATCHES
                            Number of matches required for a successful result
      -i, --insensitive     Case insensitive process matching
      --send-email          Send email notification
      --log-level LOG_LEVEL
                            Log level; debug, info, warning, error
      --version             Print the procmon version number

### Configuration file

Using a configuration file is _entirely optional_ for users that are not using the `--send-email` option. The configuration file is only used for configuring SMTP settings and similar.

#### Paths

`procmon` is looking for configuration files in the following paths:

- `/etc/procmon.cfg`
- `./procmon.cfg`

#### Example configuration file

A full example of a configuration file can be found under [https://github.com/sebdah/procmon/blob/main/examples/procmon.cfg](https://github.com/sebdah/procmon/blob/main/examples/procmon.cfg)

#### Example

The below command would be looking for a process called `python bpytop` (case insensitive). It would expect to find _at least_ 2 matches. And it would be logging on the debug level.

    procmon -i --log-level debug -m 2 python bpytop

## Running tests

The `Makefile` is configured for running tests unless you want to run it in your editor. Simply execute:

    make test

This assumes that Python and `pytest` are available on your host.
