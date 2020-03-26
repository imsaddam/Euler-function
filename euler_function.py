def calculate_euclid_algorithm(number1,number2): #Function for Algorithm
  if number1 == 0:
    return number2
  elif number2 == 0 :
    return number1;    
  reminder = number1%number2; #Check the Reminder
  return calculate_euclid_algorithm(number2,reminder) # Return Function value


def euler_function(n):
  counter = 1
  for i in range(2, n):
    if calculate_euclid_algorithm(i, n) == 1:
      counter+=1
  return counter


n = int(input("Enter your number ="))
euler_function(n)
