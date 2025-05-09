# Binary Storage

## Problem Description

A scientist needs to store DNA information in a database where each record is represented as a binary number with a fixed number of set bits. To optimize storage, these binary numbers are stored as lists of integers representing the indices of the set bits (1 bits), starting from the rightmost bit (least significant bit) and given in random order.

### Given

* A list of binary numbers, each represented as a list of indices of the set bits.
* The binary numbers are stored in random order.

### Task

Sort these binary numbers in descending order based on their decimal values and return the sorted list of their original indices.

### Example

#### Input

```
bitArrays = [[0, 2], [2, 3], [2, 1]]
```

#### Step-by-step Execution

1. Convert each list of indices to its binary representation and then to its decimal value:

   * \[0, 2] -> 0101 -> 5
   * \[2, 3] -> 1100 -> 12
   * \[2, 1] -> 0110 -> 6

2. Sort the binary numbers in descending order by their decimal values:

   * \[12, 6, 5]

3. Return the indices of the sorted binary numbers:

```
[1, 2, 0]
```

## Constraints

* `1 ≤ n, m ≤ 10^3` (Number of rows and columns)
* `0 ≤ bitArrays[i][j] ≤ 10^9`
* All integers in a row are distinct.
* Each row generates a unique binary number.

## Function Description

Complete the function `sortBinaryNumbers` with the following parameter:

```python
sortBinaryNumbers(bitArrays: List[List[int]]) -> List[int]
```

* `bitArrays`: A list of lists, where each sublist represents the indices of the set bits for each binary number.

### Returns

* A list of integers representing the sorted indices of the binary numbers in descending order of their decimal values.

## Sample Case

### Input

```
2
3
0 1 2
3 1 0
```

### Output

```
1
0
```

### Explanation

* The corresponding binary numbers are:

  * Index 0: 0111 (7 in decimal)
  * Index 1: 1011 (11 in decimal)
* The numbers in descending order are 11, 7.
* The sorted indices are `[1, 0]`.
