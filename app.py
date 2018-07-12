## FAHRENHEIT TO CELSIUS
def fahrenheit_to_celsius(input):
    print ("Fahrenheit to Celsius conversion.")
    ## Takes input as int
    fahrenheit = int(input("What is the temperature in Fahrenheit?: "))
    ##Math
    celsius = (fahrenheit - 32) * 5 / 9
    round(celsius,2)
    #Print string and celsius variable
    print ("The temperature in Celsius is: ", celsius)
    
## CELSIUS TO FAHRENHEIT           
def celsius_to_fahrenheit(input):        
    print ("Celsius to Fahrenheit conversion.")
    ## Takes input as int
    celsius = int(input("What is the temperature in Celsius?: "))
    ## Math
    fahrenheit = (1.8 * celsius) + 32
    round(fahrenheit,2)
    ##Print string and fahrenheit variable
    print ("The temperature in Fahrenheit is: ", fahrenheit)

    
    #function to select which calculator used
def select_conversion(input):
    #1 = Fahrenheit to Celsius, 2 = Celsius to Fahrenheit. Anything else returns string 'Not a valid input'.
    int(input("Which converter are you looking for?: "))
    if 1:
        return fahrenheit_to_celsius(input)
    elif 2:
        return celsius_to_fahrenheit(input)
    else:
        #if input isn't the number 1 or 2, returns string.
        return "Not a valid input."


    
## Executing functions 
if __name__ == "__main__":
    print ("SELECT CONVERSION TYPE")
    print ("FAHRENHEIT -> CELSIUS - '(1)'")
    print ("CELSIUS -> FAHRENHEIT - '(2)'")
    ##Runs select function
    print (select_conversion(input))
    #Program should continue from input to selected function.
