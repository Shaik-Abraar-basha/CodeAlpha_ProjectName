stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150
}

stock_name = input("Enter stock name: ").upper()
quantity = int(input("Enter quantity: "))

total_investment = stock_prices[stock_name] * quantity

print("\nStock Name:", stock_name)
print("Stock Price:", stock_prices[stock_name])
print("Quantity:", quantity)
print("Total Investment:", total_investment)

with open("portfolio_result.txt", "w") as file:
    file.write("STOCK PORTFOLIO TRACKER\n")
    file.write("-----------------------\n")
    file.write("Stock Name: " + stock_name + "\n")
    file.write("Stock Price: " + str(stock_prices[stock_name]) + "\n")
    file.write("Quantity: " + str(quantity) + "\n")
    file.write("Total Investment: " + str(total_investment) + "\n")

print("\nResult saved successfully in portfolio_result.txt")