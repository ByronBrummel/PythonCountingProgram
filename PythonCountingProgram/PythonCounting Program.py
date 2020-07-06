print('Counting Program')

# Ask user for name
name = input('Your name? ').capitalize()

print('Hi there, ' + name)

while True:
# Ask user for a number and turn number into integer
  try:
    number=int(input('Enter a number? '))
    break
  except ValueError:
    print('Sorry numbers only')  
# limit number to range of 3-100
while number not in range(3,101):
  print('Your number has to be in range of 3 to 100')
  number=int(input('Enter a number? '))
# create a loop starting from 0 until user number
input('press Enter and I will count by twos to ' + str(number) + '.')
for i in range(0, number+1, 2):
  print(i)