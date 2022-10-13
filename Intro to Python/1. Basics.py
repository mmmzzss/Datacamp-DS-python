exponential: **
module: %

x = [1,2,3]
y = x 
This is just copying the index rather than the actual values in the list
so we have to use:
  y = list[x]
  y = x[:]
deep copy

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))

# Print out how often 9.50 appears in areas
print(areas.count(9.50))


import numpy as np
np.array([1,2,3])

array 

return --> array([1,2,3])


from numpy import array


# Import numpy
import numpy as np

# Create array from height_in with metric units: np_height_m
np_height_m = np.array(height_in) * 0.0254

# Create array from weight_lb with metric units: np_weight_kg
np_weight_kg = np.array(weight_lb) * 0.453592

# Calculate the BMI: bmi
bmi = np_weight_kg / np_height_m ** 2

# Print out bmi
print(bmi)
results:
  [23.11037639 27.60406069 28.48080465 ... 25.62295933 23.74810865
 25.72686361]
  
  
