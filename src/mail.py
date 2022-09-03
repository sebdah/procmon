import smtplib
import socket
import ssl

from src.config import config
from src.logger import log, log_stream


def build_email_message(filter_string: str, case_insensitive: bool, match_count: int, expected_matches: int):
    """ build_email_message is returning a text email based on a number of variables

    Parameters
    ----------
    filter_string : str
        String to filter for.
    case_insensitive : bool
        Filter insensitive to case.
    match_count : int
        Number of processes matching the filter that was found
    expected_matches : int
        Number of expected matches

    Returns
    -------
    str
        Email message as a string
    """
    from_address = config.get('Email', 'FromAddress')
    to_addresses = []
    for addr in config.get('Email', 'ToAddresses').split(','):
        to_addresses.append(addr.strip(' '))

    return f"""From: Process monitor <{from_address}>
To: {to_addresses}
MIME-Version: 1.0
Content-type: text/plain
Subject: [procmon] Alert - Expected processes aren't running (found {match_count} of {expected_matches})

Warning! We found {match_count} of expected {expected_matches} processes running on the system.

Host name: {socket.gethostname()}
Host IP: {socket.gethostbyname(socket.gethostname())}

------------------ Settings -------------------------
Filter string: {filter_string}
Case insensitive?: {case_insensitive}
Expected process match count: {expected_matches}
-----------------------------------------------------

------------------ Log output -----------------------
{log_stream.getvalue()}
-----------------------------------------------------
This is an automatic email from procmon.
"""


def send_email(message: str):
    host = config.get('SMTP', 'Host')
    port = config.getint('SMTP', 'Port')
    use_ssl = config.getboolean('SMTP', 'UseSSL')
    username = config.get('SMTP', 'Username')
    password = config.get('SMTP', 'Password')
    from_address = config.get('Email', 'FromAddress')
    to_addresses = []
    for addr in config.get('Email', 'ToAddresses').split(','):
        to_addresses.append(addr.strip(' '))

    try:
        if use_ssl:
            log.debug(f'Connecting to SMTP server {host}:{port} over SSL')
            ctx = ssl.create_default_context()

            with smtplib.SMTP_SSL(host, port, context=ctx) as smtp:
                smtp.login(username, password)
                smtp.sendmail(from_address, to_addresses, message)

        else:
            log.debug(f'Connecting to SMTP server {host}:{port} without SSL')
            with smtplib.SMTP(host, port) as smtp:
                smtp.login(username, password)
                smtp.sendmail(from_address, to_addresses, message)

        log.info(f'Alert email sent to {", ".join(to_addresses)}')
    except smtplib.SMTPException as e:
        log.error(f'Failed to send email: %s' % e)
    except ConnectionRefusedError as e:
        log.error(f'Failed to connect to the SMTP server: %s' % e)
    except Exception as e:
        log.error(f'Unexpected error: %s' % e)
