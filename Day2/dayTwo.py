'''
#### Exercise
You are building a program to help a user decide what to wear based on the current weather conditions. Write a Python program that prompts the user to enter the current temperature in Fahrenheit and whether it is currently raining or not (as a boolean value), and then suggests an appropriate outfit based on the following criteria:

If the temperature is less than 50 degrees Fahrenheit, suggest wearing a coat, hat, scarf, and gloves.
If the temperature is between 50 and 70 degrees Fahrenheit and it is not raining, suggest wearing a sweater or light jacket.
If the temperature is between 50 and 70 degrees Fahrenheit and it is raining, suggest wearing a rain jacket and boots.
If the temperature is above 70 degrees Fahrenheit and it is not raining, suggest wearing a t-shirt and shorts.
If the temperature is above 70 degrees Fahrenheit and it is raining, suggest wearing a light jacket and rain boots.

'''
def weatherApp(temperature,raining):
    #If the temperature is less than 50 degrees Fahrenheit, 
    # suggest wearing a coat, hat, scarf, and gloves.

    if temperature < 50:
        print('I suggest you wear a coat, hat, scarg and gloves')
    elif temperature >50 and temperature <70 and raining == 1:
        print("I suggest you wear a sweater or light jacket.")
    
    else:
        print("Don't go outside")



if __name__ == "__main__":
    temperature = int(input("What is the Temperature Outside in Fahrenheit: "))
    raining = int(input("Is it Raining? \n 1 for Yes \n 0 for  No: "))
    weatherApp(temperature,raining)



