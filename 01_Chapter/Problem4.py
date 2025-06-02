import os

# Specify the directory path (you can change this or use input())
directory = input("Enter the directory path: ")

# Check if the path is valid
if os.path.exists(directory):
    print(f"\nContents of '{directory}':\n")
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            print(f"File: {item}")
        elif os.path.isdir(item_path):
            print(f"Directory: {item}")
        else:
            print(f"Other: {item}")
else:
    print("The specified directory does not exist.")
