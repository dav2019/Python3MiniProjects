hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# 1
total_price = 0

# 2
for price in prices:
  total_price += price
# print(total_price)

# 3
average_price = total_price / len(prices)
# print(average_price)

# 4
print("Average Haircut Price: " + str(average_price))

# 5
new_prices = [price - 5 for price in prices]

# 6
print(new_prices)

# 7 
total_revenue = 0

# 8, 9
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]

# 10
print(total_revenue)

# 11
average_daily_revenue = total_revenue / 7

# 12
cuts_under_30 = []
for i in range(len(hairstyles)):
  if new_prices[i] < 30:
    cuts_under_30.append(hairstyles[i])

print(cuts_under_30)