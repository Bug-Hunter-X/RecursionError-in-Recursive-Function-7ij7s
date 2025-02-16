def function_with_uncommon_error(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return function_with_uncommon_error(n-1) + function_with_uncommon_error(n-2)

# This will cause RecursionError for larger values of n
result = function_with_uncommon_error(35)