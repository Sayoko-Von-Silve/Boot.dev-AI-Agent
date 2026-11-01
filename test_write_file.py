from functions.write_file import write_file

print("Running test...\n")

testcase = [
    ["lorem.txt", "wait, this isn't lorem ipsum"],
    ["pkg/morelorem.txt", "lorem ipsum dolor sit amet"],
    ["/tmp/temp.txt", "this should not be allowed"],
]

for case in testcase:
    print(f'File: {case}\n---------------------------------------\n')
    result = write_file("calculator", case[0], case[1])
    print(result)
    print('\n---------------------------------------\n\n')

print("Test completed.\n")
