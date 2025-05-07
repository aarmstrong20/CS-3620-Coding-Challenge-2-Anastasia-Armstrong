products = {
    "Olive oil" : 10.99,
    "White Vinegar": 30.99,
    "Sushi" : 20.00,
    "Pasta" : 10.99,
    "House Salad" : 15.99
}


productName = input("Enter product name: ")
print("{0} is ${1}".format(productName, products[productName]))