## Rotation

Write a Python function to rotate a square matrix (a list of lists) 90 degrees clockwise. For example:

```Py
matrix = [
    [0, 1],
    [2, 3]
]

rotated_matrix = rotate(matrix)

print_matrix(matrix)
# prints
# [0, 1]
# [2, 3]

print_matrix(rotated_matrix)
# prints
# [2, 0]
# [3, 1]
```

In case the matrix is not a square, raise a `NonSquareMatrixError`.

```Py
class NonSquareMatrixError(Exception):
    pass

def print_matrix(matrix: list[list[int]]) -> None:
    for row in matrix:
        print(row)

def rotate(matrix: list[list[int]]) -> list[list[int]]:
    # TODO
    pass
```

Write a Pytest unittest for each of the following:

* Rotation of a matrix of an even size (2x2)
* Rotation of a matrix of an uneven size (3x3)
* Rotation of a 1x1 matrix
* Rotation of an empty matrix
* Rotation of a non-square matrix
* That rotate does not modify the original matrix
* That four rotations equal the original matrix


## Table tennis with words

We are creating a new app: [table tennis with words](https://youtu.be/Wu1kSXpVV8Y?t=2319). These are the rules:

The word spoken must begin with the last letter of the previous word. If you cannot think of a word within three seconds, or repeat a word, you are out.

As part of this new app, we need the function below:

```Py
def guess(word: str, previous_words: list[str], time: float): -> bool
    # TODO
    pass
```

Implement the function above. This function should return False if any rule is broken, True otherwise. Raise a `ValueError` if the input is invalid.

Write Pytest unnittests to test the function `guess`. Be sure to test:

* Normal operation: normal input yields expected output
* Edgecases, such as empty lists, one letter words, the number 0, etc.
* Handling of illegal input