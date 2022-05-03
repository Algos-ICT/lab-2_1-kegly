fin = open('input.txt', 'r')
n = fin.readline()
x = list(map(int, fin.readline().split()))
fin.close()
fout = open('output.txt', 'w')
flag = 1

if sum(x) % 3 == 0:
  tmp = sum(x) / 3
  x.sort()
  x.reverse()
  for i in range(3):
    y = []
    j = 0
    while (sum(y) != tmp and j<len(x)):
      if ((sum(y) + x[j]) <= tmp):
        y.append(x[j])
        del(x[j])
      else:
        j += 1
    if sum(y) == tmp:
      pass
      #print(y)
    else:
      flag  = 0
      break
else:
  flag = 0


if flag:
  fout.write('1')
else:
  fout.write('0')
