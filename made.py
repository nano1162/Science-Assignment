import numpy as np 
import matplotlib.pyplot as plt
import math
import matplotlib.animation as animation

# 텍스트 구현

print('나는 구현할 수 있습니다. ') # 의지 표명
y = float(input('출발지점 Y좌표를 입력해 주세요. : ')) # 높이 입력
g = 9.8 #중력가속도

print('최초 높이:', y) # 최초 높이 표시

t = math.sqrt(2*y/g)
timetable = np.linspace(0, t, 100) # 떨어지는데 필요한 시간 계산

def func(time1): # 시간 당 거리 계산
    S = 4.9*(time1**2)
    return S

a = []
for i in range(len(timetable)): # 시간 당 높이 계산
    a.append(y - func(timetable[i]))
    print('높이 :', a[i]) # 시간 당 높이 표시

print('걸린 시간 :', t, '초') # 걸린 시간

# 애니메이션 만들기

plt.plot(timetable, a)
plt.show()