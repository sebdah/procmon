# procmon

`procmon` is a small utility for checking whether certain processes are found in the `ps -ef` process list. The utility is not a daemon, meaning it will run once and then die. So to monitor that a certain process is running, you would for example have `procmon` in cron.

## Configuration

### Configuration file locations

`procmon` is looking for configuration files in the following paths:

- `/etc/procmon.cfg`
- `./procmon.cfg`

### Sample configuration file

Below is an example of what the `procmon.cfg` file could look like.

    [General]
    # FilterString is the string in 'ps -ef' to look for. It could be a process
    # name, a process id or something similar.
    FilterString = mtlcompilerservice
    
    # CaseInsensitive determines if the FilterString should be matched sensitive to
    # case or not.
    CaseInsensitive = yes
    
    # MatchCount sets how many matches we're required to find. procmon will fail if
    # less than this count is found (but succeed if the count is equal to or higher
    # than this).
    MatchCount = 1
    
    # LogLevel for the logging output.
    #
    # Valid values: debug, info, warning, error
    LogLevel = debug
    
    # SendEmailNotification is turning on or off email notifications.
    SendEmailNotification = yes
    
    [SMTP]
    # Host for the SMTP server.
    Host = smtp.gmail.com
    
    # Port to connect to.
    #
    # Typically 25 for non-SSL connections and 465 for SSL connections.
    Port = 465
    
    # UseSSL is turning SSL on and off.
    UseSSL = yes
    
    # Username for the SMTP server.
    Username = sebastian.dahlgren@gmail.com
    
    # Password for the SMTP server.
    Password = nobqrqlcivwzdinw
    
    [Email]
    # FromAddress is setting which email address the email notification should be
    # sent from.
    #
    # Unlike ToAddresses this can only be one address.
    FromAddress = sebastian.dahlgren@gmail.com
    
    # ToAddresses is a comma separated list of email addresses that should receive
    # the notification.
    ToAddresses = sebastian@saltside.se
