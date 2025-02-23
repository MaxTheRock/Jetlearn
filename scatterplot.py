import matplotlib 
import matplotlib.pyplot as plt 

xarray = [1,2,3,4,5,6,7,8,9]
yarray = [0,1,0,1,0,1,0,1,0]

plt.scatter(xarray,yarray,label="Scatterplot", color="c", marker="o", s=50)
plt.title("Scattering points")

plt.show()