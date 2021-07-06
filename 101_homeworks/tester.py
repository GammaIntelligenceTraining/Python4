def first(chislo):
    result = chislo ** 2
    print(result)
    return first(result)

print(first(10))