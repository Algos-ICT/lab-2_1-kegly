
in_file = open('input.txt')
n, max_weight = in_file.readline().split()
n, max_weight = int(n), int(max_weight)
things = []
for i in range(int(n)):
    line = in_file.readline().split()
    price = int(line[0])
    weight = int(line[1])
    things.append((price, weight, price / weight))
in_file.close()

things.sort(key=lambda x: x[2], reverse=True)
taked = 0

ans = ""
for i in things:
    new_weight = max_weight - i[1]
    if (new_weight >= 0):
        taked += i[0]
        max_weight -= i[1]
    else:
        taked += i[0] * (max_weight / i[1])
        max_weight = 0

    if (max_weight == 0):
        ans = f"{taked:.4f}"

out = open('output.txt', 'w')
out.write(ans)
print(ans)
out.close()

