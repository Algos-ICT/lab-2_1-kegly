def first(a: str, b: str):
    if len(a) == len(b):
        return max(a, b)

    else:
        mini = min(a, b)
        maxi = max(a, b)
        if maxi[:len(mini)] == mini and mini > maxi[len(mini):]:
            return mini
        else:
            return maxi


def main(numbers: list):
    answer = ''
    while numbers:
        mx = '0'
        for number in numbers:
            mx = first(number, mx)

        answer += mx
        numbers.remove(mx)

    return answer


fin = open('input.txt')
n = fin.readline()
numbers = [i for i in fin.readline().split()]
fout = open('output.txt', 'w')

fout.write(main(numbers))

