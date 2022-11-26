import numpy as np 
import matplotlib.pyplot as plt
import math
import matplotlib.animation as animation

print('나는 구현할 수 있습니다. ')
y = float(input('출발지점 Y좌표를 입력해 주세요. : ')) #높이 입력

v = 0

print('최초 높이:', y)

t = np.linspace(0, 10, 100)

S = 1/2*9.8*(time**2)

timetable = []
for i in range(len(t)):
    timetable.append(func(t[i]))

print(timetable)

for i in range(len(timetable)):
    y = y - timetable[i]
    print('높이 :', y)



''' 
plt.figure()
plt.plot(x,y, 'b-', label = '1st')
plt.ylabel('Y')
plt.xlabel('X')
plt.legend(loc='best')
plt.show() 
'''