#!/bin/bash

# Check if there are any arguments
if [ "$#" -eq 0 ]; then
    echo "Usage: $0 file1.txt [file2.txt ...]"
    exit 1
fi

# Loop through all provided files
for file in "$@"; do
    # Check if the file exists
    if [ -e "$file" ]; then
        # Check if the file has a .txt extension
        if [[ "$file" == *.txt ]]; then
            # Convert Mac line endings to Unix line endings
            tr '\r' '\n' < "$file" > "${file%.txt}_unix.txt"
            echo "Converted $file to Unix line endings."
        else
            echo "Skipping $file: Not a .txt file."
        fi
    else
        echo "Skipping $file: File not found."
    fi
done

