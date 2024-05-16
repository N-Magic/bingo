from yattag import Doc
import random

file_name = "input.in"

# Initialize an empty array to store the lines
lines = []

# Open the file and read its contents
with open(file_name, 'r') as file:
    # Read each line in the file
    for line in file:
        # Remove newline characters and any leading/trailing whitespace
        clean_line = line.strip()
        # Append the cleaned line to the array
        lines.append(clean_line)

# Define the method to define a new array
def define_new_array():
    # Get the number of lines
    num_lines = len(lines)
    
    # Determine how many random lines to select (in this case, 25)
    num_random_lines = 25
    
    # Check if there are enough lines to select from
    if num_random_lines > num_lines:
        raise ValueError("Not enough lines to select from")
    
    # Shuffle the lines array in place
    random.shuffle(lines)
    
    # Select the first num_random_lines from the shuffled lines
    random_lines = lines[:num_random_lines]
    
    # Initialize a 5x5 array
    new_array = []
    for i in range(5):
        row = []
        for j in range(5):
            # Add a random line to each cell of the array
            row.append(random_lines[i * 5 + j])
        new_array.append(row)
    
    return new_array

# Dimensions of the grid layout
num_rows = 2  # Number of rows
num_cols = 3  # Number of columns

# Create a Yattag Doc instance
doc, tag, text = Doc().tagtext()

# Start HTML document
doc.asis('<!DOCTYPE html>')
with tag('html'):
    with tag('head'):
        with tag('title'):
            text('3x2 Grid of 5x5 Grids Example')
        with tag('style'):
            # Set the width and height of each individual grid to 5 inches and 3 inches respectively, with a maximum of 20% of the available space
            text('.grid { width: 5in; height: 3in; float: left; margin: 5px; overflow: hidden; font-size: 12px; }')
            text('.grid table { width: 100%; height: 100%; table-layout: fixed; border-collapse: collapse; }')
            text('.grid tr { max-width: 20%; max-height: 20%; border: 1px solid black; text-align: center; overflow: hidden; text-overflow: ellipsis; }')
            text('.grid td { max-width: 20%; max-height: 20%; border: 1px solid black; text-align: center; overflow: hidden; text-overflow: ellipsis; }')
            text('.clear { clear: both; }')
    with tag('body'):
        for row in range(num_rows):
            with tag('div', klass='grid-row'):
                for col in range(num_cols):
                    with tag('div', klass='grid'):
                        with tag('table'):
                            new_array = define_new_array()
                            for sub_row in new_array:
                                with tag('tr'):
                                    for cell in sub_row:
                                        with tag('td'):
                                            text(str(cell))
            # Clear the float after each row to maintain the grid structure
            with tag('div', klass='clear'):
                pass

# Get the rendered HTML
html_output = doc.getvalue()

# Save HTML output to a file
with open('grid_output.html', 'w') as file:
    file.write(html_output)

print("HTML output saved to grid_output.html")
