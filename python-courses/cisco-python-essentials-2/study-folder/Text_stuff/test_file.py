from os import strerror

def process_student_points(filename):
    """
    Reads a file containing student names and points,
    calculates the total points for each student,
    and prints a sorted report.
    """
    student_points = {} # Dictionary to store total points for each student
                        # Key: "FirstName LastName" (string)
                        # Value: Total points (float)

    print(f"\n--- Processing file: '{filename}' ---")

    try:
        # Use 'with open' for safe and automatic file handling
        # 'rt' for read text mode, encoding='utf-8' is a good standard
        with open(filename, 'rt', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1): # Enumerate to get line number for error reporting
                # Remove leading/trailing whitespace (including newlines)
                # and non-breaking spaces (U+00A0) which often look like regular spaces
                cleaned_line = line.replace('\xa0', ' ').strip()

                if not cleaned_line: # Skip empty lines
                    continue

                # Split the line by any whitespace (handles multiple spaces between words)
                parts = cleaned_line.split()

                # Basic validation for expected number of parts
                if len(parts) < 3: # Expect at least first name, last name, and points
                    print(f"Warning: Skipping malformed line {line_num} in '{filename}': '{line.strip()}' (Expected at least 3 parts)")
                    continue

                # Extract data: First name, Last name, and Points
                # Handle cases where names might have multiple parts (e.g., "Mary Jo Smith")
                try:
                    # Assume points is always the last part
                    points_str = parts[-1]
                    points = float(points_str)

                    # The rest are name parts. Combine them into a full name.
                    # This handles names like "Andrew Cox" or "Anna Boleyn" but also "John van der Smith"
                    full_name = " ".join(parts[:-1]) # Join all parts except the last one (points)

                except ValueError:
                    print(f"Warning: Skipping line {line_num} in '{filename}': Could not convert points '{points_str}' to a number.")
                    continue
                except Exception as e: # Catch any other parsing issues
                    print(f"Warning: Skipping line {line_num} in '{filename}': Error parsing line '{line.strip()}': {e}")
                    continue

                # Aggregate points for the student
                # Use .get() to safely add to existing total or start a new total
                student_points[full_name] = student_points.get(full_name, 0.0) + points

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return # Exit function if file not found
    except IOError as e:
        print(f"Error reading file '{filename}': {strerror(e.errno)}")
        return # Exit function on other I/O errors
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return # Exit function on other unexpected errors

    # --- Print the sorted report ---
    if not student_points:
        print("No student data found or processed.")
        return

    print("\n--- Student Points Report ---")

    # Sort the report by student full name (alphabetically)
    # The example output shows sorting by full name.
    sorted_students = sorted(student_points.keys())

    for student_name in sorted_students:
        total_points = student_points[student_name]
        # Format the output to match the example (e.g., 7.0 for whole numbers)
        print(f"{student_name} {total_points:.1f}") # .1f ensures one decimal place

# --- Main program execution ---
if __name__ == "__main__":
    file_name = input("Enter the name of the file to analyze (e.g., samplefile.txt): ")
    process_student_points(file_name)