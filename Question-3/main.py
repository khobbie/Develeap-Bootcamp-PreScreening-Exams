count = 0

# Reading File
with open("exam.log") as f:

  # Loop over lines
  for sentence in f:
  
  # Checking if line is a transaction
    if 'transaction' in sentence :
            # Count the transaction
            count = count + 1

# lines contain transaction word
# Since a transaction is begin and end 
# divide by 2
print("Number of transactions:  " + str(count/2))   