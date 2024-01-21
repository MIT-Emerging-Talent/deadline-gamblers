# Randomize Array  
The randomize_array function reorders the elements of an input array into a random sequence.

## Examples
Here's how you can use this function:

```python

# Create an array
original_array = [1, 2, 3, 4, 5]

# Call the function with the array
randomized_array = randomize_array(original_array)

# Print the original and randomized arrays
print("Original array: ", original_array) # output :  Original array:  [1, 2, 3, 4, 5]
print("Randomized array: ", randomized_array) # output :  Randomized array:  [3, 4, 5, 1, 2]


```


## Approach

The randomize_array function works by creating a copy of the original array and then shuffling the elements of the copied array in place. This is done using the shuffle function from Python's built-in random module. The shuffle function randomly rearranges the elements of the list it's called on.



## Unittest results
test command:
```
randomize_array % python3 -m unittest discover -v

```
results:
```

test_randomize_array (tests.test_randomize_array.TestRandomizeArray.test_randomize_array) ... ok
test_randomize_array_empty (tests.test_randomize_array.TestRandomizeArray.test_randomize_array_empty) ... ok
test_randomize_array_single (tests.test_randomize_array.TestRandomizeArray.test_randomize_array_single) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```


## Author

Abed Hamami





