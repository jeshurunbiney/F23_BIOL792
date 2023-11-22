import sys

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 3:
    print("Usage: python script.py input_file output_file")
    sys.exit(1)

# Get the input and output file names from command-line arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# Create an empty list to store the flying time for night-time values
night_flying_time = []

# Open the input file for reading
with open(input_file, 'r') as infile:
    # Open the output file for writing
    with open(output_file, 'w') as outfile:
        # Read the input file line by line
        for line in infile:
            # Split each line into a list using whitespace as the delimiter
            columns = line.split()
            
            # Check if the second column is 'N' (night-time)
            if len(columns) >= 2 and columns[1] == 'N':
                # If it's night-time, append the flying time (third column) to the night_flying_time list
                night_flying_time.append(columns[2])
        
        # Write the night flying times to the output file, one per line
        outfile.write('\n'.join(night_flying_time))

print("Night-time flying times written to", output_file)

