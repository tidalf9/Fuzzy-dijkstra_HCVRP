
# 模糊Dijkstra算法解决单源最短路径问题

## 使用方法

### 数据
在文件路径下的txt文件中，也可以自定义输入数据。

### 实验过程
命令行使用如下代码进行输入为110个节点的dijkstra最短路径规划，输出结果打印成图,121个节点同理。
```bash
python dijkstra.py D:\python\F2018-HW2-master\P1\input1.txt 1 110
```
使用如下代码进行输入为10个节点的学校地图环境下的dijkstra最短路径规划，输出结果打印成图。
```bash
python fixed_dijkstra.py graph.txt positions.txt
```
使用如下代码进行输入为10个节点的学校地图环境下的模糊dijkstra的最短路径规划，输出结果打印成图。
```bash
python fuzzy_dijkstra.py graph1.txt positions1.txt
```



