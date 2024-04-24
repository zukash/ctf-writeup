print(
    'Can you help us write a docstring for our python code?\nPlease give us the docstring that you want, end with "END"'
)
docstring = ""
user_input = input("> ")

while user_input != "END":
    docstring += user_input + "\n"
    user_input = input("> ")

# Let's make sure the docstring is not terminated:
while '"""' in docstring:
    print("replace")
    docstring = docstring.replace('"""', "")

if len(docstring) > 100:
    print("Docstring too long")
    quit()

docstring = '"""\n' + docstring + '\n"""\n'
with open("code_to_comment.py", "r") as rf:
    source = rf.read()

# Write new file
new_python_file = docstring + source

package_name = "commented_code"
new_filename = package_name + ".py"
with open(new_filename, "w") as wf:
    wf.write(new_python_file)

import os

os.system("python commented_code.py")

print(new_python_file)
