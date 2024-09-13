import torch

def check_cuda_devices():
    print("Checking CUDA availability...")
    # 检查CUDA是否可用
    if torch.cuda.is_available():
        print("CUDA is available")
        # 获取并显示所有可用的CUDA设备
        num_devices = torch.cuda.device_count()
        print(f"Number of CUDA devices: {num_devices}")
        for i in range(num_devices):
            print(f"Device {i}: {torch.cuda.get_device_name(i)}")
            # 打印当前选定的CUDA设备
            if i == torch.cuda.current_device():
                print(f"Current CUDA device: {torch.cuda.get_device_name(i)}")
    else:
        print("CUDA is not available. Please check your system configuration.")

# 调用函数
check_cuda_devices()
