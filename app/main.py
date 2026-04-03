from typing import Callable


def cache(func: Callable) -> Callable:
    cash = []
    def wrapper(*args, **kwargs) -> None:
        if args or kwargs in cash:
            print ("Calculating new result")
        else:
            cash.append((args, kwargs))
            print ("Getting from cache")
        return wrapper
