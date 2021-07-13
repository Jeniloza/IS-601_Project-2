# Variance

The Difference in Calculation: Population vs. Sample Variance

There is only one little difference in the calculation of variance, and it is at the very end of it. For both population and sample variance, I calculate the mean, then the deviations from the mean, and then I square all the deviations. I sum all the squared deviations up. So far it was the same for both population and sample variance.

When I calculate population variance, I then divide the sum of squared deviations from the mean by the number of items in the population.

When I calculate sample variance, I divide it by the number of items in the sample less one.

As a result, the calculated sample variance (and therefore also the standard deviation) will be slightly higher than if we had used the population variance formula. The purpose of this little difference it to get a better and unbiased estimate of the population‘s variance (by dividing by the sample size lowered by one, we compensate for the fact that we are working only with a sample rather than with the whole population).