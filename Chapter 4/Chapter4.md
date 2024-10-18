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
# Creating Sessions
| Graph                                    | Session                                          |
| ---------------------------------------- | ------------------------------------------------ |
| Every Session must be explicitly created | You can create a `Session` by calling tf.Session |

tf.Session accepts 3 optional arguments:
- `target`: Name of the execution engine
- `graph`: The `Graph` instance to be launched
- `config`: A `ConfigProto` that configures the session's execution

---

Most of the settings in a `ConfigProto` relate to threads and devices.

By Default, a session accesses tensors and operations in the default graph. But if You set the `graph` parameter in tf.Session, the session will execute that graph instead.

---

# Executing a session
> The most important method of the `Session` class is `run`

- `fetches`: Identifiers one or more operations or tensors to be executed, It accepts a wide range of data types. Most app set this param equal to an operation, a tensor, or the name of an operation or tensor.
- `feed_dict`: Data to be fed into a tensor
- `options`: Configuration options for the session's execution
- `run-metadata`: Output data from the session

---
If you assign `fetches` to a tensor, `run` will return an `ndarray` with the same values and shape. 

[Implementaion](./Code4.md)

---

if you assign `fetches` to an Operation, `run` will return an `ndarray` containing the values of the tensor produced by the operation.

[Implementaion file2.py](./Code4.md)

---
If you assign `fetches` to a collection of elements, `run` will return a similar collection containing the processed results.

[Implementaion file2.py](./Code4.md)

The `feed_dict` parameter of `run` plays an important role in applications that process training data with batches.

---
# Interactive sessions
In this session interpreter show output of each line when a code run (line by line output).

> to support interactive development TF provides the `InteractiveSession` class. 
An `InteractiveSession` serves the same role as `Session`, Itself, Default Session when it is constructed.

---

Instead of calling `sess.run`, you can evaluate tensors by calling their `eval` method. There is `run` in `Operation` class also.

[Impelementaion](./Code4.md)

---

# Writing Message to the log
5 point to know about tf logging:
- Tf enables logging through the `tf.logging` package.
- Tf logging is based on regular python logging, and many `tf.logging` functions are identical to the methods of Python's `Logger` class.
- Tf supports 5 logging levels. In order of severity, these are `DEBUG, INFO, WARN, ERROR, and FATAL`.
- To enable logging, an app needs to call `tf.logging` `set_verbosity` with the lowest level of severity that should be logged.
- By default, TF writes log messages to standard output. At the time of this writing, TF logging does not support writing messages to a log file.

---
[Implementaion](./Code4.md)

---
| Function                             | Description                                                                   |
| ------------------------------------ | ----------------------------------------------------------------------------- |
| set_verbosity(level)                 | Enables logging for messages of the given severity level and greater severity |
| debug(msg, *args, **kwargs)          | Logs a message at DEBUG severity                                              |
| info(msg, *args, **kwargs)           | Logs a message at INFO severity                                               |
| warn(msg, *args, **kwargs)           | Logs a message at Warn severity                                               |
| error(msg, *args, **kwargs)          | Logs a message at ERROR severity                                              |
| fetal(msg, *args, **kwargs)          | Logs a message at FETAL severity                                              |
| flush()                              | Forces logging operations to complete                                         |
| log(level, msg, *args, **kwargs)     | Logs a message at the given severity level                                    |
| log_if(level, msg, condition, *args) | Logs a message at the given severity level if the condition is true           |
| log_first_n(level, msg, n, *ars)     | Logs a message at the given severity level at most `n` times                  |
| log_every_n(level, msg, n, *args)    | Logs a message at the given severity level once every `n` times               |

---

> The 3rd parameter of `log_if` defines a condition that determines when the message should be logged.

```
tf.logging.log_if(tf.logging.INFO, 'Output: %f', (output>0), output)
```

The 3 args of `log_first_n` and `log_every_n` is an integer that determines how often should be performed. 


---

