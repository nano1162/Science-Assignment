import numpy as np 
import matplotlib as mtplt
import matplotlib.pyplot as plt
mtplt.use('Agg')
import math
from celluloid import Camera

# 텍스트 구현

y = float(input('출발지점 Y좌표를 입력해 주세요. (단위 : m) : ')) # 높이 입력
x = float(input('출발 속도를 입력해 주세요. (단위 : m/s) : '))
z = float(input('수평 방향 가속도를 입력해 주세요. (단위 : m/s^2) : '))
g = 9.8 #중력가속도

t = math.sqrt(2*y/g)
timetable = np.linspace(0, t, 100) # 떨어지는데 필요한 시간 계산

def func(time1): # 시간 당 연직 거리 계산
    S = 4.9*(time1**2)
    return S

def two(time1): # 시간 당 수평 거리 계산
    S = (x * time1) + ((z/2)*(time1**2))
    return S

fig, axes = plt.subplots(1)

camera = Camera(fig)

a = []
b = []

for i in range(len(timetable)): # 시간 당 높이 계산
    a.append(y - func(timetable[i]))
    b.append(x + two(timetable[i]))
    # print('높이 :', a[i]) # 시간 당 높이 표시
    axes.plot(b[i], a[i], 'o', markersize = 20, color = 'r')
    hello = b[0]

    axes.text( hello ,0,'Time\n%1fs' %timetable[i])
    axes.text(b[i], a[i], '%1fm\nHeight' %a[i])
    axes.text( hello , y / 2 , 'Distance\n%1fm' %b[i])
    camera.snap()

animation = camera.animate(interval=50)

animation.save( 'gravity.gif', writer = 'ffmpef', fps = 20)