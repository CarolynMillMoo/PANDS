#This program will take in a quantity of money in dollar and cents and convert it to cents in its absolut value
#Author: Carolyn Moorhouse

money = float(input('Please enter an amount in dollars and cents:'))
absoluteValueMoney = abs(money*100)
print('That amount in cents is: {}'.format(absoluteValueMoney))

