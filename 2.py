inp = open('input.txt')
need = int(inp.readline())
tank = int(inp.readline())
n = int(inp.readline())
stations = list(map(int, inp.readline().split()))
inp.close()

def getFillsCount(need, tank, stations):
    stations.append(need)
    curr = 0
    count = 0
    for i in range(len(stations) - 1):
        if (stations[i] - curr > tank):
            return -1
        if (stations[i + 1] - curr) > tank:
            curr = stations[i]
            count += 1
    if (stations[len(stations) - 1] - curr < tank):
        return count
    else:
        return -1


count = getFillsCount(need, tank, stations)
out = open('output.txt', 'w')
out.write(str(count))
print(str(count))
out.close()