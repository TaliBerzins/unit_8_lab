"""UPC Validator
Tali Berzins
To validate a 12-digit UPC-A code
03/04/2026"""
#Asking user for UPC number then outputting the first 11 digits and the check digit
upc_number = input("Enter a 12-digit UPC number\n")
upc_input = upc_number[:-1]
print(f'The first 11 digits are {upc_input}.')
print(f'The provided check digit is {upc_number[-1]}.\n')

#Defining function to check expected check digit
def find_UPC(upc_input: str):
    print("Calculating...")
    total = 0
#For loop to run through the first 11 digits of the UPC and perform the check
    for i in range(len(upc_input)):
        input_digit = int(upc_input[i])     
#Checking if digit is at an odd or even position, note odds are actually evens in context of the actual UPC number because index starts at zero rather than 1 
        if(i%2 ==0):
            total += (input_digit*3)
            
        else:
            total += input_digit
          
        i +=1 
    
    #Calculating the expected last digit and returning it
    result_modulo: int = total%10
    print(result_modulo)
    result: int = 10 - result_modulo
    print(f"The expected check digit is {result}.\n")
    return result


        
#If statement to write output depending if last digit is valid or not
if find_UPC(upc_input) == int(upc_number[-1]):
    print("UPC is VALID")
else:
    print("UPC is INVALID")



