# core/ndarray.py

class CustomArray:
    def __init__(self, data):
        self.data = data
        self.shape = self._calculate_shape(data)
        self.ndim = len(self.shape)

    def _calculate_shape(self, data):
        # not a list means we've hit a raw value
        if not isinstance(data, list):
            return ()
        if not data:
            return (0,)

        inner_shape = self._calculate_shape(data[0])
        return (len(data),) + inner_shape

    def __repr__(self):
        return f"CustomArray({self.data})\nShape: {self.shape}, Dimensions: {self.ndim}"

    def __add__(self, other):
        # adding a number to every element
        if isinstance(other, (int, float)):
            return CustomArray(self._add_scalar(self.data, other))

        # adding two arrays together
        elif isinstance(other, CustomArray):
            if self.shape != other.shape:
                raise ValueError(f"Shape mismatch: {self.shape} vs {other.shape}")
            return CustomArray(self._add_array(self.data, other.data))

        else:
            raise TypeError("Can only add a number or another CustomArray.")

    def _add_scalar(self, data, scalar):
        # base case: just add the number
        if not isinstance(data, list):
            return data + scalar
        return [self._add_scalar(item, scalar) for item in data]

    def _add_array(self, data1, data2):
        # base case: add the two elements
        if not isinstance(data1, list):
            return data1 + data2
        return [self._add_array(a, b) for a, b in zip(data1, data2)]
        # Subtraction
    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return CustomArray(self._sub_scalar(self.data, other))
        elif isinstance(other, CustomArray):
            if self.shape != other.shape:
                raise ValueError(f"Shape mismatch: {self.shape} vs {other.shape}")
            return CustomArray(self._sub_array(self.data, other.data))
        raise TypeError("Can only subtract a number or another CustomArray.")

    def _sub_scalar(self, data, scalar):
        if not isinstance(data, list):
            return data - scalar
        return [self._sub_scalar(item, scalar) for item in data]

    def _sub_array(self, data1, data2):
        if not isinstance(data1, list):
            return data1 - data2
        return [self._sub_array(a, b) for a, b in zip(data1, data2)]


    # Multiplication
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return CustomArray(self._mul_scalar(self.data, other))
        elif isinstance(other, CustomArray):
            if self.shape != other.shape:
                raise ValueError(f"Shape mismatch: {self.shape} vs {other.shape}")
            return CustomArray(self._mul_array(self.data, other.data))
        raise TypeError("Can only multiply by a number or another CustomArray.")

    def _mul_scalar(self, data, scalar):
        if not isinstance(data, list):
            return data * scalar
        return [self._mul_scalar(item, scalar) for item in data]

    def _mul_array(self, data1, data2):
        if not isinstance(data1, list):
            return data1 * data2
        return [self._mul_array(a, b) for a, b in zip(data1, data2)]


    # Power
    def __pow__(self, other):
        if isinstance(other, (int, float)):
            return CustomArray(self._pow_scalar(self.data, other))
        elif isinstance(other, CustomArray):
            if self.shape != other.shape:
                raise ValueError(f"Shape mismatch: {self.shape} vs {other.shape}")
            return CustomArray(self._pow_array(self.data, other.data))
        raise TypeError("Can only raise to a number or another CustomArray.")

    def _pow_scalar(self, data, scalar):
        if not isinstance(data, list):
            return data ** scalar
        return [self._pow_scalar(item, scalar) for item in data]

    def _pow_array(self, data1, data2):
        if not isinstance(data1, list):
            return data1 ** data2
        return [self._pow_array(a, b) for a, b in zip(data1, data2)]


    # Flatten to 1D
    def flatten(self):
        return CustomArray(self._flatten_recursive(self.data))

    def _flatten_recursive(self, data):
        # base case: wrap the number in a list
        if not isinstance(data, list):
            return [data]
        result = []
        for item in data:
            result.extend(self._flatten_recursive(item))
        return result

