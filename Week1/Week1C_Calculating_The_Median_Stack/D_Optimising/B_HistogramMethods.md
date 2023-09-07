If there were a way to calculate a "*running median*" you could save space by only having one image loaded at a time. Unfortunately, there’s no way to do an exact running median, but there are ways to do it *approximately*.

The [binapprox](http://www.stat.cmu.edu/~ryantibs/papers/median.pdf) algorithm does just this. The idea behind it is to find the median from the data's histogram. As an example, say we have a list of 30 numbers between 7 and 16 and its histogram is:

 ![zoinks](https://groklearning-cdn.com/modules/dw9AvcWCtyCN4L6JXMLMk4/histogram_labelled.png)

The median is the average of the 15th and 16th numbers in the ordered list (we can think of this as the 15.5th number). So, starting from the left, if we sum up the counts in the histogram bins until we get to just over 15.5 then we know the last bin we added must have contained the median.

In our example, the first 3 bins sum to 9 and the first 4 bins sum to 18, so we know that the median falls into the 4th bin (marked in red), and so it must be between 10 and 11.

We choose the middle (or midpoint) giving an estimate of 10.5.
