import matplotlib.pyplot as plt 

slices = [6,1,12,1,3,2]
activities = ["Sleeping","Eating","Coding","School","Football","Video games"]
col = ["blue","green","gray","purple","brown","orange"]

plt.pie(slices,labels=activities,colors=col,startangle=0,shadow=True,autopct='%1.1f%%') # % means percentage, 1.1f means 1 decimal place (float), %% used to escape the percentage sign 
plt.show()