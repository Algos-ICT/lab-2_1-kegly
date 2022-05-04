def canDivision(coins, n, first, second, third, backs):
    if (first == 0) and (second == 0) and (third == 0):
        if (n < 0):
            return True
        else:
            return False

    if (n < 0):
        return False

    way = (first, second, third, n)
    if (way not in backs):
        inFirst = False
        inSecond = False
        inThird = False

        if (first - coins[n] >= 0):
            inFirst = canDivision(coins, n - 1, first - coins[n], second, third, backs)
        if (inFirst == False) and (second - coins[n] >= 0):
            inSecond = canDivision(coins, n - 1, first, second - coins[n], third, backs)
        if (inFirst == False) and (inSecond == False) and (third - coins[n] >= 0):
            inThird = canDivision(coins, n - 1, first, second, third - coins[n], backs)

        backs[way] = inFirst or inSecond or inThird

    return backs[way]


inp = open("input.txt")

n = int(inp.readline())
coins = list(map(int, inp.readline().split()))

summ = sum(coins)
if (summ % 3 != 0) or (n < 3):
    out = open("output.txt", "w")
    out.write("0")
    out.close()
    exit

need = summ / 3

backs = {}

res = canDivision(coins, n - 1, need, need, need, backs)

out = open("output.txt", "w")
if (res):
    out.write("1")
else:
    out.write("0")
out.close()
