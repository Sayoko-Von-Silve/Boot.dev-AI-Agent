import os, subprocess

def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        # Will be True or False
        valid_target_file = os.path.commonpath([working_dir_abs, target_file_path]) == working_dir_abs
    except Exception as e:
        return f'Error: during working_directory/file_path check; {e}'

    if not valid_target_file:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    elif not os.path.isfile(target_file_path):
        return f'Error: "{file_path}" does not exist or is not a regular file'
    elif not target_file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file'
    else:
        try:
            command = ["python", target_file_path]
            if args:
                command.extend(args)
            completed_process = subprocess.run(command, cwd=working_dir_abs, capture_output=True, timeout=30, text=True)

            output_string = ""
            if completed_process.returncode != 0:
                output_string += f"Process exited with code {completed_process.returncode} \n"
            if not completed_process.stdout and not completed_process.stderr:
                output_string += "No output produced \n"
            if completed_process.stdout:
                output_string += f"STDOUT: {completed_process.stdout} \n"
            if completed_process.stderr:
                output_string += f"STDERR: {completed_process.stderr} \n"
            return output_string
        except Exception as e:
            return f"Error: executing Python file: {e}"
