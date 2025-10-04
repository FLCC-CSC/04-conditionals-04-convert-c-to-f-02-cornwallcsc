# FILE NAME - convert_C_to_F_02.py

# NAME: OCTAVIA CORNWALL
# DATE: OCTOBER 4, 2025
# BRIEF DESCRIPTION: CONVERT_C_TO_F



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########
print('===== Temperature Converter =====')
print()
print('  1. Convert from Celsius to Fahrenheit')
print('  2. Convert from Fahrenheit to Celsius')
print()
num = (input('Please choose from the above menu: '))
temperature = float(input('Enter a temperature to convert: '))
print()
if num == '1':
  celsius_f = temperature * 9/5 + 32
  print(f'{temperature} degrees Celsius is {celsius_f} degrees Fahrenheit.')
elif num == '2':
  fahrenheit_c = (temperature - 32) * 5/9  
  print(f'{temperature} degrees Fahrenheit is {fahrenheit_c} degrees Celsius.')
else:
  print('Invalid choice.')
########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: 32

32.0 degrees Fahrenheit is 0.0 degrees Celsius.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: -40

-40.0 degrees Fahrenheit is -40.0 degrees Celsius.
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is one lesson you learned in this lab?
Remember to cast as a float.






'''
