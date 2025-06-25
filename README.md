## Causal discovery

A causal graph contains nodes and edges which link nodes that are causally related.

### Assumptions

**The Causal Markov Condition** implies that once you know the direct causes of a variable, any other information about its non-descendants becomes irrelevant in predicting its value. 

**Causal Faithfulness** in causal inference states that the conditional independence relationships observed in a probability distribution accurately reflect the causal structure.

**Causal Sufficience** refers to the assumption that all relevant confounders (unobserved variables that influence both the cause and effect) have been measured and included in the analysis.

**Acyclicity** means there can be no cycle in the causal graph.

### Knowledge
A Markov equivalence class, in the context of graphical models, is a set of Directed Acyclic Graphs (DAGs) that all represent the same set of conditional independence relationships between variables. These DAGs, despite potentially having different edge orientations, share the same skeleton (undirected graph with the same edges) and the same "v-structures" (patterns where two converging arrows point to the same node). A Completed Partially Directed Acyclic Graph (CPDAG) can uniquely represent a Markov equivalence class. 

