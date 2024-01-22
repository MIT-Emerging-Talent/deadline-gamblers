# Array Product

This function takes an array as input and returns a new array of the same length where each element represents the product of all elements in the original array except the one at the corresponding index.

```python
# function: 
array_product(arr)

# arr: an array of any size
```

It creates an empty list first and iterates over the original array and makes a copy of array except the one at the corresponding index. Then it calculates the product of all elements in the copied array and appends it to the new array.

```python
array_product([1, 2, 3, 4, 5, 6, 7])
output: [5040, 2520, 1680, 1260, 1008, 840, 720]

array_product([1, 2, 3, 4, 5, 6, 0])
output: [0, 0, 0, 0, 0, 0, 720]

array_product([0, 2, 3, 4, 5, 6, 7])
output: [5040, 0, 0, 0, 0, 0, 0]

array_product([])
output: []

array_product([1])
output: [1]

array_product([0])
output: [0]

```

## Test the Code Implementation
Run the following command in the `array_product` directory.

```pash
python -m unittest discover -v
```
