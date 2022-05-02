
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\NEAK\\Downloads\\company_sales_data.csv")
profitList = df['total_profit'].to_list()
monthList = df['month_number'].to_list()
plt.plot(monthList, profitList, label='Month-wise Profit data of last year')
plt.xlabel('Month number')
plt.ylabel('Profit in dollar')
plt.xticks(monthList)
plt.title('Company profit per month')
plt.yticks([100000, 200000, 300000, 400000, 500000])
plt.show()

df = pd.read_csv("C:\\Users\\NEAK\\Downloads\\company_sales_data.csv")
profitList = df['total_profit'].to_list()
monthList = df['month_number'].to_list()

plt.plot(monthList, profitList, label = 'Profit data of last year', color='b', marker='o', markerfacecolor='k',
         linestyle='--', linewidth=3)

plt.xlabel('Month Number')
plt.ylabel('Profit in dollar')
plt.legend(loc='lower right')
plt.title('Company Sales data of last year')
plt.xticks(monthList)
plt.yticks([100000, 200000, 300000, 400000, 500000])
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

fd = pd.read_csv("C:\\Users\\NEAK\\Downloads\\company_sales_data.csv")
monthList = fd['month_number'].tolist()
faceCreamSalesData = fd['facecream'].tolist()
faceWashSalesData = fd['facewash'].tolist()
toothPasteSalesData = fd['toothpaste'].tolist()
bathingSoapSalesData = fd['bathingsoap'].tolist()
shampoosSalesData = fd['shampoo'].tolist()
moisturizerSalesData = fd['moisturizer'].tolist()

plt.plot(monthList, faceCreamSalesData, label='Face cram Sales Data', marker='o', linewidth=3)
plt.plot(monthList, faceWashSalesData, label='Face Wash Sales Data', marker='o', linewidth=3)
plt.plot(monthList, toothPasteSalesData, label='Toothpaste Sales Data', marker='o', linewidth=3)
plt.plot(monthList, bathingSoapSalesData, label='ToothPaste Sales Data', marker='o', linewidth=3)
plt.plot(monthList, shampoosSalesData, label='ToothPaste Sales Data', marker='o', linewidth=3)
plt.plot(monthList, moisturizerSalesData, label='ToothPaste Sales Data', marker='o', linewidth=3)

plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.legend(loc='upper left')
plt.xticks(monthList)
plt.yticks([1000, 2000, 3000, 4000, 5000, 6000, 8000, 10000, 12000, 15000, 18000])
plt.title('Sales Data')
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\NEAK\\Downloads\\company_sales_data.csv")
monthList = df['month_number'].to_list()
toothPasteSalesData = df['toothpaste'].to_list()
plt.scatter(monthList, toothPasteSalesData, label='Tooth paste Sales data')
plt.xlabel('Month Number')
plt.ylabel('Number of units Sold')
plt.legend(loc='upper left')
plt.title(' Tooth paste Sales data')
plt.grid(True, linewidth=1, linestyle="--")
plt.show()
