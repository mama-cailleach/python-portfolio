from os import strerror
import os

srcname = input("Enter the source file name: ")
srcinput = input("Enter the source file text: ")
try:
    with open(srcname, 'wt', encoding='utf-8') as src_file:
        # Write the entire string at once - more efficient than char by char
        src_file.write(srcinput)
except IOError as e:
    print(f"Error: Cannot write to source file '{srcname}': {strerror(e.errno)}")
    exit(e.errno) # Exit if source file cannot be written

dicCount = {}

try:
    # Use 'with open' for automatic file closing
    # 'rt' mode: read text
    with open(srcname, 'rt', encoding='utf-8') as f:
        while True:
            char = f.read(1)  # Read one character at a time
            if not char:      # Check for End Of File (EOF)
                break

            char_lower = char.lower() # Convert to lowercase for case-insensitive counting
            # Increment count: .get(key, 0) returns 0 if key not found, else current count
            dicCount[char_lower] = dicCount.get(char_lower, 0) + 1

    # --- AMENDMENT 1: Sort histogram by character frequency (descending) ---
    # Convert dictionary items to a list of (character, count) tuples.
    # Sort this list:
    #   key=lambda item: (-item[1], item[0])
    #   -item[1]: Sorts by count (item[1]) in descending order (negative value makes bigger numbers smaller).
    #   item[0]: If counts are equal, sort alphabetically by character (item[0]) in ascending order.
    sorted_histogram_data = sorted(dicCount.items(), key=lambda item: (-item[1], item[0]))

except FileNotFoundError:
    print(f"Error: The source file '{srcname}' was not found.")
    exit(1) # Exit if source file not found
except IOError as e:
    print(f"Error reading source file '{srcname}': {strerror(e.errno)}")
    exit(e.errno)
except Exception as e:
    print(f"An unexpected error occurred while processing '{srcname}': {e}")
    exit(1)

    # --- AMENDMENT 2: Send histogram output to a new file ---

    # Construct the output histogram file name
    # os.path.splitext handles cases where srcname might already have an extension (e.g., 'doc.txt')
    # It splits 'doc.txt' into ('doc', '.txt'), so we take the base name 'doc' and add '.hist'
base_name, _ = os.path.splitext(srcname)
hist_filename = base_name + '.hist'

try:
    # Open the histogram output file in write text mode
    with open(hist_filename, 'wt', encoding='utf-8') as hist_file:
        # Iterate through the sorted data and write each line to the histogram file
        for char, count in sorted_histogram_data:
            # Format the output line for the file
            output_line = ""
            if char == '\n':
                output_line = f"'\\n' (newline): {count}\n"
            elif char == '\t':
                output_line = f"'\\t' (tab): {count}\n"
            elif char == ' ':
                output_line = f"' ' (space): {count}\n"
            else:
                output_line = f"{char}: {count}\n"

            hist_file.write(output_line)
            # You can also print to console for immediate feedback if desired
            # print(output_line, end='')


except IOError as e:
    print(f"Error: Cannot write histogram to file '{hist_filename}': {strerror(e.errno)}")
    exit(e.errno)
except Exception as e:
    print(f"An unexpected error occurred while writing histogram: {e}")
    exit(1)

