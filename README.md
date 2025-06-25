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
In this test I will try to find the dependencies between variables altitude, latitude and temperature. I found some dataset containing information on  500+ cities in Brazil. For every city it contains latitude, altitude and average temperature, I will try to find a causal graph that captures dependencies.
#### Predicted outcome
Google's AI engine states Latitude and altitude both have a significant impact on temperature. 
> Generally, as latitude increases (moving away from the equator towards the poles), temperatures tend to decrease. Similarly, temperature decreases with increasing altitude, meaning higher altitudes are typically colder. The causal graph for this mechanism looks like in the picture directly below.

<image src="https://github.com/user-attachments/assets/d5c66b5a-13eb-4f7a-a286-29041d2c9788" width="300"/>

#### Own experiments
Before anything else a pairplot should give some idea. For every 2 columns a pairplot shows how these two columns relates. The diagonal plots show the histogram for every column.

<image src="https://github.com/user-attachments/assets/697f9530-03ad-4b9a-8ad0-cb0b7750e02b" width="300"/>

To get an idea of the associations between variables I have performed a (conditional) independency test for every combination possible. For this test I have used the "dowhy" package.

marginal independency test:

`import dowhy.gcm as gcm`
`gcm.independence_test(data[x], data[y], method="kernel")`

conditional independency test:

`gcm.independence_test(data[x], data[y],conditioned_on=data[z], method="kernel")`

| x  | y  | conditioned_on  | p  | assoc  |
|---|---|---|---|---|
| altitude  | latitude  |   | 0.31  | no  |
| altitude  | temperature  |   | 0.08  | no  |
| latitude  | temperature  |   | 0.05  | yes  |
| altitude  | latitude  | temperature  | 0.79  | no  |
| altitude  | temperature  | latitude  | 0.0   | yes  |
| latitude  | temperature  | altitude  | 0.12  | no  |

Given this data I am able to produce a graph that looks like the graph directly below. I must admit using another statistical method (currently "kernel"), I get different results. The p-values are very close to the critical values so it is a matter of tens of rows to get another result. Brazil does not count that many cities located on mountains or in mountainous area.


![own](https://github.com/user-attachments/assets/791994c4-d959-4e83-8c4a-117b3cd0c310)


<image src="" width="300"/>

#### Using the PC algorithm as implemented by causallearn

Using the PC algorithm as mentioned directly below, I get a result like in my own experiments. I really think I need data that is more global.

`from causallearn.search.ConstraintBased.PC import pc`

`cg = pc(temp_data[relevant_cols].to_numpy())`









