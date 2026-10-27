from functions.get_file_content import get_file_content

print("Running test...\n")

testcase = [
    "lorem.txt",
    "main.py",
    "pkg/calculator.py",
    "/bin/cat",
    "pkg/does_not_exist.py",
]

for case in testcase:
    print(f'File: {case}\n---------------------------------------\n')
    result = get_file_content("calculator", case)
    if result.startswith("Error:"):
        print(result)
    elif len(result) < 10000:
        print(result)
    else:
        print(f"{case} length: {len(result)}")
        print(f"{case} truncated: {'truncated' in result}")
    print('\n---------------------------------------\n\n')

print("Test completed.\n")
