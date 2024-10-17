`FrameWorks automate many aspexts of developing ml applications. and they allow developers to re-use code and take advantage of best practices.`

# 5 most popular frameworks:
1. `Torch`\
   1st ml framework to attract a sgnificant following. 
   Release: 2002 (Ronan Collobert)
   Used as a tool for neumerical computing.
   Computation with the framework involves multidimenional arrays called `tensors`. Which can be processed regular vector/matrix operations.
   With Time, it acquired routines for building training and evaluating neural networks.
   `Interface language lua`.

2. `Theano`\
   2010: Group at the University of Montreal reseased theano a library for numeric computation. Like Numpy, Theano Stores information as `graph` data structures. Which it compiles into high-performance code. Module also supports `symobolic differentiation`, which makes its possible to find derivatives of functions automatically.

   Theano able to get processed on CPUs and GPUs. 
   `Written in python`.

3. `Caffe`\
   At `UC Berkeley, YangQing Jia created Caffe`, a framework for developing Image Recognition applications. As other joined the development, Caffe expanded to support other ml algos and many different types of nn.

   `Caffe is written in C++`
   It supports GPU acceleration. 

   in 2007 Caffe2 was released.

4. `Keras`\
   Focusses on Modularity and Simpicity of the development. 
   Fracois Chollet created Keras as an interface to mlframeworks. 
   Developers combined keras and accessing theano through keras for simplicity and performance.
   
   Keras was released under the MIT license and google has incorporated his interface into Tensorflow. For this reson, many Tensorflow developers prefer to code their nn using keras.

5. `Tensorflow`\
   Developed by Google.
   The Google Brain Team released the tensorflow 1.0 in 2015.
   Apache 2.0 openSource license. Allows the free use and modifications.

   Interface Language is python But Core Language is written C++ for improved performance. Tensorflow saves operations in a graph that can be deployed to a GPU, a remote system, or a network of remote systems. 
   TensorBoard, which make visualizing graphs and their operations possible.

   tensorflow Supports CPU and GPU. Application of tensorflow can be executed on the GCP(Google Cloud Platform). provind low-cost processing power.



