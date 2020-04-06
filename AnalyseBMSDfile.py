import pandas as pd
import seaborn as sns   #--> plotting module
import matplotlib.pyplot as plt

#Assignmnet is to analyse the BigDataSalesMart.csv file to draw few graphs

table = pd.read_csv("BigMartSalesData.csv")
#print(table.head(20))

table["SalesRev"] = table.UnitPrice * table.Amount

# #plt.scatter(table["SalesRev"], table.Month)
#
# plt.bar(table["SalesRev"],table.Month,align='center')
# plt.xlabel("Sales Total")
# plt.ylabel("Month")
# plt.title("Analyses of Total Sales Year 2011")
# plt.show()


# Sales Revenue = Units Sold x Amount to Calculate total sale

SalesofYear2011 = table[table["Year"] == 2011]  #creating a new table which contains all 2011 year records
print(SalesofYear2011)

#SalesMonthWise = SalesofYear2011.groupby('Month').sum()['Amount'] # using pandas to group the data on the basis of Month and we perform
# the sum of Amount
#print(SalesMonthWise)
#
#plt.plot(SalesMonthWise.index, SalesMonthWise.values)
# plt.xlabel("Years")
# plt.ylabel("Sales")
# plt.title("Sales of Year 2011")
# #plt.show()

# print("Lowest sales: ",SalesMonthWise.min(),"Index is : ",SalesMonthWise.idxmin())
# print("Maximm Sales", SalesMonthWise.max(),"Index is:",SalesMonthWise.idxmax())

print("2. Writing the Barchart---->")
#plt.bar(SalesMonthWise.index, SalesMonthWise.values,color="red")
# plt.xlabel("Years")
# plt.ylabel("Sales")
# plt.title("Sales of Year 2011")
# plt.show()

print("3.Creating a PieChart---->")

SalesCountryWise = SalesofYear2011.groupby('Country').sum()["Amount"]
#plt.pie(SalesCountryWise.values,labels=SalesCountryWise.index,autopct="%1.1f%%") # creating a grouped according to the Country
plt.show()

print("4.Creating Scatter plot---->")

SalesInvoiceWise = SalesofYear2011.groupby('InvoiceNo').sum()['Amount']
plt.scatter(SalesInvoiceWise.values,SalesInvoiceWise.values)
plt.grid(True)
plt.show()