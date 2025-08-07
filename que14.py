#14. Build a dictionary where the keys are product names and the values are their prices.
#Implement options to:
#a. Add a new product
#b. Update price of an existing product
#c. Find products within a given price range

print("╔════════════════════════════════════════╗")
print("║          PRODUCT OPERATION             ║")
print("╠════════════════════════════════════════╣")
print("║ 1. Add a new product                   ║")
print("║ 2. Update price of an existing product ║")                         ║")
print("║ 3. Find products with price range      ║")
print("║ 4. Exit                                ║")
print("╚════════════════════════════════════════╝")
while True:
 choice=int(input("Enter the choice:\n"))
 if choice==1:
    product_name=input("Enter the product name: ")
    prices=int(input(f"Enter the price for '{product_name}'"))
    d={}
    d[product_name]=prices
 

