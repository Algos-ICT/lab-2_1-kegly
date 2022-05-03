fin = open('input.txt')
n = int(fin.readline())
sum = 0
list_num = []
for i in range(1, n+1):
    if sum + i <= n:
        sum += i
        list_num.append(i)
    else:
        list_num[-1] += (n-sum)
        break


fout = open('output.txt', 'r')
fout.write(len(list_num))
fout.write(*list_num)


