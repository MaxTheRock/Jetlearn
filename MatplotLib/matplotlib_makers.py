import matplotlib
import matplotlib.pyplot as plt
import numpy as np

a1 = np.array([3,8,1,10])

# plt.plot(a1,marker='*')
# plt.plot(a1,'o:r') # Marker Line Color
# plt.plot(a1,marker='o',ms='15',mec="b",mfc="r")
plt.plot(a1,linestyle='dotted')
plt.show()