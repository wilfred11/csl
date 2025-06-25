## Causal discovery

A causal graph contains nodes and edges which link nodes that are causally related.

### Assumptions

**The Causal Markov Condition** implies that once you know the direct causes of a variable, any other information about its non-descendants becomes irrelevant in predicting its value. 

**Causal Faithfulness** in causal inference states that the conditional independence relationships observed in a probability distribution accurately reflect the causal structure.

**Causal Sufficience** refers to the assumption that all relevant confounders (unobserved variables that influence both the cause and effect) have been measured and included in the analysis.

**Acyclicity** means there can be no cycle in the causal graph.

### Knowledge
A Markov equivalence class, in the context of graphical models, is a set of Directed Acyclic Graphs (DAGs) that all represent the same set of conditional independence relationships between variables. These DAGs, despite potentially having different edge orientations, share the same skeleton (undirected graph with the same edges) and the same "v-structures" (patterns where two converging arrows point to the same node). A Completed Partially Directed Acyclic Graph (CPDAG) can uniquely represent a Markov equivalence class. 

### Conditional independence tests

Conditional independence (CI) tests are crucial for causal discovery, as they help identify relationships between variables by determining if they are statistically independent given a set of other variables. These tests form the foundation of constraint-based causal discovery algorithms like the PC algorithm, which use CI relationships to infer causal structures.

#### Null hypothesis
The null hypothesis assumes that there is no association between the two variables of interest. A p-value can then be calculated and if it is below 0.05 the null hypothesis will be rejected suggesting that there is significant association between the variables.

### Experiment
In this test I will try to find the dependencies between variables altitude, latitude and temperature. I found some dataset that includes several cities in Brazil, the latitude, altitude and the temperature, I will try to find a causal graph that captures dependencies. 
#### Predicted outcome
Google's AI engine states Latitude and altitude both have a significant impact on temperature. 
> Generally, as latitude increases (moving away from the equator towards the poles), temperatures tend to decrease. Similarly, temperature decreases with increasing altitude, meaning higher altitudes are typically colder

