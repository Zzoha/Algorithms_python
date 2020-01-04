def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# 1. 7 * 6! // 5040
# 2. 6 * 5! // 720
# 3. 5 * 4! // 120
# 4. 4 * 3! // 24
# 5. 3 * 2! // 6
# 6. 2 * 1! // 2
# 7. 1 * 0! // 1
# 8. 0! 1
# stek vizovov pochitat'!!!!


print(factorial(7))