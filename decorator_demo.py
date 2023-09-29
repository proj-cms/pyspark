import json
import math
from typing import Callable


def memoize(target: Callable):
    cache: dict = {}

    def replacement(*args: any):
        key: str = json.dumps(args)
        print(f"within replacement and key is {key}")
        value: any = cache.get(key)
        print(f"within replacement and value  is {value}")

        if not value:
            print(f"{value} value not found in cache , adding to cache with  key {key}")
            value = target(*args)  ## this is the place it calls the target function
            print(f"{value} value not found in cache , adding to cache with  key {key}")
            cache[key] = value
        return value

    return replacement


@memoize
def is_prime(value: int):
    print(f"is_prime called with  {value}")
    max_range: int = int(math.sqrt(value))

    for div in range(2, max_range):
        if value % div == 0:
            return False
    return True


if __name__ == "__main__":
    print("call - 1-----")
    print(is_prime(10011))
    print("call - 2-----")
    print(is_prime(10011))
