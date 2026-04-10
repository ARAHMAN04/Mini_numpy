# statistics/stats.py
from core.ndarray import CustomArray

def mean(arr: CustomArray):
    flat = arr.flatten().data
    if not flat:
        return 0.0
    return sum(flat) / len(flat)

def var(arr: CustomArray):
    flat = arr.flatten().data
    if not flat:
        return 0.0
    m = mean(arr)
    return sum((x - m) ** 2 for x in flat) / len(flat)

def std(arr: CustomArray):
    return var(arr) ** 0.5

