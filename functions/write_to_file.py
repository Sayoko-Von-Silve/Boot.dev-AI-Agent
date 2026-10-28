import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        # Will be True or False
        valid_target_file = os.path.commonpath([working_dir_abs, target_file_path]) == working_dir_abs
    except Exception as e:
        return f'Error: during working_directory/file_path check; {e}'

    if not valid_target_file:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    elif os.path.isdir(target_file_path):
        return f'Error: Cannot write to "{file_path}" as it is a directory'
    else:
        try:
            os.makedirs(os.path.dirname(target_file_path), exist_ok=True)
        except Exception as e:
            return f'Error: During os.makedirs to target filepath; {e}'
        
        try:
            with open(target_file_path, "w") as f:
                f.write(content)
        except Exception as e:
            return f'Error: During file_path opening and content writing; {e}'

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'