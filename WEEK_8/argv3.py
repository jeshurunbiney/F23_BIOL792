import sys
import re

# Check if the correct number of command-line arguments is provided
#if len(sys.argv) != 3:
 #   print("Usage: python process_fasta.py input_file output_file")
  #  sys.exit(1)

# Get the input and output file names from command-line arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# Initialize variables for summary information
total_sequences = 0
total_length = 0
total_GC_count = 0

# Open the input file for reading
with open(input_file, 'r') as infile:
    # Open the output file for writing
    with open(output_file, 'w') as outfile:
        # Process the file line by line
        for line in infile:
            # Remove newline characters
            line = line.strip()

            # Check if the line starts with ">"
            if re.search("^>", line):
                # If it's an ID line, write it to the output file
                outfile.write(line + '\n')
            else:
                # If it's a sequence line, calculate and write the required information
                sequence_length = len(line)
                GC_count = line.count('G') + line.count('C')

                # Write the length and GC content to the output file
                outfile.write(f"Length: {sequence_length}, GC content: {GC_count / sequence_length:.2%}\n")

                # Update running totals
                total_sequences += 1
                total_length += sequence_length
                total_GC_count += GC_count

# Calculate average GC content
average_GC_content = total_GC_count / total_length if total_length > 0 else 0

# Print summary information to the screen
print("Total DNA sequences:", total_sequences)
print("Average GC content:", f"{average_GC_content:.2%}")

# Append summary information to the output file
with open(output_file, 'a') as outfile:
    outfile.write(f"\nTotal DNA sequences: {total_sequences}\n")
    outfile.write(f"Average GC content: {average_GC_content:.2%}\n")

print("Summary information written to", output_file)

