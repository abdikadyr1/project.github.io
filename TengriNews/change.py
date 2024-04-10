# Read the content of the CSS file
file_path = r"css\style.css"
with open(file_path, 'r') as file:
    file_content = file.read()

# Replace all occurrences of '#FF6F61' with '#32a801'
updated_content = file_content.replace('#FF6F61', '#32a801')

# Write the updated content back to the file
with open(file_path, 'w') as file:
    file.write(updated_content)

# Confirm the replacement
'All occurrences of "#FF6F61" have been replaced with "#32a801" in the file.'
