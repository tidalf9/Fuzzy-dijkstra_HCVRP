import matplotlib.pyplot as plt
import networkx as nx
import matplotlib as mpl
from matplotlib import font_manager
import sys

# 设置字体路径
font_path = r'C:\Windows\Fonts\msyhl.ttc'
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = [font_manager.FontProperties(fname=font_path).get_name()]

def dijkstra(G, start, end):
    shortest_paths = {vertex: float('infinity') for vertex in G}
    previous_vertices = {vertex: None for vertex in G}
    shortest_paths[start] = 0
    nodes = set(G.nodes())

    while nodes:
        current_node = min(nodes, key=lambda vertex: shortest_paths[vertex])
        nodes.remove(current_node)
        if shortest_paths[current_node] == float('infinity'):
            break
        for neighbor, data in G[current_node].items():
            weight = data['weight']
            alternative_route = shortest_paths[current_node] + weight
            if alternative_route < shortest_paths[neighbor]:
                shortest_paths[neighbor] = alternative_route
                previous_vertices[neighbor] = current_node

    path, current_vertex = [], end
    while previous_vertices[current_vertex] is not None:
        path.insert(0, current_vertex)
        current_vertex = previous_vertices[current_vertex]
    if path:
        path.insert(0, current_vertex)
    return path, shortest_paths[end]

def plot_graph(G, route_taken, pos):
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=700, font_size=10)
    path_edges = list(zip(route_taken[:-1], route_taken[1:]))
    nx.draw_networkx_nodes(G, pos, nodelist=route_taken, node_color='red', node_size=700)
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)
    plt.title("Graph with highlighted shortest path")
    plt.show()

def read_graph_from_file(graph_file):
    with open(graph_file, 'r') as f:
        lines = f.readlines()

        num_edges = int(lines[0].strip())
        start_node = lines[1].strip()
        end_node = lines[2].strip()

        edges = []
        for line in lines[3:3 + num_edges]:
            u, v, weight = line.strip().split()
            edges.append((u, v, float(weight)))

    return edges, start_node, end_node

def read_positions_from_file(position_file):
    positions = {}
    with open(position_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            parts = line.strip().split()
            if len(parts) == 3:
                node, x, y = parts
                try:
                    x = float(x)
                    y = float(y)
                    positions[node] = (x, y)
                except ValueError:
                    print(f"Warning: Skipping line with incorrect format: {line}")
            else:
                print(f"Warning: Skipping line with incorrect format: {line}")

    # 打印出所有读取的位置数据
    print("Positions read from file:")
    for node, pos in positions.items():
        print(f"Node {node}: {pos}")

    return positions

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python fixed_dijkstra.py <graph_file> <position_file>")
        sys.exit(1)

    graph_file = sys.argv[1]
    position_file = sys.argv[2]

    edges, start, end = read_graph_from_file(graph_file)
    positions = read_positions_from_file(position_file)

    G = nx.Graph()
    G.add_weighted_edges_from(edges)

    # 检查所有节点是否有位置信息
    missing_positions = [node for node in G.nodes if node not in positions]
    if missing_positions:
        print(f"Warning: The following nodes have no position data: {missing_positions}")

    shortest_path, total_cost = dijkstra(G, start, end)
    print("Shortest path:", shortest_path)
    print("Total cost to reach end:", total_cost)

    # 检查路径中的所有节点是否有位置信息
    if all(node in positions for node in shortest_path):
        plot_graph(G, shortest_path, positions)
    else:
        print("Error: Not all nodes in the shortest path have position data.")
