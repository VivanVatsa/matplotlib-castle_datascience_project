# similar script from barcharts
import pandas as pd
# from matplotlib import pyplot as plt
import matplotlib.pyplot as plt

plt.style.use('seaborn')

data = pd.read_csv('data.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

# # ax => axis (plot)
# # subplot create a figure and then specify a certain number of rows & columns of axis!

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)


ax1.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')


ax2.plot(ages, py_salaries, label='Python')
ax2.plot(ages, js_salaries, label='JavaScript')

ax1.legend()
ax1.set_title('Median Salary (USD) by Age')
ax1.set_xlabel('Ages')
ax1.set_ylabel('Median Salary (USD)')


ax2.legend()
# ax2.set_title('Median Salary (USD) by Age')
ax2.set_xlabel('Ages')
ax2.set_ylabel('Median Salary (USD)')

plt.tight_layout()

plt.show()



# =====
# fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)




# print (ax1)
# print (ax2)
# AxesSubplot(0.125,0.53;0.775x0.35)
# AxesSubplot(0.125,0.11;0.775x0.35)

# print(ax) # AxesSubplot(0.125,0.11;0.775x0.77)
# print(ax) 
# a list of plots -- [<AxesSubplot:> <AxesSubplot:>]
