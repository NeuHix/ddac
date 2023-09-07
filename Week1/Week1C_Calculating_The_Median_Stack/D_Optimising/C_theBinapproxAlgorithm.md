The [binapprox](http://www.stat.cmu.edu/~ryantibs/papers/median.pdf) algorithm uses the method from the previous slide, but it saves even more time and space by only looking for the median within one standard deviation of the mean (see the link if you’d like to know why that works).

The full algorithm for a set of _**N**_ data points works as follows:

1. Calculate their mean and standard deviation, _**μ**_ and _**σ**_;
2. Set the bounds: `minval` = $\mu - \sigma$ and `maxval` = $\mu + \sigma$. Any `value`>=`maxval` is ignored;
3. Set the bin width: `width` = $2\sigma/B$;
4. Make an ignore bin for counting `value` < `minval`;
5. Make **B** bins for counting values in `minval` and `maxval`, e.g. the first bin is `minval`<= `value` < `minval` + `width`;
6. Count the number of values that fall into each bin;
7. Sum these counts until `total`>=`(N+1)/2`. Remember to start from the ignore bin;
8. Return the midpoint of the bin that exceeded `(N+1)/2`.

The midpoint of a bin is just the average of its min and max boundaries, i.e. the lower boundary + `width/2`

As soon as the relevant bin is updated the data point being binned can be removed from memory. So if you're finding the median of a bunch of FITS files you only need to have one loaded at any time. (The mean and standard deviation can both be calculated from running sums so that still applies to the first step).

The downside of using binapprox is that you only get an answer accurate to $\frac{\sigma}{B}$ by using _**B**_ bins. Scientific data comes with its own uncertainties though, so as long as you keep _**B**_ large enough this isn't necessarily a problem.
