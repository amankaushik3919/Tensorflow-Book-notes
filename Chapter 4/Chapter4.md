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

- The additional info. is stored in a set of lists called the graph's `collections`.
- Dictionariesm you can access the elements of a collections using identifiers called `keys`. 

| Collection Key           | Description                                   |
| ------------------------ | --------------------------------------------- |
| GLOBAL_VARIABLES         | All vars used in the application              |
| LOCAL_VARIABLES          | Vars local to this machine                    |
| MODEL_VARIABLES          | Vars used in the model                        |
| TRAINABLE_VARIABLES      | Vars capable of being trained by an optimizer |
| MOVING_AVERAGE_VARIABLES | Variables that maintain moving averages       |
| SUMMARIES                | Tensor summaries                              |
| QUEUE_RUNNERS            | QueueRunners that provide input data          |
| REGULARIZATION_LOSSES    | Losses produced by regularization             |
---
\
\
\
\
\
.

# Creating GraphsDefs

Many Applications need access to graphs from other tf apps. The `as_graph_def` method makes this possible. This ethod returns a serialized form of a `Graph` called a `GraphDef`.

`Protocol Buffer` or `protobuf`: this is a format used to store `graphdef` graph's data.

This is generated in text or binary form. And in text form it is in JSON format.

GraphDef Node has:
1. name field
2. op field
3. 1 or more attr fields

Example:
```Code
node {
    name: "..."
    op:"..."
    arr { ... }
    arr { ... }
    ...
}
```

Last element is versions element. Identifies the version of the GraphDef structure.

The graphDef has 3 nodes. Two that represents Tensors and One that represents the operation taht adds the tensors.

---
`write_graph`(graph/graph_Def, logdir, name, as_text=True)

The above is in the `tf.train` makes it possible to store a Graphdef data to a file.

---

To store a file written in text or binary form:
The below saves the graphdef's data in `graph.data` file:

```Code
tf.train.write_graph(tf.get_default_graph(), os.getcwd(), 'graph.dat')
```
Similarly an app can load a `GraphDef` from a file.

- `TextFormat.Merge`(data, graphdef): Initializes a `GraphDef` from text elements
- Creating `GraphDefs`: Converting a graph into a procol buffer.

`TextFormat` class is provided in `google.protobuf`.\
For more info. https://developers.google.com/protocol-buffers/docs/pythontutorial.

----

# Creating and Running Sessions
