def multiply_10(n):
    """Multiply by 10 , add to cache, return cached result."""
    cache[n] = n * 10
    return cache[n]


def memo_multiply_10(n):
    """Check if n was calculated before, return cached version or make calculation."""
    if n in cache:
        print("Found in cache!:", cache)
        return cache[n]
    print("Not in cache...:", cache)
    return multiply_10(n)


cache = {}


print(memo_multiply_10(9))
print(memo_multiply_10(9))
