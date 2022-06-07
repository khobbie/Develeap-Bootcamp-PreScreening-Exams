
# Reading File
with open("exam.log") as f:
    lines = f.read() ##Assume the sample file has 3 lines
    
    # Read only first line
    first = lines.split('\n', 1)[0]

print(first)