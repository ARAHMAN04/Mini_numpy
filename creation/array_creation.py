# creation/array_creation.py
from core.ndarray import CustomArray
from validation.schemas import ArraySchema

def array(data):
    return CustomArray(ArraySchema(data=data).data)

def zeros(shape):
    def _build(s):
        if len(s) == 1:
            return [0.0] * s[0]
        return [_build(s[1:]) for _ in range(s[0])]
    if isinstance(shape, int):
        shape = (shape,)
    return CustomArray(_build(shape))

def ones(shape):
    def _build(s):
        if len(s) == 1:
            return [1.0] * s[0]
        return [_build(s[1:]) for _ in range(s[0])]
    if isinstance(shape, int):
        shape = (shape,)
    return CustomArray(_build(shape))

def eye(m, n=None, k=0):
    if n is None:
        n = m
    matrix = [
        [1.0 if j - i == k else 0.0 for j in range(n)]
        for i in range(m)
    ]
    return CustomArray(matrix)

