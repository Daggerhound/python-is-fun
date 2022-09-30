import ctypes

# This is because 5 + 4 loads the constant 9, the sum is done at interpret time
# while int.__add__(5, 4) loads the 

ctypes.c_uint.from_address(id(5) + 24).value = 6
print(int.__add__(5, 4)) # while this prints 10

ctypes.c_uint.from_address(id(5) + 24).value = 6
print(5 + 4)             # this prints 9