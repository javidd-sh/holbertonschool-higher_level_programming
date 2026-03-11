# Square Matrix Simple

## Description

This project contains a Python function that computes the **square value of all integers in a matrix**.

The function takes a **2D list (matrix)** as input and returns a **new matrix** of the same size where each value is the **square of the corresponding value in the original matrix**.

The **original matrix remains unchanged**.

## Prototype

```python
def square_matrix_simple(matrix=[])
```

## Requirements

* Python 3.x
* Do not import any module
* The original matrix must not be modified
* The returned matrix must have the same size as the input matrix

## Parameters

| Parameter | Type          | Description                    |
| --------- | ------------- | ------------------------------ |
| matrix    | list of lists | A 2D array containing integers |

## Return

* A **new matrix** with the same dimensions as the input matrix.
* Each element is the **square** of the corresponding element in the input matrix.

## Example

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)

print(new_matrix)
print(matrix)
```

### Output

```
[[1, 4, 9], [16, 25, 36], [49, 64, 81]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

## Implementation

```python
#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [[value ** 2 for value in row] for row in matrix]
```

## Author

Cavid
