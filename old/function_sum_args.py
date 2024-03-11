def sum(*args):
    result = 0
    for value in args:
        try:
            result += float(value)
        except ValueError:
            continue
    return result

print(sum(1,2,3,4," ", 6, "fdfffff"))