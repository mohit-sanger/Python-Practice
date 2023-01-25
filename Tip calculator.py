# WElcome to tip calculator
# what was total bill? eg $124.56
# what percentage tip would you like to give? 10,12, or 15? eg 12
# How many people to split bill?eg 7
# Each person should pay: $19.93

a = float(input('please enter the bill amount'))
b = int(input('Please choose bill tip percentage 10%,12% or 15%'))
c = int(input('Please enter number of people to split the bill'))
d = (a*((b/100)+1))/c
print(f'Your Total bill is ${a},tip percent added by you is{b}%, no. of people the bill need to split is{c} '
      f'and Each person shuld pay:$ {round(d,2)}')