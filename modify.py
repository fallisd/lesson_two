input_filename = 'poem.txt'
output_filename = 'output.txt'

# store contents of input file in a list named "original_file_contents"
# This is slightly different then the last assignment. Each line in the file is being
# stored as an element in a list, not as one large string.
# Notice when the list is printed that there is an extra '\n' character at the end of each line
# this indicates a new line when the output is written to a file.
with open(input_filename, 'r') as f:
    lines = f.readlines()
print(lines)

# Open file for writing
target = open(output_filename, 'w')

# Assignment
# Read in the file from poem.txt and write the poem to output.txt with the following modifications
#   
#   1. Add a title to the poem
#   2. Capitalize the first word of every line
#   3. Indent the last two lines with four spaces
#
#   More difficult:
#   4. If the line doesn't end in punctuation add a period to the end of the line
#
#   Advanced:
#   5. Delete the repeated line
#   6. Number the lines
#   7. Add a blank line after every four lines in the poem
#    
#
# Keep in mind:
# There are many ways the modifications could be done. The solution should be as concise as possible.
# Fewer lines of code doesn't necessarily mean that the code is better, but duplicating operations that 
# could be done in a loop is inefficient while writing and it requires more time to modify the code if 
# it is duplicated in several places.
# Try to make the operations general. The operations shouldn't be specific to the words
# of just one poem but it could be applied to others without modifying the code. 
# For example: 
# When deleting the repeating line, don't just delete line 11, because the repeated line might not
# be on line 11 in another file.

#-----------------------------
# write code here
#-----------------------------

# These two lines will write a copy of the poem to output_filename.
# You can make modifications in the loop or outside the loop, depending on what is required.
# for line in lines:
#    target.write(line)

#-----------------------------
#
#-----------------------------

# Close the file
target.close()