list1 = [4,5,12,-2,8,9]
answerList= []
count = 0
for i in range(0,5):
    for j in range(1,6):
        if i == j :
            continue
        elif list1[i]+list1[j] == 10 and count == 0:
            count += 1
            answerList.append((list1[i], list1[j]))
            break

print(answerList)