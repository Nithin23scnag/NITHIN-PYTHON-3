# Set the name of the file to read from
file_name = "my_file.txt"

# Open the file in read mode ('r')
with open(file_name, 'r') as file_object:

   content = file_object.read()

# Print the content of the file
print("Content of the file:", content)