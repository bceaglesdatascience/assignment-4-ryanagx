

def add_tax(itemList, salesTax):
    taxedList = []
    for cost in itemList:
        taxedCost = cost * (1 + salesTax)
        taxedList.append(taxedCost)
    return taxedList

purchases = int(input("Number of purchases: "))
salesTaxRate = float(input("Sales tax: "))
customerNames = []
itemCosts = []
for i in range(purchases):
    customerName = input("Customer: ")
    cost = float(input("Cost: "))
    customerNames.append(customerName)
    itemCosts.append(cost)
taxedCosts = add_tax(itemCosts, salesTaxRate)
customerTotals = {}
for i in range(purchases):
    customerName = customerNames[i]
    totalCost = taxedCosts[i]
    totalCost = round(totalCost,1)
    if customerName not in customerTotals:
        customerTotals[customerName] = totalCost
    else:
        customerTotals[customerName] += totalCost

print(customerTotals)
   
