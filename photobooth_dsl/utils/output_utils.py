import re


def check_format(file_name):
    file_format_pattern = r'[a-zA-Z0-9-_.:\/]+\.([a-zA-Z0-9]+)'
    regex = re.compile(file_format_pattern)

    if regex.match(file_name):
        return True
    else:
        return False
