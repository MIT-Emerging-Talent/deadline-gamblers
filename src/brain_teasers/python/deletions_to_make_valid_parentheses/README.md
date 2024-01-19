# Make parentheses valid 
This module provides a function to calculate the minimum number of deletions required to balance parentheses in a given input string.

## Examples
Here's an example of how to use the deletions_to_make_valid_parentheses function:


```python
# Call the function with a string containing unbalanced parentheses
result = deletions_to_make_valid_parentheses("()(())")
print(result) # Outputs: 0

# Call the function with a string containing unbalanced parentheses
result = deletions_to_make_valid_parentheses("(()))")
print(result) # Outputs: 1

# Call the function with a string containing unbalanced parentheses
result = deletions_to_make_valid_parentheses("()())())")
print(result) # Outputs: 2

```


## Approach

The approach used to solve this problem involves using a stack data structure. For each character in the input string, if it's an opening parenthesis, it's pushed onto the stack. If it's a closing parenthesis, the function checks if the stack is empty. If it is, it means there's no matching opening parenthesis for this closing parenthesis, so a deletion is needed. If the stack is not empty, it pops the top element from the stack, effectively balancing the parentheses. After going through all the characters in the string, any remaining elements in the stack represent unbalanced opening parentheses, so the number of such elements is added to the total count of deletions.




## Unittest results
test command:
```
deletions_to_make_valid_parentheses % python3 -m unittest discover -v
```
results:
```

test_1 (tests.test_deletions_to_make_valid_parentheses.TestDeletionsToMakeValidParentheses.test_1) ... ok
test_2 (tests.test_deletions_to_make_valid_parentheses.TestDeletionsToMakeValidParentheses.test_2) ... ok
test_3 (tests.test_deletions_to_make_valid_parentheses.TestDeletionsToMakeValidParentheses.test_3) ... ok
test_4 (tests.test_deletions_to_make_valid_parentheses.TestDeletionsToMakeValidParentheses.test_4) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```


## Author

Abed Hamami