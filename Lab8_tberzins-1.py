"""UPC Validator
Tali Berzins
To validate a 12-digit UPC-A code
03/04/2026"""
#Asking user for UPC number then outputting the first 11 digits and the check digit
upc_number = input("Enter a 12-digit UPC number")
upc_input = upc_number[:-1]
print(f'The first 11 digits are {upc_input}')
print(f'The provided check digit is {upc_number[-1]}')

#Defining function to check expected check digit
def find_UPC(upc_input: str):
    print("Calculating...")
    total = 0
    for i in range(len(upc_input)):
        print(i)
        input_digit = int(upc_input[i])
        print(input_digit)
#Checking if digit is at an odd or even position, note odds are actually evens because index starts at zero rather than 1 
        if(i%2 ==0):
            total += input_digit
        else:
            total += (input_digit*3)
        i +=1 
    
    print(total)

        

find_UPC(upc_input)
