from functions.get_files_info import get_files_info

print("Running tests...\n")
print(f"#1: {get_files_info("calculator", ".")}\n")
print(f"#2: {get_files_info("calculator", "pkg")}\n")
print(f"#3: {get_files_info("calculator", "/bin")}\n")
print(f"#4: {get_files_info("calculator", "../")}\n")
print("Tests completed.\n")
