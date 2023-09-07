We'll go through an example of how to implement the formula you saw on the previous slide using NumPy's trigonometric functions. Please keep in mind that NumPy trigonometric functions only take radians as input so you need to convert your coordinates when needed.

First, let's break down the formula into smaller part:

$$
d = 2 \arcsin \sqrt{a + b} \\
a = \sin^2 \frac{|\delta_1 - \delta_2|}{2} \\
b = \cos \delta_1 \cos \delta_2 \sin^2 \frac{|\alpha_1 - \alpha_2|}{2}
$$

Using Numpy to calculate each of these pieces separately:

```
a = np.sin((d1 - d2)/2)**2
b = np.cos(d1)*np.cos(d2)*np.sin(np.abs(ra1 - ra2)/2)**2
d = 2*np.arcsin(np.sqrt(a + b)
```

Don't forget to convert the arguments into Radians using `np.radians` because Numpy takes angle arguments in radians.
