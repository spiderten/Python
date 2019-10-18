import matplotlib.pyplot as plt

x = []
y = []

teste = open('C:/Users/thiagodl/Desktop/teste.csv', 'r')

for line in teste:
    line = line.strip()
    X, Y = line.split(',')
    x.append(X)
    y.append(Y)

plt.plot([1,2,3,4], [4,7,8,12])

plt.title('exemple')
plt.xlabel('x label')
plt.ylabel('y label')

plt.show()