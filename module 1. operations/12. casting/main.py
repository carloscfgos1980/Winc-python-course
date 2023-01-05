# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line

# PART 1
leek_price = 2
print('Leek is' + ' ' + str(leek_price) + ' ' + 'euro per kilo.')

# PART 2
order_01 = 'leek 4'
leek_amount = int(order_01[order_01.find(' ') + 1:])
sum_total = leek_amount * leek_price
print(sum_total)

# PART 3
broccoli_price = 2.34
order_02 = 'broccoli 1.6'
# string like 1.6 cannot be directly converted to number (inter). So first it needs to be converted to a float and then to an inter
broccoli_amount = float(order_02[order_02.find(' ') + 1:])

broccoli_total_price = round((broccoli_price * broccoli_amount), 2)
'''
print('total price', broccoli_total_price)
'''
print(str(broccoli_amount) + 'kg' + ' ' +
      'broccoli costs' + ' ' + str(broccoli_total_price) + 'e')
