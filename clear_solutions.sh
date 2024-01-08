#!/bin/bash

DOCS="
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

This script clears solutions from the /src folder so you can solve them yourself.

  -h, --help       Show this message and exit
  -p, --python     Clear all Python solutions in /src
  -c, --cpp        Clear all C++ solutions in /src
  -r, --readme     Clear all challenge READMEs for the selected language(s)

If no options are passed, this message will be displayed and the script will exit.

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

"

### ======== parse CLI options ======== ###

# Read flags to decide which solutions to clear
clear_python=0
clear_cpp=0
clear_readmes=0
help=0

while [[ $# -gt 0 ]]; do
  case $1 in
  -p | --python)
    clear_python=1
    shift # past argument
    ;;
  -c | --cpp)
    clear_cpp=1
    shift # past argument
    ;;
  -r | --readme)
    clear_readmes=1
    shift # past argument
    ;;
  -h | --help)
    help=1
    shift # past argument
    ;;
  -* | --*)
    printf "\n>>>>>     Unknown option $1     <<<<<\n"
    printf "$DOCS"
    exit 1
    ;;
  *)
    shift # past argument
    ;;
  esac
done

# Print the docs and exit if help, or no language selected
if [ $help == 1 ] || ([ $clear_python == 0 ] && [ $clear_cpp == 0 ]); then
  printf "$DOCS"
  exit 1
fi

### ======== give user fair warning, last chance to exit ======== ###

# Display a warning and ask the user if they want to continue
WARNING='\n!!WARNING!! Are you sure you want to delete all solutions '
if [ $clear_readmes == 1 ]; then
  WARNING+='and READMES '
fi
WARNING+='for: \n\n'
if [ $clear_python == 1 ]; then
  WARNING+="   Python  \n\n"
fi
if [ $clear_cpp == 1 ]; then
  WARNING+="   C++   \n\n"
fi
printf "$WARNING"
echo "This will delete all of your work. Enter 'yes' to continue, anything else to exit: "
read answer

# If the user does not want to continue, exit the script
if [[ "$answer" != "yes" ]]; then
  echo "Ok! Exiting without clearing any solutions."
  exit 1
fi

### ======== clear solutions for the selected language(s) ======== ###

# Change to the solutions directory because of hard-coded search logic
cd 'src'

# Find all directories that match the pattern
for dir in $(find . -type d -name 'src'); do
  # Skip C++ directories if they were not selected
  if [ $clear_cpp == 0 ] && [ $(basename $(dirname "$(dirname "$dir")")) == 'cpp' ]; then
    continue
  fi
  # Skip Python directories if they were not selected
  if [ $clear_python == 0 ] && [ $(basename $(dirname "$(dirname "$dir")")) == 'python' ]; then
    continue
  fi

  # Clear READMEs so new solutions can be documented
  if [ $clear_readmes == 1 ] && [ "$dir/../README.md" ]; then
    truncate -s 0 "$dir/../README.md"
  fi

  echo "src: $dir"

  # Find all files in the directory
  for file in $(find $dir -type f); do

    # Get the grandparent directory
    grandparent=$(dirname "$(dirname "$file")")
    # Get the name of the grandparent directory
    grandparent_name=$(basename "$grandparent")
    # Get the name of the file without the extension
    file_name_without_extension=$(basename "${file%.*}")

    # Clear files whose name (without the extension) matches the grandparent name
    if [[ "$file_name_without_extension" == "$grandparent_name" ]]; then
      truncate -s 0 "$file"
    fi

    # Delete pychaches if the use selected Python
    if [ $clear_python == 1 ]; then # in case there's a pycache in a cpp folder, who knows?
      for dir in $(find . -type d -name "__pycache__"); do
        # Delete the directory
        rm -rf $dir
      done
    fi
  done
done

printf "\n\nAll done! Your turn to pass the tests and document your solutions.\n"
