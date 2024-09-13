import pickle

# 指定pkl文件的路径
file_path = r'D:\python\HCVRP_DRL-main\fleet_v3\results\hcvrp\hcvrp_40_seed24610\hcvrp_40_seed24610-minmax_40_lr0.995_grad3.0_20200725T113544_epoch-45-greedy-t1-0-1280.pkl'

# 打开并读取pkl文件
with open(file_path, 'rb') as file:
    data = pickle.load(file)

# 打印读取的数据
print(data)
