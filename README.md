<br />
<p align="center">
<img src="https://github.com/sebdah/procmon/blob/main/images/procmon.png?raw=true" alt="procmon logo"><br /><br />
<img src="https://github.com/sebdah/procmon/actions/workflows/python-package.yml/badge.svg" alt="Python tests badge">
</p>

`procmon` is a small utility for checking whether certain processes are found in the `ps -ef` process list. The utility is not a daemon, meaning it will run once and then die. So to monitor that a certain process is running, you would for example have `procmon` in cron.

If the looked for process is running, `promon` will exit with return code `0`. If the process isn't found or if not enough processes are found (see `-e` flag), then `procmon` exits with `1`.

# Usage

Check if a process is running:

    procmon "firefox -param"

Make the filter case-insensitive (`-i` / `--insensitive`):

    procmon -i "FiReFox -param"

Mandate the minimum number of matched processes expected (default is 1):

    procmon -e 5 "firefox -param"

Setting the log level:

    procmon --log-level debug "firefox -param"

Sending an email notification on error. This requires you to have a `procmon.cfg` configured with the SMTP server settings:

    procmon --send-email "firefox -param"

# Configuration

The configuration of `procmon` happens at two levels; 

1. In the CLI (command line interface)
2. In a configuration file (this is where SMTP settings etc are)

## CLI

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

## Configuration file

Using a configuration file is _entirely optional_ for users that are not using the `--send-email` option. The configuration file is only used for configuring SMTP settings and similar.

### Paths

`procmon` is looking for configuration files in the following paths:

- `/etc/procmon.cfg`
- `./procmon.cfg`

### Example configuration file

A full example of a configuration file can be found under [https://github.com/sebdah/procmon/blob/main/examples/procmon.cfg](https://github.com/sebdah/procmon/blob/main/examples/procmon.cfg)

### Example

The below command would be looking for a process called `python bpytop` (case insensitive). It would expect to find _at least_ 2 matches. And it would be logging on the debug level.

    procmon -i --log-level debug -m 2 python bpytop

# Development

## EditorConfig

The project uses [EditorConfig](https://editorconfig.org/) for configuration of IDEs for development. Please make sure you have EditorConfig enabled in your IDE when developing, that will make your code abide to the coding guidelines automatically.

## Running tests

The `Makefile` is configured for running tests unless you want to run it in your editor. Simply execute:

    make test

This assumes that Python and `pytest` are available on your host.

# License
APACHE LICENSE 2.0 Copyright 2022 Sebastian Dahlgren

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
