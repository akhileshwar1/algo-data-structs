# uses python3
def opt_gcd(a, b):
    if(b == 0):
        return a
    return opt_gcd(b, a % b)


a, b = map(int, input().split())

print(opt_gcd(a, b))
