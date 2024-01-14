
# Adding string numbers

This function takes two numbers in string format as parameters, adds them, and returns the result as a string.

```
function:
add_string_numbers(sn1, sn2)

sn1 and sn2:
numbers in string form
```

If either `sn1` or `sn2` is not a valid numeric string, a ValueError is caught, and an error message is printed.
Below examples demonstrate various scenarios, including integers and decimal numbers as input.

```
add_string_numbers("10", "20")
output: "30"

add_string_numbers("11.34", "9")
output: "20.34"

add_string_numbers("5", "4.99")
output: "9.99"

add_string_numbers("3.4", "6.6")
output: "10.0"

add_string_numbers("4", "6")
output: "10"

add_string_numbers("three", "4")
output: ValueError: sn1='three' is not a valid numeric string

add_string_numbers("3", "four")
ValueError: sn2='four' is not a valid numeric string

```

