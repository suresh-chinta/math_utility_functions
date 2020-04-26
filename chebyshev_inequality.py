###    Author Suresh Chinta
###    Date April 24th 2020
###    Chebyshev's inequality assures for any random variable with any distribution
###    a certain proportion of values are guranteed to be with in a certain distance from its mean.
###    create two normal variables with different means and sigmas add them, verify if the inequality holds

import numpy as np

mean1 = -10
sigma1 = 20
mean2 = 100
sigma2 = 400

s = np.random.normal(mean1, sigma1, 1000000)
p = np.random.normal(mean2, sigma2, 1000000)
s = (s + p)

sigma = sigma1 + sigma2
mu = mean1 + mean2

# thresholds of sigma
ks = [1.5,2.0,2.5,3.0]

# to hold proportion of values greater than threshold * sigma from mean
probs = []
for k in ks: 
    probs.append(sum(np.abs(np.array(s) - mu) >= k * sigma)/len(s))

# compare actual proportion of values that are beyond threshold * sigma with theoretical proportion (1/threshold **2) of 
# values as per Chebyshev's property
for i, prob in enumerate(probs):
    print("k:" + str(ks[i]) + ", probability: "           + str(prob)[0:5] +           " | in theory, probability should less than: "           + str(1/ks[i]**2)[0:5])

