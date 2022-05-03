def getCardWeight(card):
    arr = ["6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    return arr.index(card)


inp = open("input.txt")

myCount, enemyCount, trump = inp.readline().split()
myCount = int(myCount)
enemyCount = int(enemyCount)
myCards = inp.readline().split()
enemyCards = inp.readline().split()

myColorCards = {"S": [], "C": [], "D": [], "H": []}
enemyColorCards = {"S": [], "C": [], "D": [], "H": []}

for card in myCards:
    myColorCards[card[1]].append(card[0])
for card in enemyCards:
    enemyColorCards[card[1]].append(card[0])

cardColors = ["S", "C", "D", "H"]
for color in cardColors:
    myColorCards[color] = sorted(myColorCards[color], key=lambda x: getCardWeight(x))
    enemyColorCards[color] = sorted(enemyColorCards[color], key=lambda x: getCardWeight(x), reverse=True)
cardColors.remove(trump)


def CanWin():
    for enemyCard in enemyColorCards[trump]:
        isBreaked = False
        for myCard in myColorCards[trump]:
            if (getCardWeight(myCard) > getCardWeight(enemyCard)):
                myColorCards[trump].remove(myCard)
                isBreaked = True
                break
        if (isBreaked == False):
            return False

    for color in cardColors:
        for enemyCard in enemyColorCards[color]:
            isBreaked = False
            for myCard in myColorCards[color]:
                if (getCardWeight(myCard) > getCardWeight(enemyCard)):
                    myColorCards[color].remove(myCard)
                    isBreaked = True
                    break
            if (isBreaked == False):
                for myTrump in myColorCards[trump]:
                    isBreaked = True
                    myColorCards[trump].remove(myTrump)
                    break
                if (isBreaked == False):
                    return False
    return True


result = CanWin()

out = open("output.txt", "w")
if (result):
    out.write("YES")
else:
    out.write("NO")
out.close()
