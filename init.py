import sys

def debug_print(*args, **kwargs):
    print(*args, **kwargs, file=sys.stderr)
