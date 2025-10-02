import time

def measure_time(func, *args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    print(f"Function '{func.__name__}' executed in {end-start:.6f} seconds")
    return result

