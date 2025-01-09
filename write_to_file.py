# Set the default file name
default_file_name = "Toshith.txt"

# Get the text from the user
text = input("Enter the text you want to write to the file: ")

# Open the file in write mode ('w')


with open(default_file_name, 'w') as file_object:

# Write the user's text to the file


   file_object.write(text)

print("Data has been added to", default_file_name)