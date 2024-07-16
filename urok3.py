import matplotlib.pyplot as plt
f = open('dz.csv')
lines = 0
massive = []
for i in f:
    lines += 1
    if lines == 1:
        continue
    row = i.split(';')
    CTR = row[2].replace('\n', "")
    CTR = CTR.replace(',' ,".")
    CTR = float(CTR)
    massive.append(CTR)
plt.plot(massive)
plt.show()