def generator():
    yield 1
    yield 'string'
    yield True

gen = generator()

print(next(gen))
print(next(gen))
print(next(gen))

