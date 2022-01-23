# uses python3
def naive_gcd(a, b):
    best = 0
    for i in range(1, a+b):
        if(a % i == 0 and b % i == 0):
            best = i
    return best


a, b = map(int, input().split())
print(naive_gcd(a, b))
