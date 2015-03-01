numbers = list(range(2,2000000))
for n,_ in enumerate(numbers):
    i = numbers[n]
    if i:
        for j in range(2, int(2000000 / i)):
            numbers[(j-1)*i + n] = 0
numbers = [i for i in numbers if i]
numbers_set = set(numbers)
for i in numbers:
    if sum(int(c) for c in str(i)) in numbers_set and i > 1000000:
        print(i)
