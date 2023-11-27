import os
import sys


def rename_files_with_sequential_prefix(directory_path):
    renaming_info = []  

    try:
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"Directory not found: {directory_path}")

        files = os.listdir(directory_path)
        files.sort()

        for index, filename in enumerate(files, start=1):
            old_path = os.path.join(directory_path, filename)
            new_filename = f"file{index}{os.path.splitext(filename)[1]}"
            new_path = os.path.join(directory_path, new_filename)

            renaming_info.append((old_path, new_path))
            print(f"Renaming: {filename} -> {new_filename}")
            
        for old_path, new_path in renaming_info:
            try:
                os.rename(old_path, new_path)
            except Exception as e:
                print(f"Error renaming file '{old_path}': {str(e)}")

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]

    rename_files_with_sequential_prefix(directory_path)
