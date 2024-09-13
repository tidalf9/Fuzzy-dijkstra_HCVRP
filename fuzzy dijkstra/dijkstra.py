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


def read_graph_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        num_nodes = int(lines[0].strip())
        num_edges = int(lines[1].strip())

        edges = []
        for line in lines[3:]:
            u, v, weight = map(float, line.strip().split())
            edges.append((int(u), int(v), weight))

    return edges


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python dijkstra.py <graph_file> <start_node> <end_node>")
        sys.exit(1)

    graph_file = sys.argv[1]
    start = int(sys.argv[2])
    end = int(sys.argv[3])

    edges = read_graph_from_file(graph_file)

    G = nx.Graph()
    G.add_weighted_edges_from(edges)

    shortest_path, total_cost = dijkstra(G, start, end)
    print("Shortest path:", shortest_path)
    print("Total cost to reach end:", total_cost)

    pos = nx.spring_layout(G)  # 使用 spring 布局来绘制图形
    plot_graph(G, shortest_path, pos)
