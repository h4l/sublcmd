from __future__ import print_function, unicode_literals

import sys
import os
import subprocess
import tempfile

__version__ = '0.0.0'


class SublCmdError(Exception):
    def __init__(self, msg, exit_status):
        super(SublCmdError, self).__init__(msg)
        self.exit_status = exit_status


def get_subl_cmd():
    subl_cmd = os.environ.get('SUBL')
    if subl_cmd is None:
        raise SublCmdError('SUBL environment variable is not set', 2)

    if not os.path.isfile(subl_cmd):
        raise SublCmdError('SUBL envar does not point to an existing file: {}'
                           .format(subl_cmd), 3)

    return subl_cmd


def execute_sublime(args):
    subprocess.check_call([get_subl_cmd()] + args)


def main():
    args = sys.argv[1:]

    # Handle passing data to stdin
    if not sys.stdin.isatty():
        with os.fdopen(sys.stdin.fileno(), 'rb') as stdin:
            handle, subl_stdin_path = tempfile.mkstemp(prefix='subl-stdin')
            with os.fdopen(handle, 'wb') as subl_stdin_file:
                subl_stdin_file.write(stdin.read())
        args.append(subl_stdin_path)

    try:
        execute_sublime(args)

    except SublCmdError as e:
        print('Fatal: {}'.format(e))
        sys.exit(e.exit_status)

if __name__ == '__main__':
    main()
