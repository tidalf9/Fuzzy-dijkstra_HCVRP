
# 异质车队的三车辆问题

基于注意力机制的模型，用于学习解决具有最小化最大值和最小化总和目标的异质容量车辆路径问题（HCVRP）。使用 REINFORCE 与贪婪回滚基线进行训练。

## 使用方法

### 生成数据

训练数据是动态生成的。要生成测试数据（与论文中使用的数据相同），用于 3 辆车和 40 个客户：
```bash
python generate_data.py --veh_num 3 --graph_size 40
```

### 训练

对于具有 40 个节点和最小化最大值目标的 HCVRP 实例，并使用rollout 作为 REINFORCE 基线进行训练：
```bash
python run.py --graph_size 40 --baseline rollout --run_name 'hcvrp40_rollout' --obj min-max
```
对于具有 40 个节点和最小化总和目标的 HCVRP 实例，并使用rollout 作为 REINFORCE 基线进行训练：
```bash
python run.py --graph_size 40 --baseline rollout --run_name 'hcvrp40_rollout' --obj min-sum
```

#### 多GPU
默认情况下，训练将在*所有可用的GPU*上进行。要完全禁用CUDA，请添加标志`--no_cuda`。设置环境变量`CUDA_VISIBLE_DEVICES`以仅使用特定GPU：
```bash
CUDA_VISIBLE_DEVICES=2,3 python run.py 
```
对于小问题规模（最多50个节点），使用多个GPU的效率有限。

#### 初始化运行
您可以使用`--load_path`选项通过预训练模型初始化运行：
```bash
python run.py --graph_size 40 --load_path outputs/hcvrp40_rollout/hcvrp40_rollout_{datetime}/epoch-49.pt
```

`--load_path`选项也可用于加载较早的运行，在这种情况下，还将加载优化器状态：
```bash
python run.py --graph_size 40 --load_path outputs/hcvrp40_rollout/hcvrp40_rollout_{datetime}/epoch-{num}.pt
```

### 评估
要评估模型，可以在`run.py`中添加`--eval-only`标志，或者使用`eval.py`，它还将测量时间并保存结果：
```bash
python eval.py data/hcvrp/hcvrp_40_seed24610.pkl --model outputs/hcvrp40_rollout/hcvrp40_rollout_{datetime}/epoch-{num}.pt --decode_strategy greedy
```
如果未指定epoch，默认使用文件夹中的最后一个模型文件。

