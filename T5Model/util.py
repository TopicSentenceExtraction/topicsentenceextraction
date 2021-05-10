import logging
import time

logging.basicConfig(level=logging.INFO)
transformers_logger = logging.getLogger("t5-small")
transformers_logger.setLevel(logging.WARNING)

def print_run_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        back = func(*args, **kwargs)
        print('Function [%s] run time is %.2fs' % (func.__name__ , time.time() - start_time))
        return back
    return wrapper