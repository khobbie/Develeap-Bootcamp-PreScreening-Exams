# from calendar import different_locale
from datetime import datetime



# Date format
date_format_str = '%d-%m-%Y %H:%M:%S.%f'



# Declaring variables
begin = False
end = False

start_date = 0
end_date = 0

timeDifference = 0

count = 0

timeDifferenceList = []

id = "N/A"


# Method 
# Python program to get average of a list
def Average(lst):
    return sum(lst) / len(lst)


# Reading File
with open("exam.log") as f:

# Loop over lines
  for sentence in f:

    # Trim line  
    sentence = sentence.strip()

    # Start transaction
    if "begin" in sentence :
        # print("begin here")
        begin = True
        start_date = datetime.strptime(sentence[0:22], date_format_str)
        # print(start_date)

    # End transaction
    if "end" in sentence :
        # print("end here")
        end = True 
        end_date = datetime.strptime(sentence[0:22], date_format_str)  
        # print(end_date)

    # between begin and end of a transaction
    if begin == True and end == True:

        # print("begin and end here")
        # Get the interval between two datetimes as timedelta object
        diff = end_date - start_date
        # Get the interval in milliseconds
        diff_in_milli_secs = diff.total_seconds() * 1000

        timeDifferenceList.append(diff_in_milli_secs)

    
    
# Displaying Results
print('\n\n')
print("timeDifferenceList: " + str(timeDifferenceList))
average = Average(timeDifferenceList)


print('\n\n')
print("average transaction time in milliseconds: " + str(average))
        


    

            


