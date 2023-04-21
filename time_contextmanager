import time
from contextlib import contextmanager

def kill_time():
    time.sleep(1)

@contextmanager
def timer(label: str):
    start: float = time.perf_counter()
    try:
        yield
    finally:
        end: float = time.perf_counter()
        print(f"{label}: {end - start:.3f} second")

with timer("Func"):
    kill_time()
    
# Answer: Func1.001 second
