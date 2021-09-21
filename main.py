cupcakes = open("CupcakeInvoices.csv")

for row in cupcakes:
  print(row) 

cupcakes = open("CupcakeInvoices.csv")

# for row in cupcakes:
#   values = row.split(',')
#   print(values[2])

# for row in cupcakes:
#   values = row.split(',')
#   total = int(values[3]) * float(values[4])
  
#   print(total)

total = 0

for row in cupcakes:
  values = row.split(',')
  total = total + (int(values[3]) * float(values[4]))

  print(total)

cupcakes.close()
