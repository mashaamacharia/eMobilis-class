from numpy.array_api import trunc

scores=[90,70,60,77,40,30,10,0]
print(scores[2])

#add
scores.append(61)
print(scores)

#remove
scores.pop(3)
print(scores)

scores.sort(reverse=True)