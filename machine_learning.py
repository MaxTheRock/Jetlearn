
import numpy

x = [1,2,3,4,5]
y = [5,4,3,2,1]

def find_mean(a):
  return sum(a)/len(a)

mean_of_x = find_mean(x)
mean_of_y = find_mean(y)

n = 0
d = 0

for i in range (len(x)):
  n = n + ((x[i] - mean_of_x)*(y[i] - mean_of_y)) # Covariance of numerative part of the slope
  d = d + ((x[i] - mean_of_x)**2) # Shows how far they spread out, it helps us understand how much space is needed for the x

gradient = n/d

print(gradient)

intercept = mean_of_y - (gradient * mean_of_x)

print(intercept)