import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

# this will be a list
slices = [60, 40]
# slices = [120, 80]
labels = ['sixty', 'forty', 'extra1', 'extra2']
colors = ['blue', 'red', 'yellow', 'green']


plt.pie(slices, labels = labels, colors=colors, wedgeprops={'edgecolor': 'black'})
# wedgeprops: in the documentation
# add labels to the list to be displayed inside the slides



plt.title('awesome pie chart') # head of the plot
plt.tight_layout()
plt.show()

# Colors:
# Blue = #008fd5
# Red = #fc4f30
# Yellow = #e5ae37
# Green = #6d904f