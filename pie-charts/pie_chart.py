import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

# this will be a list
# slices = [60, 40, 30, 20]
# slices = [120, 80, 30, 20]
# # slices = [120, 80]
# labels = ['sixty', 'forty', 'extra1', 'extra2']
# colors = ['#008fd5', '#fc4f30', '#e5ae37', '#6d904f']
# DO NOT USE PIE IF DATA POINTS IS MORE THAN 5- 10 (MAX) ELEMENTS

slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0, 0, 0, 0.1, 0]
# explode = [0, 0, 0, 0.5, 0]


# explode: to remove a chunk out of the pie chart
# shadow: to add shadow effect 
# startangle: to rotate the pie chart
	
plt.pie(slices, labels = labels, wedgeprops={'edgecolor': 'black'}, explode=explode, shadow=True, startangle=90, autopct='%1.1f%%')
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