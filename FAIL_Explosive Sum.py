def exp_sum(n):
    if n > 1:
        exp_sum(n - 1)
    if n == 1:
        return 1

k=0
print(exp_sum(2))
