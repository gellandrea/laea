def is_32bit_integer(n):
    if isinstance(n, int):
        if n < 0:
            return False
        elif n > 2**32 - 1:
            return False
        else:
            return True
    else:
        return False
