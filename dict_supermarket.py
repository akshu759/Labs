#A Dictionary representing products and their prices in a supermarket
#Each product in a supermarket is associated with its price.

supermarket_prices= {
    "cheese":100,
    "milk": 70,
    "bread": 60,
    "yoghurt":45,
    "potato":120
}

#Accessing the price of a specific product
print("The price of milk is Rs:",supermarket_prices["milk"])

#adding a new product with its price
supermarket_prices["buttermilk"]= 60

#printing the updated dictionary
print(supermarket_prices)