#!/bin/bash

# Loop through all JPEG files in the directory
for file in *.jpg; do
    # Check if the file is a regular file
    if [[ -f "$file" ]]; then
        # Run the convert command on each file
        convert "$file" -background white -gravity center -extent 148x148 "${file}"
    fi
done
 
