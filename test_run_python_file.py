from functions.run_python_file import run_python_file

print("Running test...\n")

testcase = [
    "main.py",
    ["main.py", ["3 + 5"]],
    "tests.py",
    "../main.py",
    "nonexistent.py",
    "lorem.txt"
]

for case in testcase:
    print(f'File: {case}\n---------------------------------------\n')
    if isinstance(case, list):
        result = run_python_file("calculator", case[0], case[1])
    else:
        result = run_python_file("calculator", case)
    print(result)
    print('\n---------------------------------------\n\n')

print("Test completed.\n")
