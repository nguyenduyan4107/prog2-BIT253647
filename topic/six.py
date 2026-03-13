s = input()

numbers = list(map(int,s.split(";")))

even = 0
negative = 0
prime = 0

def is_prime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

for x in numbers:
    print(x)

    if x%2==0:
        even+=1

    if x<0:
        negative+=1

    if is_prime(x):
        prime+=1

avg = sum(numbers)/len(numbers)

print(even)
print(negative)
print(prime)
print(avg)
