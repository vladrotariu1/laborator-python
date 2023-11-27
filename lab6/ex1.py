# 1)
import os
import sys

def read_files_in_directory(directory_path, file_extension):
    try:

        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"Directory not found: {directory_path}")

    
        for filename in os.listdir(directory_path):
            if filename.endswith(file_extension):
                file_path = os.path.join(directory_path, filename)
                try:
            
                    with open(file_path, 'r') as file:
                        content = file.read()
                        print(f"File: {filename}\nContent:\n{content}\n{'-'*30}")
                except Exception as e:
                    print(f"Error reading file '{filename}': {str(e)}")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: python script.py <directory_path> <file_extension>")
        sys.exit(1)

    directory_path = sys.argv[1]
    file_extension = sys.argv[2]

    read_files_in_directory(directory_path, file_extension)
