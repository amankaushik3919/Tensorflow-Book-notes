# Executing Graphs in Sessions

> In Tensorflow it does not execute its operation Instead, it stores its operation in a data structure called `a graph`

When a Session executes a graph, it performs the graph's operations in order.

# Forming Graphs

The below is the code which gets transformed into graph with tensorflow.
```Code
c = tf.add(a, b)
e = tf.multiply(c, d)
```
The below is the image the tensorflow saves in this graph.
![Image](./image%20graph.jpeg)
The addition operation receives the result of mltiplication.

---

- Graphs can not be nested, and only one `Graph` can be active at a time. 
- An application can access its default `Graph` by calling `get_default_graph`. 

[Impelementaion](./Code4.md)

The `Graph` class provides many methods that access and modify the graph's contents.

- **Accessing graph Data**: Reading a graph's containers and elements.
- **Creating** `GraphDef`**s**: Serializing a graph into a protocol buffer
----

# Accessing graph data

`Graph stores its elements in a set of named collections.`

| Method                           | Description                                                 |
| -------------------------------- | ----------------------------------------------------------- |
| get_tensor_by_name(name)         | Returns the tensor with the given name                      |
| get_operation_by_name(name)      | Returns the operation with the given name                   |
| get_operations()                 | Returns a list containing the graph's operations            |
| get_all_collection_keys()        | Return a list of the graph's collections                    |
| get_collection(name, scope=None) | Returns a list of values in the given collection            |
| add_to_collection(name, value)   | Adds the value to the container, can be accessed with name  |
| add_to_collection(name, value)   | Adds the value to the containers, can be accessed with name |

---

[Implementaion](./Code4.md)

