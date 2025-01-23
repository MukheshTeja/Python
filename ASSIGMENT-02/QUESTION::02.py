print("Assignment ::02 Question::02")
dict_items = {}
num = int(input("Enter the number of products needed in the dictionary: "))
for i in range(num):
    key = input("Enter the product name: ")
    value = int(input("Enter the price of the product: "))
    dict_items[key] = value
print("\nDictionary of Products and Prices:", dict_items)
print("\nFrom the above list, choose a product name to get its price:")
choice = input("Enter the product name: ")
print("Press 1 to find the price or press 0 to end the search")
loop_choice = int(input("Enter the option here: "))
while loop_choice == 1:
    if choice in dict_items:
        print(f"The price of {choice} is: {dict_items[choice]}")
    else:
        print("Product not found. Please try again.")
    loop_choice = int(input("\nPress 1 to search again or 0 to end the search: "))
    if loop_choice == 1:
        choice = input("Enter the product name: ")
print("Search ended. Thank you!")
