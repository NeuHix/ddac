from statistics import mean, median

fluxes = [17.3, 70.1, 22.3, 16.2, 20.7]
print(mean(fluxes))

# Mean is vulnerable to outliers like the value 70.1
# as a result it doesn't represent the average value of the list

print(median(fluxes))

# Median is not vulnerable to outliers as it is simply
# a middle of the sorted data set.
# Since only the order of the data points matters,
# not their value, outliers have much less of an effect.
