inp = open("input.txt")
n = int(inp.readline())
seq = list(map(int, inp.readline().split()))
need = sum(seq)
if(need % 2 == 1):
    out = open("output.txt", "w")
    out.write("-1")
    out.close()
    exit()

need = need // 2
taked = 0
i = 0
while((i < len(seq)) and (taked < need)):
    taked += seq[i]
    i += 1

if(taked == need):
    res = ""
    takedSecondHalf = 0
    takedSecondCount = 0    
    for index in range(i, len(seq)):
        takedSecondHalf += seq[index]
        takedSecondCount += 1
        res += f"{seq[index]} "
    if (takedSecondHalf == taked == need):
        out = open("output.txt", "w")
        out.write(f"{takedSecondCount} \n")
        out.write(res)
        out.close()
        exit()

out = open("output.txt", "w")
out.write("-1")
out.close()
        

