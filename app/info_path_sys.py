import os
import re
import sys
import platform
from os.path import expanduser

os_name = platform.system().lower()
current_user = expanduser("~")
path_to_project = os.path.dirname(os.path.abspath(__file__))


def get_option(option):
    """
    :param option: matched option
    :return: value of option or None
    :example: get_option('--env')
    """
    value = None
    all_argv = sys.argv
    for arg in all_argv:
        reg = re.match(r"(%s.*)" % option, arg)
        if reg:
            key, value = reg.group().split("=")
            break
    return value if value is not None else None
