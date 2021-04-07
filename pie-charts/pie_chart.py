import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

# this will be a list
slices = [60, 40]
# slices = [120, 80]
labels = ['sixty', 'forty']




plt.pie(slices, labels = labels)

# add labels to the list to be displayed inside the slides



plt.title('awesome pie chart') # head of the plot
plt.tight_layout()
plt.show()