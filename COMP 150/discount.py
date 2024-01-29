x= float(input("Enter the original price of an item: "))
y= float(input("Enter the percent being discounted: "))

discountPrice= (1-y/100)*x
print(format(discountPrice,'.2f'))