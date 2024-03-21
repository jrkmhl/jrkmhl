def isHappy(n: int) -> bool:
    st = set()
    while n not in st:
        st.add(n)
        n = get_squar(n)
        if n == 1:
            return True

    return False


def get_squar(n):
    res = 0
    while n != 0:
        tmp = n % 10
        res = res + tmp ** 2
        n = int(n / 10)

    return res

print(isHappy(1))