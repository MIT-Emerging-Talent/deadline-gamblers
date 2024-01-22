# Array Product

This function takes an array as input and returns a new array of the same length where each element represents the product of all elements in the original array except the one at the corresponding index.

```
# function: 
product_of_array_except_self(arr)

# arr: an array of any size
```

It creates an empty list first and iterates over the original array and makes a copy of array except the one at the corresponding index. Then it calculates the product of all elements in the copied array and appends it to the new array.

```
product_of_array_except_self([1, 2, 3, 4, 5, 6, 7])
output: [5040, 2520, 1680, 1260, 1008, 840, 720]

product_of_array_except_self([1, 2, 3, 4, 5, 6, 0])
output: [0, 0, 0, 0, 0, 0, 720]

product_of_array_except_self([0, 2, 3, 4, 5, 6, 7])
output: [5040, 0, 0, 0, 0, 0, 0]

product_of_array_except_self([])
output: []

product_of_array_except_self([1])
output: [1]

product_of_array_except_self([0])
output: [0]

```
