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


removed, added = parse_patch("sample.patch")

print("Removed lines:")
for r in removed:
    print(r)

print("\nAdded lines:")
for a in added:
    print(a)