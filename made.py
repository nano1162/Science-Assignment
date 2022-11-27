import numpy as np 
import matplotlib as mtplt
import matplotlib.pyplot as plt
mtplt.use('Agg')
import math
from celluloid import Camera

# 텍스트 구현

y = float(input('출발지점 Y좌표를 입력해 주세요. : ')) # 높이 입력
g = 9.8 #중력가속도

t = math.sqrt(2*y/g)
timetable = np.linspace(0, t, 100) # 떨어지는데 필요한 시간 계산

def func(time1): # 시간 당 거리 계산
    S = 4.9*(time1**2)
    return S

fig, axes = plt.subplots(1)
plt.ylabel('Height')

camera = Camera(fig)

a = []

for i in range(len(timetable)): # 시간 당 높이 계산
    a.append(y - func(timetable[i]))
    # print('높이 :', a[i]) # 시간 당 높이 표시
    axes.plot(1, a[i], 'o', markersize = 20, color = 'r')
    plt.xlabel('Time = %1fs' %timetable[i])
    camera.snap()

animation = camera.animate(interval=50)

animation.save( 'sines.gif', writer = 'ffmpef', fps = 60)