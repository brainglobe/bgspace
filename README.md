# BGSpace
Anatomical space conventions made easy.

[![Python Version](https://img.shields.io/pypi/pyversions/bgspace.svg)](https://pypi.org/project/bgspace)
[![PyPI](https://img.shields.io/pypi/v/bgspace.svg)](https://pypi.org/project/bgspace)
[![Build Status](https://travis-ci.com/brainglobe/bgspace.svg?branch=master)](https://travis-ci.com/brainglobe/bgspace)
[![Coverage Status](https://coveralls.io/repos/github/brainglobe/bgspace/badge.svg?branch=master)](https://coveralls.io/github/brainglobe/bgspace?branch=master)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)


Working with anatomical images, one often encounters the problem of matching the orientation of stacks with different conventions about axes orientation and order. Moreover, when multiple swaps and flips are involved, it can be annoying to map the same transformations to volumes and points (e.g., coordinates or meshes).

`BGSpace` provides a neat way of defining an anatomical space, and of operating stacks and point transformations between spaces.

## Installation

You can install `BGSpace` with:
```
pip install bgspace
```


## Usage
To define a new anatomical space, it is sufficient to give the directions of the stack origin position:

```python
source_origin = ("Left", "Superior", "Anterior")
target_origin = ("Inferior", "Posterior", "Right")
```

A stack can be then easily transformed from the source to the target space:

```python
import bgspace as bg
import numpy as np
stack = np.random.rand(3, 2, 4)

mapped_stack = bg.map_stack_to(source_origin, target_origin, stack)
```


The transformation is handled only with numpy index operations; *i.e.*, no complex
image affine transformations are applied. This is often useful as the preparatory step for starting any kind of image registration.

A shortened syntax can be used to define a space using initials of the origin directions:

```python
mapped_stack = bg.map_stack_to("lsa", "ipr", stack)
```

---
**NOTE**

When you work with a stack, the origin is the upper left corner when you show the first element `stack[0, :, :]` with matplotlib or when you open the stack with ImageJ.

---

## The `SpaceConvention` class

Sometimes, together with the stack we have to move a set of points (cell coordinates, meshes, etc.). This introduces the additional complexity of keeping track, together with the axes swaps and flips, of the change of the origin offset.

To handle this situation, we can define a source space using the `SpaceConvention`
class, specifying also the stack shape::

```python

stack = np.random.rand(3, 2, 4)  # a stack in source space
annotations = np.array([[0, 0, 0], [2, 1, 3]])  # related point annotations

source_space = bg.SpaceConvention(target_origin, stack.shape)

mapped_stack = source_space.map_stack_to("ipr", stack)  # transform the stack
mapped_annotations = source_space.map_points_to("ipr", annotations)  # transform the points
```


The points are transformed through the generation of a transformation matrix.
Finally, if we want to log this matrix (e.g., to reconstruct the full transformations sequence of a registration), we can get it:

```
    target_space = bg.SpaceConvention("ipr", stack.shape)
    transformation_matrix = SpaceConvention.transformation_matrix_to(target_space)
    # equivalent to:
    transformation_matrix = SpaceConvention.transformation_matrix_to("ipr", stack.shape)
```

The target get always be defined as a `bg.SpaceConvention` object, or a valid origin specification plus a shape (the shape is required only if axes flips are required).

## #TODO

- [ ] Iterate over axes names for plots, add utils for (dependency-free) label generation for plots;
- [ ] Get stack projections in user-defined order;
- [ ] Get stack planes at hairline cross in user-defined order;
