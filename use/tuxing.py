import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

if __name__ == '__main__':

    # 创建三维坐标系
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    # 定义函数
    def f(x, y):
        return x**2 + y**2

    # 生成数据
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)

    # 绘制三维图形
    ax.plot_surface(X, Y, Z)

    # 显示图形
    plt.show()
