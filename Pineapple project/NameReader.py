codes = dict()
names = []
all_ids = []
read_ids = []

with open('user_ids.txt', 'r') as f:
    for line in f:
        read_ids.append(line.strip())
        print(read_ids)

print()

with open('codenames.txt', 'r') as f:
    for line in f:
        a = line.split()
        us_id, us_name = a[0], a[1:]
        codes[us_id] = us_name
        all_ids.append(us_id)

for us_id in all_ids:
    if us_id in read_ids:
        all_ids.pop(all_ids.index(us_id))
    print(all_ids)

print(all_ids)

with open('missing_ids.txt', 'w') as f:
    for i in all_ids:
        f.write(i + '\n')