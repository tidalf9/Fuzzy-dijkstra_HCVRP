import pandas as pd
import numpy as np
import os


def pkl_to_excel(pkl_file_path, output_dir):
    # 读取 .pkl 文件
    data = pd.read_pickle(pkl_file_path)

    # 打印数据类型和示例数据
    print(f"Data type: {type(data)}")

    if isinstance(data, tuple):
        # 如果顶层是一个元组，检查其内容
        if isinstance(data[0], list) and all(isinstance(i, tuple) for i in data[0]):
            rows = []
            for item in data[0]:
                rows.append({
                    "float_value": item[0],
                    "int_list": item[1],
                    "array_data": item[2].tolist(),  # 转换为列表
                    "another_float": item[3]
                })
            df = pd.DataFrame(rows)
        else:
            raise ValueError("Unsupported tuple structure")
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
pkl_file_path = r''
output_dir = r'D:\python\HCVRP_DRL-main\data'

# 调用函数进行转换
pkl_to_excel(pkl_file_path, output_dir)
