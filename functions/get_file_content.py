import os
from config import FILE_MAX_CHARS_LIMIT

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        # Will be True or False
        valid_target_file = os.path.commonpath([working_dir_abs, target_file_path]) == working_dir_abs
    except Exception as e:
        return f'Error: during working_directory/file_path check; {e}'

    if not os.path.isfile(target_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    if not valid_target_file:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    else:
        content = ""
        try:
            with open(target_file_path, "r") as f:
                content += f.read(FILE_MAX_CHARS_LIMIT)
                if f.read(1):
                    content += f'[...File "{file_path}" truncated at {FILE_MAX_CHARS_LIMIT} characters]'
        except Exception as e:
            return f'Error: During file_path opening and content reading/appending; {e}'
        return content