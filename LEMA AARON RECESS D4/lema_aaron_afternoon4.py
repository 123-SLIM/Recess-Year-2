# Exception handling

try:
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))
    
    result = num1 / num2
    
    print("Ths result is:", result)
except ValueError:
    print("Invalid input. Please enter valid integers.")

except ZeroDivisionError:
    print("Error: Division by zerois not allowed")

except Exception as e:
    print("An error occured:", str(e))
    
    
    # File Handling
    
    # Writing to a file
    file_path = "example.txt"
    
    # open the file in write mode
    
    with open(file_path, "w") as file:
        file.write("Hello, Aaron !\n")
        file.write("This is an examle file.\n")
        file.write("Writing to a file in python.\n")
        
        print("File write operation completed.")
        
        # reading file
        with open(file_path, "r") as file:
            
            # read the entire contents of the file
            contents = file.read()
            
            print("File contents:")
            print(contents)
            
    
