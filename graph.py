# - *- coding: utf- 8 - *- 
import matplotlib.pyplot as plt
import numpy as np

x = np.array([])
y = np.array([])

f = open('part-00000','r')
lineNum = int(0)
total = len(f.readlines())
f.close()
f = open('part-00000','r')

for line in f:
    lineNum +=1
    if lineNum > total-50: #n-k
        line = line.strip('\n')
        word, count = line.split('\t')
        x = np.append(x, word)
        y = np.append(y, int(count))


print(x,'\n',y)


plt.bar(x,y)
plt.xlabel('Words')
plt.ylabel('Count')
plt.title('Top 50 most popular words')
plt.show()
