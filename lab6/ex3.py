import os
import sys


def calculate_total_size(directory_path):
    total_size = 0

    try:
    
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"Directory not found: {directory_path}")

        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                
                try:
                    file_size = os.path.getsize(file_path)
                    total_size += file_size
                except Exception as e:
                    print(f"Error getting size of file '{file_path}': {str(e)}")

        print(f"Total size of all files in '{directory_path}': {total_size} bytes")

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]

    calculate_total_size(directory_path)
