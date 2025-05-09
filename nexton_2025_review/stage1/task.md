# Flipping Switches

## Problem Description

There is a row of two-position switches numbered consecutively starting from 1, all initially in the "Off" position. A series of operations is performed, where each operation specifies a left and right index. For each operation, all switches in the inclusive range between these indices undergo a NOT operation (Off becomes On, On becomes Off).

### Given

* A series of operations, each defined as `[start, end]`.
* Each operation causes a NOT operation on all switches between the given indices.
* The switches are indexed starting from 1.
* Initially, all switches are in the "Off" position.

### Task

Given a series of operations, determine their final state. Calculate the sum of all indices where a switch is on. Use 1-based index values.

### Example

#### Input

```
operations = [[1, 4], [2, 6], [1, 6]]
```

#### Step-by-step Execution

1. Initial State: `-------` (All switches are off)
2. After first operation `[1, 4]`: `XXXX---`
3. After second operation `[2, 6]`: `X---XX-`
4. After third operation `[1, 6]`: `-XXX---`

#### Result

* The switches that are "On" are at indices 2, 3, and 4.
* Sum of indices: `2 + 3 + 4 = 9`.

## Constraints

* `1 ≤ q ≤ 10^5` (Number of operations)
* `1 ≤ operations[i][0] ≤ operations[i][1] ≤ 10^5`

## Function Description

Complete the function `finalState` with the following parameter:

```python
finalState(operations: List[List[int]]) -> int
```

* `operations`: A list of lists, where each sublist represents an inclusive range `[start, end]` of switches to flip.

### Returns

* An integer representing the sum of the indices of the switches that are "On" after all operations.

## Sample Case

### Input

```
3
3 4
2 3
2 2
```

### Output

```
4
```

### Explanation

1. Initial State: `-------`
2. After operation `[3, 4]`: `--XX---`
3. After operation `[2, 3]`: `-X-X---`
4. After operation `[2, 2]`: `---X---`

The switch that is "On" is at index 4, so the result is 4.
