# exceptions/errors.py

class InvalidShapeError(ValueError):
    # unequal row lengths
    pass

class DimensionMismatchError(ValueError):
    # shapes don't match
    pass

class NonNumericDataError(TypeError):
    # non-number found in array
    pass

class InvalidOperationError(Exception):
    # unsupported operation
    pass