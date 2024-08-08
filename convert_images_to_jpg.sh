#!/bin/bash

#####################################
# convert_images_to_jpg    v1.0 2024/08/08
# massimo martinelli  
#####################################

# sudo apt install imagemagick

# Define the directory name variable
DIRNAME="/path/to/your/directory"

# Loop through each .jpeg file in the specified directory
for file in "$DIRNAME"/*.jpeg; do
  # Check if the file exists to avoid errors
  if [[ -f "$file" ]]; then
    # Copy the file with a new extension
    cp "$file" "${file%.jpeg}.jpg"
    # Remove the original file  # mv can generate issues...
    rm "$file"
  fi
done


for file in "$DIRNAME"/*.jfif; do
  # Check if the file exists to avoid errors
  if [[ -f "$file" ]]; then
    # convert the file with a new extension
    convert "$file" "${file%.jpeg}.jpg"
    # Remove the original file
    rm "$file"
  fi
done


for file in "$DIRNAME"/*.png; do
  # Check if the file exists to avoid errors
  if [[ -f "$file" ]]; then
    # convert the file with a new extension
    convert "$file" "${file%.png}.jpg"
    # Remove the original file
    rm "$file"
  fi
done



###################àà
#function iterateinsubdirectories() {
#    local dir="$1"
#    for entry in "$dir"/*; do
#        if [ -d "$entry" ]; then
#            echo "$entry"
#            iterateinsubdirectories "$entry"  # Recursively iterate into subdirectories
#        fi
#    done
#}

# Start from the specified directory
#iterateinsubdirectories "$DIRNAME"
