count = 0

# Reading File
with open("exam.log") as f:

  # Loop over lines
  for sentence in f:
    result = sentence.find('ERROR')

    # Checking if line is ERROR
    if 'ERROR' in sentence :
        if result == 23:
          # Count the ERRORS
          count = count + 1

            
print("Number of ERROR:  " + str(count))