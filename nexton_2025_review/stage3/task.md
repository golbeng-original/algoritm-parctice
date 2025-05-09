# Team Formation

## Problem Description

Given a list of employees where each is assigned a numeric evaluation score, use the selection process below to find the sum of scores of selected employees.

### Selection Process

1. The employee with the highest score among the first `k` employees or the last `k` employees in the score list is selected.
2. The selected employee is removed from the score list.
3. The process continues to select the next employee until the `team_size` is achieved.

### Special Rules

* If multiple employees have the same highest score, the employee with the lowest index is selected.
* If there are fewer than `k` employees, the entire list is available for selection.

### Example

#### Input

```
score = [10, 20, 10, 15, 5, 30, 20]
teamSize = 2
k = 3
```

#### Step-by-step Execution

1. For the first selection, choose from the first 3 elements: `[10, 20, 10]` or the last 3 elements: `[5, 30, 20]`.

   * Score 30 is selected and removed. The list becomes `[10, 20, 10, 15, 5, 20]`.
2. For the second selection, choose from `[10, 20, 10]` or `[15, 5, 20]`.

   * Score 20 is selected, and the list becomes `[10, 10, 15, 5, 20]`.
3. The sum of the selected scores is `30 + 20 = 50`.

### Constraints

* `1 ≤ n ≤ 10^5` (Number of employees)
* `1 ≤ score[i] ≤ 10^9` (Score of each employee)
* `1 ≤ team_size ≤ n`
* `1 ≤ k ≤ n`

## Function Description

Complete the function `teamFormation` with the following parameters:

```python
teamFormation(score: List[int], team_size: int, k: int) -> int
```

* `score`: An array of scores for each employee.
* `team_size`: The number of team members required.
* `k`: The size of the array segments to select from.

### Returns

* An integer representing the sum of the scores of all members selected for the team.

## Sample Case

### Input

```
9
17 12 10 2 7 2 11 20 8
3
4
```

### Output

```
49
```

### Explanation

1. The first selection chooses from `[17, 12, 10, 2]` or `[11, 20, 8]`, and picks 20. The list becomes `[17, 12, 10, 2, 7, 2, 11, 8]`.
2. The second selection chooses from `[17, 12, 10, 2]` or `[7, 2, 11, 8]`, and picks 17. The list becomes `[12, 10, 2, 7, 2, 11, 8]`.
3. The third selection chooses from `[12, 10, 2, 7]` or `[7, 2, 11, 8]`, and picks 12. The list becomes `[10, 2, 7, 2, 11, 8]`.
4. The total sum of selected scores is `20 + 17 + 12 = 49`.
