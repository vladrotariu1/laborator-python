import os
import sys


def count_files_by_extension(directory_path):
    try:
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"Directory not found: {directory_path}")

        if not os.listdir(directory_path):
            raise ValueError(f"Directory is empty: {directory_path}")

        extension_counts = {}

        for filename in os.listdir(directory_path):
    
            if os.path.isfile(os.path.join(directory_path, filename)):
                _, file_extension = os.path.splitext(filename)
                extension_counts[file_extension] = extension_counts.get(file_extension, 0) + 1

        print("File extension counts:")
        for extension, count in extension_counts.items():
            print(f"{extension}: {count} files")

    except FileNotFoundError as e:
        print(f"Error: {str(e)}")
    except PermissionError as e:
        print(f"Error: Permission denied - {str(e)}")
    except ValueError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]

    count_files_by_extension(directory_path)
