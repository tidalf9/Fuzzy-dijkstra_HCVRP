import matplotlib.pyplot as plt
import networkx as nx
import matplotlib as mpl
from matplotlib import font_manager
import sys

# 设置字体路径
font_path = r'C:\Windows\Fonts\msyhl.ttc'
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = [font_manager.FontProperties(fname=font_path).get_name()]

def fuzzy_dijkstra(G, start, end):
    inf = float('inf')
    cost_to_come = {vertex: (inf, inf, inf) for vertex in G}
    cost_to_come[start] = (0, 0, 0)
    open_list = {start}
    route_taken = []

    while open_list:
        curr_vertex = min(open_list, key=lambda v: cost_to_come[v])
        open_list.remove(curr_vertex)
        curr_cost = cost_to_come[curr_vertex]

        for neighbor in G[curr_vertex]:
            fuzzy_weight = G[curr_vertex][neighbor]['weight']
            new_fuzzy_cost = (
                min(curr_cost[0] + fuzzy_weight[0], cost_to_come[neighbor][0]),
                min(curr_cost[1] + fuzzy_weight[1], cost_to_come[neighbor][1]),
                min(curr_cost[2] + fuzzy_weight[2], cost_to_come[neighbor][2])
            )

            if new_fuzzy_cost < cost_to_come[neighbor]:
                cost_to_come[neighbor] = new_fuzzy_cost
                route_taken.append((curr_vertex, neighbor))
                open_list.add(neighbor)

    shortest_path = []
    trace = end
    while trace != start:
        for step in reversed(route_taken):
            if step[1] == trace:
                shortest_path.append(trace)
                trace = step[0]
                break
    shortest_path.append(start)
    shortest_path.reverse()

    return shortest_path, cost_to_come[end]

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
            u, v, w_min, w_mean, w_max = line.strip().split()
            edges.append((u, v, (float(w_min), float(w_mean), float(w_max))))

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
    for u, v, w in edges:
        G.add_edge(u, v, weight=w)

    # 检查所有节点是否有位置信息
    missing_positions = [node for node in G.nodes if node not in positions]
    if missing_positions:
        print(f"Warning: The following nodes have no position data: {missing_positions}")

    shortest_path, total_cost = fuzzy_dijkstra(G, start, end)
    print("Shortest path:", shortest_path)
    print("Total cost to reach end:", total_cost)

    # 检查路径中的所有节点是否有位置信息
    if all(node in positions for node in shortest_path):
        plot_graph(G, shortest_path, positions)
    else:
        print("Error: Not all nodes in the shortest path have position data.")
