from causallearn.graph.GraphNode import GraphNode
from causallearn.search.ConstraintBased.PC import pc
from causallearn.utils.PCUtils.BackgroundKnowledge import BackgroundKnowledge
from pywhy_graphs.viz import draw
import seaborn as sns
import dowhy.gcm as gcm
from discover import get_asia_data, visualize_graph, get_ground_truth_graph
from causallearn.utils.GraphUtils import GraphUtils
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import io
from temp_alt import get_temp_data, show_actual_graph


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
    plt.savefig("own1.png")
    #plt.show()
    #plt.savefig("own.png")

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

### discover causality asian data lungs tuberculosis xray
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
    show(cg.G,labels)
    print(cg)
    cg.draw_pydot_graph(labels)
    plt.show()

    gtg=get_ground_truth_graph()
    print(gtg)
    dot_graph = draw(gtg, shape="circle")
    dot_graph.render(outfile="gt.png", view=True)
    plt.show()



# discover causality on a dataset cities, temperature, latitude, altitude
if do==2:
    relevant_cols= ["temperature","altitude","latitude_"]
    temp_data=get_temp_data()
    sns.pairplot(temp_data[relevant_cols])
    plt.savefig("out/pairplots.png")
    plt.show()
    show_actual_graph()

    ci(temp_data, "altitude", "latitude_", )
    ci(temp_data, "altitude", "temperature")
    ci(temp_data, "latitude_", "temperature")
    ci(temp_data, "altitude", "latitude_", "temperature")
    ci(temp_data, "altitude", "temperature", "latitude_")
    ci(temp_data, "latitude_", "temperature", "altitude")

    cg = pc(temp_data[relevant_cols].to_numpy())
    show(cg.G, relevant_cols)







