import os
import time
import datetime


def get_absolute_paths(folder_path):
    absolute_paths = []

    for folder_name, sub_folders, file_names in os.walk(folder_path):
        absolute_paths.append(os.path.abspath(folder_name))
        for file_name in file_names:
            file_path = os.path.join(folder_name, file_name)
            absolute_paths.append(os.path.abspath(file_path))

    return absolute_paths


def diff_file_history(initial_absolute_paths_array, monitored_location, last_diff_time):
    updated_absolute_paths = get_absolute_paths(monitored_location)
    new_items = [
        (path, os.stat(path).st_ctime)
        for path in updated_absolute_paths
        if path not in initial_absolute_paths_array
    ]
    deleted_items = [
        (path, time.time())
        for path in initial_absolute_paths_array
        if path not in updated_absolute_paths
    ]

    modified_files = [
        (path, os.stat(path).st_mtime)
        for path in updated_absolute_paths
        if os.path.isfile(path) and os.stat(path).st_mtime > last_diff_time
    ]
    accessed_files = [
        (path, os.stat(path).st_atime)
        for path in updated_absolute_paths
        if os.path.isfile(path) and os.stat(path).st_atime > last_diff_time]

    return {
        'new': new_items,
        'deleted': deleted_items,
        'modified': modified_files,
        'accessed': accessed_files
    }


def write_actions(*action_items):
    for action_item in action_items:
        action_type = action_item[0]
        items_array = action_item[1]

        for item in items_array:
            path = item[0]
            timestamp = item[1]
            item_type = 'dir' if os.path.isdir(path) else 'file'
            write_in_history(action_type, item_type, path, timestamp)


def write_in_history(action_type, item_type, item_path, timestamp):
    now_date = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    history_line = f"{now_date}: {action_type} {item_type} {item_path}\n"

    print(history_line)

    with open('actions_history.txt', 'a') as history_file:
        history_file.write(history_line)


if __name__ == "__main__":
    monitored_location = 'testdir/'
    current_absolute_paths_array = get_absolute_paths(monitored_location)

    last_diff_time = time.time()

    while True:
        diff_result = diff_file_history(current_absolute_paths_array, monitored_location, last_diff_time)
        last_diff_time = time.time()
        current_absolute_paths_array = get_absolute_paths(monitored_location)

        write_actions(*diff_result.items())

        time.sleep(5)
