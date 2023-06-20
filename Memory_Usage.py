import os
from psutil import Process

def get_memory_usage() -> float:
    process: Process = Process(os.getpid())
    megabytes: float = process.memory_info().rss / (1024 * 1024)

    return megabytes

memory_before_import: float = get_memory_usage()

# import numpy
# from numpy import pi

memory_after_import: float = get_memory_usage()
memory_difference: float = memory_after_import - memory_before_import

print(f"Before import: {memory_before_import:.2f} MB")
print(f"After import: {memory_before_import:.2f} MB")
print(f"Difference import: {memory_before_import:.2f} MB")
