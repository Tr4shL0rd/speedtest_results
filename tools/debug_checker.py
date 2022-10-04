with open("speedtest_new_test.py", "r") as f:
    lines = f.readlines()
    Lines = []
    for line in lines:
        Lines.append(line.replace("\n", ""))
    for line in Lines:
        if "debug" in line.lower():
            print(f"DEBUG STATEMENT AT LINE {Lines.index(line)+1}: {Lines[Lines.index(line)]} ")