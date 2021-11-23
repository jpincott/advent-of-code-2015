import time
from contextlib import contextmanager


@contextmanager
def timer(name):
    print(f"Starting {name}")
    start_time = time.perf_counter()
    yield start_time
    print(f"Finished {name} in {time.perf_counter() - start_time :.4f} secs")
