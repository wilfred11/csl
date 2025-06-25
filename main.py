import networkx as nx
from causallearn.graph.GraphNode import GraphNode
from causallearn.search.ConstraintBased.PC import pc
from causallearn.utils.PCUtils.BackgroundKnowledge import BackgroundKnowledge
from pywhy_graphs import CPDAG
from pywhy_graphs.viz import draw
import matplotlib.pyplot as plt
import seaborn as sns
import dowhy.gcm as gcm

from discover import get_asia_data, visualize_graph, get_ground_truth_graph, vis_gt, visualize_g

from causallearn.utils.GraphUtils import GraphUtils
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import io

from temp_alt import get_temp_data, graph

#from dodiscover import PC, make_context
#from dodiscover.ci import GSquareCITest, Oracle
#from dodiscover.ci.g_test import GSquareCITest
#from  dodiscover.ci.oracle import Oracle
#from dodiscover.constraint import  PC
#from dodiscover import Context, make_context

do = 2
#https://www.youtube.com/watch?v=NIqeFYUhSzU

#https://www.kaggle.com/datasets/lgmoneda/temperature-and-altitude?resource=download
#https://www.youtube.com/watch?v=M2lL2gcLU-k

def show(g, labels):
    pyd = GraphUtils.to_pydot(g, labels=labels)
    tmp_png = pyd.create_png(f="png")
    fp = io.BytesIO(tmp_png)
    img = mpimg.imread(fp, format='png')
    plt.axis('off')
    plt.imshow(img)
    plt.show()

def ci(data,x,y,z=""):
    print("##############################")
    print("testing:"+ x+" "+" "+y+" given:"+z)
    if z=="":
        p=round(gcm.independence_test(data[x], data[y], method="kernel"), 2)
    else:
        p = round(gcm.independence_test(data[x], data[y],conditioned_on=data[z], method="kernel"), 2)

    print("p-value: "+str(p))

    if p>0.05:
        print("no assoc "+x+" "+y+" given "+ z )
    else:
        print("assoc " + x + " " + y + " given " + z)
    print("##############################")


if do==1:
    data, labels = get_asia_data()
    E = GraphNode('E')
    T = GraphNode('T')
    L = GraphNode('L')
    S = GraphNode('S')

    bk = BackgroundKnowledge()
    #bk.add_forbidden_by_node(A,B)
    bk.add_required_by_node(L,E)
    bk.add_required_by_node(S,L)
    bk.add_required_by_node(T,E)

    cg = pc(data, indep_test="", background_knowledge=bk, stable=True)
    #print(cg.G)
    show(cg.G,labels)
    print(cg)
    cg.draw_pydot_graph(labels)
    #dot_graph1.render(outfile="lt.png", view=True)
    #nx.draw_networkx(cg.G, with_labels=True)
    plt.show()


    #visualize_graph(cg, labels)
    gtg=get_ground_truth_graph()
    print(gtg)
    dot_graph = draw(gtg, shape="circle")
    dot_graph.render(outfile="gt.png", view=True)


    #nx.draw_networkx(gtg, with_labels=True)
    plt.show()
    #show(gtg, None)
    #vis_gt(gtg)

    cpdag_directed = [
        ("T", "E"),
        ("L", "E"),
        ("B", "D"),
        ("E", "D"),
        ("E", "X")
    ]

    cpdag_undirected = [
        ("A", "T"),
        ("S", "L"),
        ("S", "B"),
    ]

    #ground_truth_cpdag = CPDAG(cpdag_directed, cpdag_undirected)

    #draw(ground_truth_cpdag, direction='TB')
    #plt.show()
    print("hier")



if do==2:
    relevant_cols= ["temperature","altitude","latitude_"]
    temp_data=get_temp_data()
    sns.pairplot(temp_data[relevant_cols])
    plt.show()
    graph()

    ci(temp_data, "altitude", "latitude_", )
    ci(temp_data, "altitude", "temperature")
    ci(temp_data, "latitude_", "temperature")
    ci(temp_data, "altitude", "latitude_", "temperature")
    ci(temp_data, "altitude", "temperature", "latitude_")
    ci(temp_data, "latitude_", "temperature", "altitude")

    labels = ["altitude","latitude_","temperature"]
    cg = pc(temp_data[["altitude","latitude_","temperature"]].to_numpy())
    # print(cg.G)
    show(cg.G, labels)

    #print(round(gcm.independence_test(temp_data["altitude"], temp_data["latitude_"], conditioned_on=temp_data["temperature"], method='gcm'), 2))
# Visualization using pydot








#match_directed = nx.is_isomorphic(ground_truth_cpdag.sub_directed_graph(), .sub_directed_graph())
#match_undirected = nx.is_isomorphic(ground_truth_cpdag.sub_undirected_graph(), graph.sub_undirected_graph())

#print(f'The oracle learned CPDAG via the PC algorithm matches the ground truth in directed edges: {match_directed} \n'
#      f'and matches the undirected edges: {match_undirected}')

#ci_estimator = GSquareCITest(data_type="binary")
#pc = PC(ci_estimator=ci_estimator, alpha=0.05)

#pc.learn_graph(data, context)

#graph = pc.graph_
#draw(graph, direction='TB')







