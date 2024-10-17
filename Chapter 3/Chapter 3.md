# Creating Tensors and Operations

### Creating Tensors

- Scalar Tensor:- Having zero-dimensions
- Vector Tensor:- Having One-dimention
- Matrix:- 2d tensor

# Important Points
- Every tensor is an instance of the tensor class.
- A tensor may contain numbers, strings, or Boolean values. Every element of a tensor must have the same type.
- tensors can be created, transformed, and operated upon using functions of the `tf` package.

---

# Creating Tensors with known Values

Function | Description
--|--
constant(value, dtype=None, shape=None, name='Cost', verify_shape=False) | Returns a tensor containing the given value
zeros(shape, dtype=tf.float32, name=None) | Returns a tensor filled with zeros
ones(shape, dtype=tf.float32, name=None) | Returns a tensor filled with the given value
fill(dims, value, name=None) | Returns a tensor filled with the given value
linspace(start, stop, num, name=None) | Returns a tensor containing a linear range of values
range(start, limit, delta=1, dtype=None, name='range') | Returns a tensor containing a range of values
range(limit, delta=1, dtype=None, name='range') | Returns a tensor containing a range of values


### `Rank`:- The number of dimensions of the tensor.

> [] - The tensor contains a single value.\
> [3] - The tensor is a one-dimensional array containing 3 values.\
> [3, 4] - The tensor is a 3-x-4 matrix.\
> [3, 4, 5] - The tensor is a multidimensional array whose dimensions equal 3, 4, and 5.\
>Default is float32=dtype

# Tensor Data Types
Data Type | Description
--|--
bool | Boolean values
uint8/uint16 | unsigned integers
quint8/quint16 | Quantized unsigned integers
int8/int16/int32/int64 | Signed integers
qint8/qint32 | Quantized signed integers
float16/float32/float64 | Floating-point values
complex64/complex128 | Complex floating-point values
string | Strings
---


# The Constant Function
Required argument is the first argument, which defines the value or values to be stored in the tensor. \
The Code part Strats from here:
[Code](./Code.md)

---
# Zeros, ones, and fill
[Code](./Code.py)

---

# Creating Sequences
The linspace and range functions create tensors whose elements change regularly between a start and end value. The difference between them is that linspace creates a tensor with a specific number of values.
For example, the following code creates a 1-x-5 tensor whose elements range from 5.0 to 9.0:

[Code1](./Code.md)

---
# Creating Tensors with Random Values
Funcion | Description
--|--
random_normal(shape, mean=0.0, stddev=1.0, dtype=tf.float32, seed=None, name=None) | Creates a tensor with normally distributed values
truncated_normal(shape, mean = 0.0, stddev=1.0, dtype=tf.float32, seed=None, name=None) | Creates a tensor with normally distributed values excluding those lying outside two standard deviations
random_uniform(shape, minval=0, maxval=None, dtype=tf.float32, seed=None, name=None) | Creates a tensor with uniformly distributed values between the minimum and maximum values
random_shuffle(tensor, seed=None, name=None) | Shuffles a tensor along its first dimension
set_random_seed(seed) | Set the seed value for all random number generation in the graph
---
The `random_normal` and `truncated_normal` funcitons crete tensors containing noramally distributed values. Their arguments determine the characterristics of the distribution.

[Code](./Code.md)

- Truncated_normal guarentees that the generated values lie within 2 std deviations from the mean.
- any value outside this range will be discarded and reselected. 

---
`random_uniform`: creates a tensor containing uniformly distributed values that lie between a minimum and maximum. Because the distribution is uniform, every value is equally likely.

`random_shuffle`: does not create a new tensor, but randomly shuffles the values in an existing tensor. 
This shuffling is limited to the tensor's first dimension.

---
# Transforming Tensors
# Functions for transforming tensors
Function | Description
--|--
cast(tensor, dtype, name=None) | Changes the tensor's data type to the given type
reshape(tensor, shape, name=None) | returns a tensor with the same elements as teh given tensor with the given shapes
squeeze(tensor, axis=None, name=None, squeeze_dims=None) | removes dimensions of size 1
reverse(tensor, axis, name=None) | Reverses given dimensions of the tensor
slice(tensor, begin, size, name=None) | Extracts a portion of a tensor
stack(tensors, axis=0, name='stack') | Combines a list of tensors into a tensor of greater rank
unstack(tensor, num=None, axis=0, name='unstack) | splits a tensor into a list tensors of lesser rank
---

> Reshape does not modify an existing tensor. Instead, the function returns a tensor with the same elements ast eh given tensor and the specified shape. Ex.
> [Code](./Code.md)

- If any dim of a tensor has a size of 1, calling `squeeze` will remove it from the tensor, thereby reducing the tensor's rank. if the function's axis parameter identifies one or more dim only those dim will be affected by squeeze.

---
The slice function extracts subtensors from a tensor. The `begin` parameter identifies the index of the first element to be extracted, and size identifies the shape of the tensor to be extracted, starting from the `begin` location/

Example: suppose that you want to extract the lower-right 2-x-2 matrix from a 3-x-3 matrix. The index of the first extracted element is [1, 1] and the size of the desired tensor is [2, 2]. The Code implementation [Code](./Code.md)

---
`Stack` accepts a list of tensors of rank N and returns a single tensor of rank N+1. 
In addition to having the same rank, the input tensors must have the same shape.

implementaion [Code](./Code.md)

---
# Creating Operations
---
### Basic Math Operation
Function | Description
--|--
add(x, y, name=None) | Adds 2 tensors
subtract(x, y, name=None) | Subtracts two tensors
multiply(x, y, name=None) | Multiplies 2 tensors
divide(x, y, name=None) | Divides the elements of 2 tensors
div(x, y, name=None) | Divides the elements of 2 tensors
add_n(inputs, name=None) | Adds multiple tensors
scalar_mul(scalar, x) | Scales a tensor by a scalar value
mod(x, y, name=None) | perorms the modulo operation
abs(x, name=None) | Computes the abosute value
negative(x, name=None) | Negates the tensor's elements
sign(x, name=None) | Extracts the signs of the tensor's element
reciprocal(x, name=None) | Computes the reciprocals

[Implementation](./Code.md)
---

When operating on floating-point values, `div` and `divide` produce the same result.
For integers division, `divide` returns a floating-point result, and `div` returns an integer result.

[implementation](./Code.md)

---

# Rounding and comparison
Function | Description
--|--
round(x, name=None) | Rounds to the nearest integer, rounding up if there are 2 nearest integers
rint(x, name=None) | Rounds to the nearest integer, rounding to the nearest even integer if there are 2 nearest integers.
ceil(x, name=None) | Returns the smallest integer greater than the value
floor(x, name=None) | returns the greatest integer less than the value
maximum(x, y, name=None) | Returns a tensor containing the larger element of each input tensor
minimum(x, y, name=None) | Returns a tensor containing the smaller element of each input tensor
argmax(x, axis=None, name=None, dimension=None) | Returns the index of the greatest element in the tensor
argmin(x, axis=None, name=None, dimension=None) | Returns the index of the smallest element in the tensor

