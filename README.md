# NumPy Reshaping and Manipulating Arrays

## 📌 Introduction

NumPy provides powerful functions to reshape and manipulate arrays without changing the original data. These operations help organize, transform, combine, split, and modify arrays efficiently, making them essential for data analysis, machine learning, and scientific computing.

---

# 📖 Table of Contents

- What is Reshaping?
- reshape()
- flatten()
- ravel()
- transpose()
- resize()
- expand_dims()
- squeeze()
- concatenate()
- stack()
- hstack()
- vstack()
- dstack()
- split()
- hsplit()
- vsplit()
- append()
- insert()
- delete()
- sort()
- unique()
- Practical Example
- Summary

---

# Creating an Array

```python
import numpy as np

arr = np.array([1,2,3,4,5,6])

print(arr)
```

Output

```
[1 2 3 4 5 6]
```

---

# 1. reshape()

Changes the shape of an array without changing its data.

### Syntax

```python
array.reshape(rows, columns)
```

### Example

```python
import numpy as np

arr = np.array([1,2,3,4,5,6])

new_arr = arr.reshape(2,3)

print(new_arr)
```

Output

```
[[1 2 3]
 [4 5 6]]
```

---

# 2. flatten()

Converts a multi-dimensional array into a one-dimensional array.

```python
import numpy as np

arr = np.array([[1,2],[3,4]])

print(arr.flatten())
```

Output

```
[1 2 3 4]
```

---

# 3. ravel()

Returns a flattened view of the array.

```python
import numpy as np

arr = np.array([[1,2],[3,4]])

print(arr.ravel())
```

Output

```
[1 2 3 4]
```

---

# Difference Between flatten() and ravel()

| flatten() | ravel() |
|------------|----------|
| Returns a copy | Returns a view (if possible) |
| More memory | Less memory |
| Changes don't affect original | Changes may affect original |

---

# 4. transpose()

Interchanges rows and columns.

```python
import numpy as np

arr = np.array([[1,2,3],
                [4,5,6]])

print(arr.T)
```

Output

```
[[1 4]
 [2 5]
 [3 6]]
```

---

# 5. resize()

Changes the shape of the original array.

```python
import numpy as np

arr = np.array([1,2,3,4])

arr.resize((2,2))

print(arr)
```

Output

```
[[1 2]
 [3 4]]
```

---

# 6. expand_dims()

Adds a new axis.

```python
import numpy as np

arr = np.array([1,2,3])

new_arr = np.expand_dims(arr, axis=0)

print(new_arr)
```

Output

```
[[1 2 3]]
```

---

# 7. squeeze()

Removes dimensions of size 1.

```python
import numpy as np

arr = np.array([[[10,20,30]]])

print(np.squeeze(arr))
```

Output

```
[10 20 30]
```

---

# 8. concatenate()

Joins arrays along an existing axis.

```python
import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

print(np.concatenate((a,b)))
```

Output

```
[1 2 3 4 5 6]
```

---

# 9. stack()

Joins arrays along a new axis.

```python
import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

print(np.stack((a,b)))
```

Output

```
[[1 2 3]
 [4 5 6]]
```

---

# 10. hstack()

Stacks arrays horizontally.

```python
import numpy as np

a = np.array([1,2])
b = np.array([3,4])

print(np.hstack((a,b)))
```

Output

```
[1 2 3 4]
```

---

# 11. vstack()

Stacks arrays vertically.

```python
import numpy as np

a = np.array([1,2])
b = np.array([3,4])

print(np.vstack((a,b)))
```

Output

```
[[1 2]
 [3 4]]
```

---

# 12. dstack()

Stacks arrays depth-wise.

```python
import numpy as np

a = np.array([[1],[2]])
b = np.array([[3],[4]])

print(np.dstack((a,b)))
```

Output

```
[[[1 3]]

 [[2 4]]]
```

---

# 13. split()

Splits an array into equal parts.

```python
import numpy as np

arr = np.array([1,2,3,4,5,6])

print(np.split(arr,3))
```

Output

```
[array([1,2]), array([3,4]), array([5,6])]
```

---

# 14. hsplit()

Splits columns.

```python
import numpy as np

arr = np.array([[1,2,3,4],
                [5,6,7,8]])

print(np.hsplit(arr,2))
```

Output

```
[array([[1,2],
       [5,6]]),

 array([[3,4],
       [7,8]])]
```

---

# 15. vsplit()

Splits rows.

```python
import numpy as np

arr = np.array([[1,2],
                [3,4],
                [5,6],
                [7,8]])

print(np.vsplit(arr,2))
```

Output

```
[array([[1,2],
       [3,4]]),

 array([[5,6],
       [7,8]])]
```

---

# 16. append()

Adds values at the end.

```python
import numpy as np

arr = np.array([1,2,3])

print(np.append(arr,4))
```

Output

```
[1 2 3 4]
```

---

# 17. insert()

Inserts values at a specified position.

```python
import numpy as np

arr = np.array([10,20,30])

print(np.insert(arr,1,15))
```

Output

```
[10 15 20 30]
```

---

# 18. delete()

Deletes elements from an array.

```python
import numpy as np

arr = np.array([10,20,30,40])

print(np.delete(arr,2))
```

Output

```
[10 20 40]
```

---

# 19. sort()

Sorts array elements.

```python
import numpy as np

arr = np.array([4,2,1,3])

print(np.sort(arr))
```

Output

```
[1 2 3 4]
```

---

# 20. unique()

Returns unique elements.

```python
import numpy as np

arr = np.array([1,2,2,3,4,4,5])

print(np.unique(arr))
```

Output

```
[1 2 3 4 5]
```

---

# Practical Example

```python
import numpy as np

data = np.arange(1,13)

matrix = data.reshape(3,4)

print("Original Matrix:")
print(matrix)

print("\nTranspose:")
print(matrix.T)

print("\nFlatten:")
print(matrix.flatten())

print("\nFirst Two Rows:")
print(matrix[:2])

print("\nHorizontal Split:")
print(np.hsplit(matrix,2))
```

Output

```
Original Matrix
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]

Transpose
[[ 1  5  9]
 [ 2  6 10]
 [ 3  7 11]
 [ 4  8 12]]

Flatten
[ 1 2 3 4 5 6 7 8 9 10 11 12]
```

---

# Summary Table

| Function | Description |
|----------|-------------|
| `reshape()` | Change array shape |
| `flatten()` | Convert to 1D (copy) |
| `ravel()` | Convert to 1D (view if possible) |
| `transpose()` / `.T` | Swap rows and columns |
| `resize()` | Resize original array |
| `expand_dims()` | Add a new dimension |
| `squeeze()` | Remove dimensions of size 1 |
| `concatenate()` | Join arrays |
| `stack()` | Stack along a new axis |
| `hstack()` | Horizontal stacking |
| `vstack()` | Vertical stacking |
| `dstack()` | Depth-wise stacking |
| `split()` | Split into equal parts |
| `hsplit()` | Split columns |
| `vsplit()` | Split rows |
| `append()` | Add elements |
| `insert()` | Insert elements |
| `delete()` | Delete elements |
| `sort()` | Sort array |
| `unique()` | Return unique values |

---

# Applications

- Data preprocessing
- Machine Learning
- Data Cleaning
- Image Processing
- Scientific Computing
- Matrix Operations
- Feature Engineering
- Statistical Analysis

---

# Conclusion

NumPy's reshaping and manipulation functions make it easy to reorganize, combine, split, and modify arrays efficiently. Mastering these operations is essential for working with large datasets and building high-performance data science and machine learning applications.
