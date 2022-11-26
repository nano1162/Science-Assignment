import numpy as np 
import matplotlib.pyplot as plt
import math
import matplotlib.animation as animation

print('(100, 100)까지 구현할 수 있습니다. ')
x = int(input('출발지점 X좌표를 입력해 주세요. : '))
y = int(input('출발지점 Y좌표를 입력해 주세요. : '))


t = np.linspace(0, 10, 100)

plt.figure()
plt.plot(x,y, 'b-', label = '1st')
plt.ylabel('Y')
plt.xlabel('X')
plt.legend(loc='best')
plt.show()