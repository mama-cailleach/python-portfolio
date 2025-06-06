allNumbers = [
'''

###
# #
# #
# #
###
''',
'''

  #
  #
  #
  #
  #
''',
'''

###
  #
###
#  
###
''',
'''

###
  #
###
  #
###
''',
'''

# #
# #
###
  #
  #
''',
'''

###
#  
###
  #
###
''',
'''

###
#  
###
# #
###
''',
'''

###
  #
  #
  #
  #
''',
'''

###
# #
###
# #
###
''',
'''

###
# #
###
  #
###
''']


number = input("Input number: ", )

def numberprint(number):
    drawn_number_lines = []
    for i in number:
        j = int(i)
        drawn_number_lines.append(allNumbers[j].split('\n'))

    # Determine the height of the numbers (number of lines in each character)
    # Assuming all drawn numbers have the same height
    if drawn_number_lines:
        num_lines_per_char = len(drawn_number_lines[0])
    else:
        num_lines_per_char = 0 # Handle case where 'number' is empty

    # 2. Iterate through each line (row) of the multi-character display
    for line_idx in range(num_lines_per_char):
        # 3. For each line_idx, iterate through all the drawn numbers
        for char_lines in drawn_number_lines:
            # Print the current line segment of the current character
            # Add two spaces for separation between characters
            print(char_lines[line_idx], end="  ")
        # After printing one segment from ALL characters, move to the next line
        print() # This print() adds a newline character

numberprint(number)