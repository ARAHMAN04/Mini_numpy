# Mini NumPy Library

A simplified version of the NumPy library built from scratch using pure Python. This project demonstrates core Object-Oriented Programming (OOP) principles, modern Python development practices, and internal array memory management.

## 🚀 Features

* **Custom Array Class:** A robust `ndarray` equivalent that manages data, shape, and dimensions.
* **Array Creation:** Built-in functions to generate arrays (`array`, `zeros`, `ones`, `eye`).
* **Operator Overloading:** Full support for mathematical operations (`+`, `-`, `*`, `**`) between arrays and scalars using Python magic methods.
* **Statistical Functions:** Calculate `mean()`, `var()`, and `std()` across array elements.
* **Array Manipulation:** Flatten multi-dimensional arrays while preserving element order.
* **Robust Validation:** Integrated `Pydantic` models to ensure strict shape and numeric data validation.
* **Custom Error Handling:** Clear, informative exceptions for invalid shapes, dimension mismatches, and unsupported operations.

## 📂 Project Architecture

```text
mini_numpy/
│
├── core/
│   └── ndarray.py           # Base CustomArray class and magic methods
│
├── creation/
│   └── array_creation.py    # np.array, zeros, ones, eye implementations
│
├── statistics/
│   └── stats.py             # mean, var, std, and flatten operations
│
├── exceptions/
│   └── errors.py            # Custom Exception classes
│
├── validation/
│   └── schemas.py           # Pydantic validation models
│
└── main.py                  # Project entry point and integration testing