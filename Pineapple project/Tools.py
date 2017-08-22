def addmember(file, string):
    mass = []
    with open(file, 'r') as f:
        for line in f:
            mass.append(line.strip())
            
    mass.append(string)
            
    with open(file, 'w') as f:
        for line in mass:
            f.write(line + '\n')