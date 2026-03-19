import re
def parse_patch(file_path):
    removed = []
    added = []

    file = open(file_path, "r")

    for line in file:
        line = line.strip()

        if line.startswith("---") or line.startswith("+++"):
            continue

        if line.startswith("-"):
            removed.append(line[1:].strip())
        elif line.startswith("+"):
            added.append(line[1:].strip())

    file.close()

    return removed, added
def make_pattern(line):
    if "(" in line and ")" in line:
        func_name = line.split("(")[0]
        pattern = func_name + r"\s*\(.*\)"
    else:
        pattern = re.escape(line)

    return pattern

removed, added = parse_patch("sample.patch")

print("\nAdded lines:")
for a in added:
    print(a)

test_code = [
    "strcpy(buf, data);",
    "printf('hello');",
    "strcpy(user, input);",
    "printf(user);"
]
#the removed[0] is only for the first vulnerable line 
# pattern = make_pattern(removed[0])
#print("Pattern:", pattern)


#prints all the lines 
# for line in test_code:
#     print(line) 

print("\nPattern Matching Results:\n")
#ALL removed lines are checked (not just first one):
for r in removed:
    pattern = make_pattern(r)
    print("Pattern:", pattern)

    for line in test_code:   # ← MUST BE INSIDE
        if re.search(pattern, line):
            print("Matched:", line)

    print()