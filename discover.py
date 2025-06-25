import bnlearn as bn
import networkx as nx
from causallearn.utils.GraphUtils import GraphUtils
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import io


def get_asia_data():
    d = bn.import_example(data='asia')

    d.rename(columns={
        'tub': 'T',
        'lung': 'L',
        'bronc': 'B',
        'asia': 'A',
        'smoke': 'S',
        'either': 'E',
        'xray': 'X',
        'dysp': 'D'},
        inplace=True
    )

    labels = d.columns
    print(labels)
    print(d.head())
    data = d.to_numpy()
    return data, labels

def visualize_g(cg, labels):
    nx.draw(cg.G, pos=nx.spring_layout(cg.G))
    plt.show()

def visualize_graph(cg, labels):
    print("vis")
    pyd = GraphUtils.to_pydot(cg.G, labels)

    #print(type(pyd))
    tmp_png = pyd.create_png(f="png")
    print("fp")
    fp = io.BytesIO(tmp_png)
    img = mpimg.imread(fp, format='png')
    plt.axis('off')
    plt.imshow(img)
    plt.show()

def get_ground_truth_graph():
    ground_truth_edges = [
        ("A", "T"),
        ("T", "E"),
        ("L", "E"),
        ("S", "L"),
        ("S", "B"),
        ("B", "D"),
        ("E", "D"),
        ("E", "X")
    ]
    ground_truth = nx.DiGraph(ground_truth_edges)
    return ground_truth

def vis_gt(ground_truth_graph):
    pos = nx.spring_layout(ground_truth_graph, seed=1234)
    nx.draw(ground_truth_graph, with_labels=True, pos=pos)
    plt.show()