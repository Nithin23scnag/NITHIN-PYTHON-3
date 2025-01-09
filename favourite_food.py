# Set the default file name

file_name = input("Enter the name for the file (with .txt extension): ")

# Get the text about favourite food from the user

favorite_food = input("Type about your favourite food: ")

# Open the file in write mode ('w')

with open(file_name, 'w') as file_object:

# Write the user's text to the file

   file_object.write(favorite_food)

print("Data about your favourite food has been added to", file_name)