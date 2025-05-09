# Modified Knapsack Problem

## Problem Description

The Knapsack problem is a well-known problem in the field of computer programming and problem-solving. To make it more interesting, an interviewer uses a modified version of the problem.

Given `n` items, where the weight of the `i`th item is `2^i`, and the cost of the `i`th item is `cost[i]`, find the minimum amount needed to purchase the items such that the combined weight of the purchased items is at least `minWeight`.

### Example

#### Input

```
n = 5
cost = [2, 5, 7, 11, 25]
minWeight = 26
```

#### Explanation

One of the optimal ways to purchase the items is as follows:

* Buy 2 units of the 0th item and 3 units of the 3rd item.
* Total cost = 2 × 2 + 3 × 11 = 37.
* Total weight = (2 × 2^0) + (3 × 2^3) = 26, which is at least `minWeight`.

#### Output

```
37
```

## Function Description

Complete the function `getMinimumCost` in the editor below.

```python
getMinimumCost(cost: List[int], minWeight: int) -> int
```

### Parameters

* `cost`: An array of integers representing the cost of each item.
* `minWeight`: The minimum combined weight of the items.

### Returns

* A long integer representing the minimum amount needed to purchase the items.

## Constraints

* `1 ≤ n ≤ 30`
* `1 ≤ cost[i] ≤ 10^9`
* `1 ≤ minWeight ≤ 10^9`

### Sample Case

#### Input

```
5
4 3 2 1 10
2
```

#### Output

```
1
```

#### Explanation

* Given `n = 5`, `cost = [4, 3, 2, 1, 10]`, `minWeight = 2`.
* It is optimal to buy 1 unit of item 3 which has a weight of 2^3 = 8 units (greater than `minWeight = 2`) and has a cost of 1.
