# [Typing Module](https://docs.python.org/3/library/typing.html#module-typing 'View full documentation')

- This module provides runtime support for type hints.
- Introduced in Lab 1.2

#### Consider the function below:

```python
def surface_area_of_cube(edge_length: float) -> str:
    return f"The surface area of the cube is {6 * edge_length ** 2}."
```

- The function surface_area_of_cube takes an argument expected to be an instance of float, as indicated by the type hint edge_length: float. The function is expected to return an instance of str, as indicated by the ->
