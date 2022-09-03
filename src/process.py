import subprocess

from src.logger import log


def match(source: str, filter_string: str, case_insensitive=False):
    """ match is returning the number of matched processes found

    Parameters
    ----------
    source : str
        Source string used for looking for the filter_string in.
    filter_string : str
        String to filter for.
    case_insensitive : bool
        Filter insensitive to case.

    Returns
    -------
    bool
        Returns True if the string was matched
    """
    if filter_string == '':
        return False

    if case_insensitive:
        filter_string = filter_string.lower()

    source_original_clean = source.rstrip('\n').strip(' ')
    source_cmp = source_original_clean
    if case_insensitive:
        source_cmp = source_cmp.lower()

    log.debug(f'Looking for "{filter_string}" in "{source_original_clean}"')
    if source_cmp.find(filter_string) < 0:
        return False

    log.info(f'Matching process found: "%s"' % source_original_clean)
    return True


def list_processes():
    """ Lists all processes

    The function is not returning anything, instead it's yielding log lines to the calling function.
    """
    cmd = 'ps -ef'
    ps_cmd = subprocess.Popen(cmd.split(' '), stdout=subprocess.PIPE, universal_newlines=True)

    for line in ps_cmd.stdout:
        yield line

    ps_cmd.stdout.close()

    return_code = ps_cmd.wait()
    if return_code:
        raise subprocess.CalledProcessError(return_code, cmd)
