import pandas as pd
import numpy as np
import os


def pkl_to_excel(pkl_file_path, output_dir):
    # 读取 .pkl 文件
    data = pd.read_pickle(pkl_file_path)

    # 检查数据类型并处理
    if isinstance(data, pd.DataFrame):
        df = data
    elif isinstance(data, np.ndarray):
        # 假设 ndarray 是二维的，可以直接转换为 DataFrame
        df = pd.DataFrame(data)
    else:
        raise ValueError("Unsupported data type in pkl file")

    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)

    # 生成 Excel 文件路径
    base_name = os.path.basename(pkl_file_path)
    excel_file_name = os.path.splitext(base_name)[0] + '.xlsx'
    excel_file_path = os.path.join(output_dir, excel_file_name)

    # 将 DataFrame 写入 Excel 文件
    df.to_excel(excel_file_path, index=False)
    print(f"Excel file saved to {excel_file_path}")


# 输入和输出路径
pkl_file_path = r'D:\python\HCVRP_DRL-main\fleet_v5\data\hcvrp\hcvrp_v5_100_seed24610.pkl'
output_dir = r'D:\python\HCVRP_DRL-main\data'

# 调用函数进行转换
pkl_to_excel(pkl_file_path, output_dir)
