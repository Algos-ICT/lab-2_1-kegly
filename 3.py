inp = open("input.txt")
n = int(inp.readline())
a = list(map(int, inp.readline().split()))
b = list(map(int, inp.readline().split()))
inp.close()

a = list(sorted(a))
b = list(sorted(b))

summ = 0
for i in range(n):
    summ += a[i] * b[i]

out = open("output.txt", "w")
out.write(str(summ))
out.close()