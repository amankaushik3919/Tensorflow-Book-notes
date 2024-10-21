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

In `log_first_n`, the value sets the max number of times the function should write its message to the log.
In `log_every_n`, the value tells teh function to log its message once every _N_ times it is called.

---

# Visualizing Data with TensorBoard

>Logging is less used for large datasets.
>Logging is not sufficient to monitor how data changes with each execution.

The `TensorBoard` resolves this issue.

`TensorBoard` reads an app data and display it in a web page.
it requires specially formatted data.

# Running TensorBoard

It accepts 3 flags.
- --logdir DIR: The directory containing the summary data.
- --host HOST: Identifies the host portion of the page's URL.
- --port PORT: Identifies the port of the web page's URL.

Default IP == 127.0.0.1\
Default Port == 6006\
Default URL == http://localhost:6006


--logidir flag is required, So that tensorboard will not launch without data.
where `flag` refers to a directory containing special file _`event file`_.
The `event file` contains the summary data that is needed for tensorboard, for visualization. 

----
# Generating Summary Data
Creating math operation and execute them in a session.
The above talk introduces to a new type of operation called a _`summary operation`_. 
This resembles other TF operations, but when a session executes a summary operation, 
the result is a protocol buffer thatcontains summary data. An app can write this buffer to a file whose content can be displayed with Tensor Board(TB).

TB can illustrate many DT's and each corressponds to a function of tf.summary.

Function | Description
--|--
scalar(name, tensor, collections=None) | Creates a summary operation that provides data about a scalar
histogram(name, values, collections=None) | Creates a summary operation that provides histogram data
audio(name, tensor, sample_rate, max_output=3, collections=None) | Creates a summary operation that provides data from an audio source
image(name, tensor, max_outputs=3, collections=None) | Creates a summary operation that provides data from an image
merge(inputs, collections=None, name=None) | Merges the specified summary operations into one summary operation
merge_all(key=tf.GraphKeys.SUMMARIES) | Merges summary operations into one summary operation

---
- tf.summary.scalar generates operations that provide scalar data.
- tf.summary.merge_all combines them into one operation.
- sess.run executes the merged summary operation.

[Implementation](./Code4.md)

----
# Creating Custom Summaries
By Creating `Summary` object you can generate custom summary data.
The `Summary class` is python wrapper for a protocol buffer containing summary data.

`Summary` instance creation can be done `tf.Summary` and setting its value parameter to a list of `Summary.Value` buffers. Each `Summary.Value` can have a `none_name`, a tag, and one of 5 data field:
- simple_value: - a 32-bit floating-point value.
- image: - an Image instance containing pixel data
- histo: - a HistogramProto containing data to be displayed in a histogram
- audio: - an Audio instance containing audio data
- tensor: - a TensorProto containing data related to tensors.

#### Example Code
```Python
custom_summary = tf.Symmary(value=[
    tf.Summary.Value(tag="num_tag", simple_value=5.0),
])
```

# Writing Summary data

### Creating a File Writer
```python
tf.summary.FileWriter(logdir, graph=None, max_queue=10, flush_secs=120, filename_suffix=None)
```
A FileWriter updates the event file asynchronously.

The code creates FileWriter and configures it to create a directory named `log`. The event file in this will contain summary data for the default graph.
```python
fw = tf.summary.FileWriter("log", graph=tf.get_default_graph())
```

#### Printing data to the event file

Method | Description
--|--
add_summary(summary, global_step=None) | Adds summary data to the event file
add_event(event) | Adds event data to the event file
add_graph(graph, global_step=None, graph_def=None) | Adds summary data for the graph to the event file
add_meta_graph(meta_graph_def, global_step=None) | Adds data from a MetaGraphDef to the event file
add_run_metadata(run_metadata, tag, global_step=None) | Adds run metadata from a session to the event file
add_session_log(session_log, global_step=None) | Adds data from a SessionLog to the event file
flush() | Executes pending write operations
close() | Flushes write operations and closes teh event file
reopen() | Reopens the eveent file for writing summary data

---

`add_summary` prints summary data. 

```python
# Merge operations into a single operation
merged_op = tf.summary.merge_all()

# Create the FileWriter
writer = tf.summary.FileWriter("summar")

with tf.Session() as sess:
    _, summary = sess.run([sum, merged_op])
    writer.add_summary(summary)
    writer.close()
```

Each event has a `wall_time` field that identifies the time and a step that identifies the global. An `Event'`s data is specified by the `what` field, which can be set top one of the following:
- file_version: - The version of the event file
- graph_def: - Content of GraphDef buffer
- summary: - an Summary containing summary data
- log_message: - LogMessage containing logged messages
- session_log: - SessionLog containing the session's state
- tagged_run_metadata: - TaggedRunMetadata contaning metadata from the session
- meta_graph_def: - content of a MetaGraphDef buffers

```python
new_summary=tf.Summary(value=[
    tf.Summary.Value(tag="val", simple_value=9.0),
])
event = tf.Event(wall_time=time.time(), summary=new_summary)
file_writer.add_event(event)
```


