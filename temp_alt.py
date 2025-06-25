import networkx as nx
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


# Set colours for plots
COLORS = [
    '#00B0F0',

    '#FF0000',
    '#B0F000'
]

def plot_graph(input_graph, node_lookup):
    '''
    Function to visualise graphs.

    Args:
        input_graph (array): Adjacency matrix representing graph
        node_lookup (dict): Dictionary containing node names.
    '''

    graph = nx.DiGraph(input_graph)

    plt.figure(figsize=(8, 8))
    nx.draw(
        G=graph,
        node_color=COLORS[0],
        node_size=8000,
        arrowsize=17,
        with_labels=True,
        labels=node_lookup,
        font_color='white',
        font_size=9,
        pos=nx.circular_layout(graph)
    )
    plt.show()

def get_temp_data():
    data=pd.read_csv("data/temp-alt-2020.csv")
    print(data.head())
    print(data.columns)
    #data.dropna(inplace=True)
    #data = data.replace(np.inf, np.nan).replace(-np.inf, np.nan).dropna()
    """print(data['temperature'].isna().sum())
    print(data['lat'].isna().sum())
    print(data['altitude'].isna().sum())
    print(data['temperature'].isnull().sum())
    print(data['lat'].isnull().sum())
    print(data['altitude'].isnull().sum())
    """
    pattern = r'(?P<d>[\d\.]+).*?(?P<m>[\d\.]+).*?(?P<s>[\d\.]+)'
    dms = data['lat'].str.extract(pattern).astype(float)
    data['latitude_'] = dms['d'] + dms['m'].div(60) + dms['s'].div(3600)
    """
    print(data['temperature'].isna().sum())
    print(data['lat'].isna().sum())
    print(data['altitude'].isna().sum())
    print(data['temperature'].isnull().sum())
    print(data['lat'].isnull().sum())
    print(data['altitude'].isnull().sum())
    """
    #print(data.isnull().sum().sum())
    #print(data.isnull().any())
    null_mask = data.isnull().any(axis=1)
    print(null_mask)
    null_rows = data[null_mask]
    data = data.drop(null_rows.index)
    data.reset_index(inplace=True)
    #print(null_rows)
    print(data.isna().any(axis=None))
    return data


def nodes():
    node_lookup = {0: 'latitude_', 1: 'altitude',2: 'temperature'}
    return node_lookup

def graph():
    total_nodes = len(nodes())

    # Create adjacency matrix - this is the base for our graph
    graph_actual = np.zeros((total_nodes, total_nodes))
    print(graph_actual)

    # Create graph using expert domain knowledge
    graph_actual[0, 2] = 1.0  # Temperature -> Ice cream sales
    graph_actual[1, 2] = 1.0  # Temperature -> Shark attacks

    plot_graph(input_graph=graph_actual, node_lookup=nodes())