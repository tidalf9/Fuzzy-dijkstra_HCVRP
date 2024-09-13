import matplotlib.pyplot as plt
import numpy as np

# 输入数据
input_data = {
    'loc': [
        [0.8469, 0.6611],
        [0.6045, 0.3756],
        [0.4612, 0.3142],
        [0.5887, 0.9087],
        [0.6058, 0.8602],
        [0.1023, 0.9078],
        [0.0017, 0.8972],
        [0.4198, 0.2823],
        [0.6407, 0.3343],
        [0.4990, 0.2311],
        [0.3780, 0.8617],
        [0.1205, 0.0665],
        [0.1549, 0.8699],
        [0.7916, 0.9641],
        [0.9036, 0.9321],
        [0.3109, 0.5334],
        [0.0877, 0.1530],
        [0.0535, 0.1430],
        [0.2007, 0.5126],
        [0.6719, 0.1247],
        [0.8667, 0.6718],
        [0.3959, 0.5674],
        [0.8396, 0.7350],
        [0.9611, 0.9731],
        [0.1319, 0.7486],
        [0.1615, 0.7985],
        [0.3097, 0.9314],
        [0.6317, 0.9146],
        [0.0358, 0.0807],
        [0.1599, 0.1711],
        [0.8329, 0.0855],
        [0.4888, 0.5672],
        [0.4051, 0.8034],
        [0.9050, 0.8916],
        [0.3403, 0.5282],
        [0.0431, 0.0861],
        [0.5633, 0.7494],
        [0.1985, 0.7454],
        [0.7084, 0.6467],
        [0.0872, 0.7648]
    ]
}

tour = [25, 39, 7, 26, 0, 38, 13, 6, 27, 11, 0, 33, 4, 5, 37, 0, 28, 14, 24, 15, 34, 1, 0, 39, 23, 21, 31, 20, 0, 17, 18, 29, 36, 12, 30, 0, 2, 9, 0, 3, 10, 0, 19, 16, 35, 0, 8, 0, 32, 22, 0]
veh = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2]

# 将loc数据转换为numpy数组
loc = np.array(input_data['loc'])

# 创建图形
plt.figure(figsize=(10, 10))

# 绘制节点
for i, (x, y) in enumerate(loc):
    plt.scatter(x, y, c='blue', s=50)
    plt.text(x, y, str(i), fontsize=12, ha='right')

# 绘制路径
colors = ['red', 'green', 'blue']  # 为不同的车辆设置不同的颜色
capacities = {0: 20, 1: 25, 2: 30}
for i in range(len(tour) - 1):
    start = tour[i]
    end = tour[i + 1]
    if start < len(loc) and end < len(loc):
        plt.plot([loc[start][0], loc[end][0]], [loc[start][1], loc[end][1]], color=colors[veh[i]])

# 标注起点
plt.scatter(loc[0][0], loc[0][1], c='black', s=100, label='Depot')

# 添加车辆编号和容量注释
vehicle_info = "\n".join([f"Vehicle {i} (Capacity {capacities[i]}): {colors[i]}" for i in capacities])
plt.text(0.01, 0.99, vehicle_info, transform=plt.gca().transAxes, fontsize=12, verticalalignment='top', bbox=dict(facecolor='white', alpha=0.5))

plt.title('Vehicle Routing Problem Solution')
plt.xlabel('X coordinate')
plt.ylabel('Y coordinate')
plt.legend()
plt.grid(True)
plt.show()
