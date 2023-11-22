#!/bin/bash

# Check for the correct number of arguments
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 input_file output_file"
    exit 1
fi

# Convert Mac line endings to Unix line endings
tr '\r' '\n' < "$1" > "$2"

echo "Conversion complete."

