def function_with_uncommon_error_fixed(a, b):
    if a == 0 and b == 0:
        raise ZeroDivisionError("Both inputs cannot be zero.")
    elif a == 0:
        return b
    elif b == 0:
        return a
    else:
        return a / b

result = function_with_uncommon_error_fixed(0, 0) 
# This will now raise a ZeroDivisionError
#print(result)  # Uncomment to see the error

result = function_with_uncommon_error_fixed(1, 0)
print(result) 

result = function_with_uncommon_error_fixed(0, 1)
print(result) 

result = function_with_uncommon_error_fixed(10, 2)
print(result) 