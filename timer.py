import time
from typing import Callable

def timer(func: Callable) -> Callable:
    def timer_wrapper(*args, **kwargs) -> None:
        start = time.time()
        func(*args, **kwargs)
        print(f"{func.__name__} executed in {time.time() - start} seconds")
    return timer_wrapper