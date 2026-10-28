import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        # Will be True or False
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
    except Exception as e:
        return f'Error: during working_directory/directory check; {e}'

    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'    
    elif not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    else:
        info = "Files in directory:\n"
        try:
            items = os.listdir(target_dir)
            if not items:
                info += "No files found in directory."
                return f'Success: "{directory}" is within the working directory\n\n{info}'
            for item in items:
                info += f'{item}: file_size={os.path.getsize(os.path.join(target_dir, item))} bytes, is_dir={os.path.isdir(os.path.join(target_dir, item))}\n'
            info = info[:-1] # Remove the last newline character
        except Exception as e:
            return f'Error: during listing files in directory; {e}'
        return f'Success: "{directory}" is within the working directory\n\n{info}'