# Script for file handling operations with error handling

# Writing to the file and reading content
try:
    # Step 1: Creating and writing to "my_file.txt"
    with open("my_file.txt", 'w') as file:
        file.write("This is the first line.\n")
        file.write("Here is the second line with a number: 12345\n")
        file.write("And finally, the third line.\n")
    print("File 'my_file.txt' created and written successfully.")
    
    # Step 2: Reading the contents of "my_file.txt"
    with open("my_file.txt", 'r') as file:
        print("\nReading the contents of 'my_file.txt':")
        content = file.read()
        print(content)
    
    # Step 3: Appending additional lines to the file
    with open("my_file.txt", 'a') as file:
        file.write("This is the fourth appended line.\n")
        file.write("The fifth line contains another number: 67890\n")
        file.write("Finally, the sixth appended line.\n")
    print("Additional lines appended successfully.")
    
    # Step 4: Reading the updated contents of "my_file.txt"
    with open("my_file.txt", 'r') as file:
        print("\nReading the updated contents of 'my_file.txt':")
        updated_content = file.read()
        print(updated_content)

# Error handling using try, except, and finally blocks
except FileNotFoundError as fnf_error:
    print(f"Error: File not found - {fnf_error}")
except PermissionError as perm_error:
    print(f"Error: Permission denied - {perm_error}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("\nFile handling operations completed.")
