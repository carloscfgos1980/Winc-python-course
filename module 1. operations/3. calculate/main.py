# Do not modify these lines
__winc_id__ = '499e67d5cb54448e93cee7465be2c866'
__human_name__ = 'calculate'

# Add your code after this line
broccoli = 2
leek = 2
potato = 3
brussel_sprout = 7

# Calculate the total cost if you were to buy one of each
sum_one_each = broccoli + leek + potato + brussel_sprout


# Calculate the average price per item
avg_price = sum_one_each / 4


# Several Items price
num_potatoes = potato * 7
num_broccolis = broccoli * 5
num_leeks = leek * 2
num_brussel_sprouts = brussel_sprout * 10


# Calculate the sum total
sum_total = num_potatoes + num_broccolis + num_leeks + num_brussel_sprouts


# 30% Disccount
discount_percentage = 30 / 100

# Sum total 30 %
sum_total_30 = sum_total * discount_percentage


# Calculate the amount owed
discounted_sum_total = sum_total - sum_total_30
# using built-in function: rond to decide how much units after the colon (,)
rond_total = round(discounted_sum_total, 1)

print(rond_total)
