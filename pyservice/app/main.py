import functools
from .utils import before_run
from .utils import get_args_parser
from .utils import set_app_args

def main(app_name):

    def main_decorator(some_func):
        @functools.wraps(some_func)
        def wrapper(*args, **kwargs):
            cmd_args = get_args_parser()
            try:
                before_run(app_name, cmd_args)
                set_app_args(cmd_args)
                result = some_func(*args, **kwargs)
                return result
            except KeyboardInterrupt:
                import sys
                sys.exit(-1)
            except SystemExit:
                pass
        return wrapper

    return main_decorator