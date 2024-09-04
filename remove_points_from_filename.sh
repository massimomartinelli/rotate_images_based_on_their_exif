#!/bin/bash

# Find all files in the current directory and subdirectories
find /home/user/MYDIR/ -type f | while read -r file; do   # CHANGE THE DIRECTORY
  # Extract the extension and filename
  extension="${file##*.}"
  filename="${file%.*}"

  # Remove all dots from the filename  (apart the one before the extension of course)
  clean_filename="${filename//./}"

  # Construct the new filename
  new_file="$clean_filename.$extension"

  # Rename the file if the new filename is different
  if [ "$file" != "$new_file" ]; then
    mv "$file" "$new_file"
  fi
done
