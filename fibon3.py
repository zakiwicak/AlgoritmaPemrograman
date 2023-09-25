def R(n):
    if n==1:
        return -7
    else:
        return R(n-1)+12

print(R(3))