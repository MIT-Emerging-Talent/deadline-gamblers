from decimal import Decimal
def add_string_numbers(sn1, sn2):
    """
    Adds two numbers in string format and returns the result as a string.

    Parameters:
    - sn1 (str): First number in string format.
    - sn2 (str): Second number in string format.

    Returns:
    str: The sum of sn1 and sn2 as a string.
    """

    try:    
        n1 = Decimal(sn1) if '.' in sn1 else int(sn1)
    except ValueError:
        raise ValueError(f'{sn1=} is not a valid numeric string')
    
    try:
        n2 = Decimal(sn2) if '.' in sn2 else int(sn2)
    except ValueError:
        raise ValueError(f'{sn2=} is not a valid numeric string')
    
    return str(n1+n2)

# checks
# print(add_string_numbers("10", "20") == "30")
# print(add_string_numbers("11.34", "9") == "20.34")
# print(add_string_numbers("5", "4.99") == "9.99")
# print(add_string_numbers("3.4", "6.6") == "10.0")
# print(add_string_numbers("4", "6") == "10")