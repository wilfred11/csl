import networkx as nx
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

def plot_graph(input_graph, node_lookup):
    graph = nx.DiGraph(input_graph)
    plt.figure(figsize=(8, 8))
    nx.draw(
        G=graph,
        node_size=8000,
        arrowsize=17,
        with_labels=True,
        labels=node_lookup,
        font_color='white',
        font_size=14,
        pos=nx.circular_layout(graph)
    )
    plt.savefig("out/true_graph.png")
    plt.show()


def get_temp_data():
    data = pd.read_csv("data/temp-alt-2020.csv")
    print(data.head())
    print(data.columns)
    # convert latitude to a number
    pattern = r'(?P<d>[\d\.]+).*?(?P<m>[\d\.]+).*?(?P<s>[\d\.]+)'
    dms = data['lat'].str.extract(pattern).astype(float)
    data['latitude_'] = dms['d'] + dms['m'].div(60) + dms['s'].div(3600)
    # check nulls
    null_mask = data.isnull().any(axis=1)
    print(null_mask)
    null_rows = data[null_mask]
    data = data.drop(null_rows.index)
    data.reset_index(inplace=True)
    print(data.isna().any(axis=None))
    return data


def nodes():
    node_lookup = {0: 'latitude_', 1: 'altitude', 2: 'temperature'}
    return node_lookup


def actual_graph(length):
    graph_actual = np.zeros((length, length))
    graph_actual[0, 2] = 1.0
    graph_actual[1, 2] = 1.0
    return graph_actual


def show_actual_graph():
    graph_actual = actual_graph(len(nodes()))
    plot_graph(graph_actual, node_lookup=nodes())