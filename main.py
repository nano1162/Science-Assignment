import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math
import matplotlib.animation as animation

#함수 정의
def func(theta, t, b, g, l, m):
    theta1 = theta[0]
    theta2 = theta[1]

    dtheta1_dt = theta2

    dtheta2_dt = -(b/m)*theta2-(g/l)*math.sin(theta1)

    dtheta_dt = [dtheta1_dt, dtheta2_dt]

    return dtheta_dt

