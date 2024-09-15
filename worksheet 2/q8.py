# Write a Python program to display the examination schedule. (extract the date from
# exam_st_date). exam_st_date = (11, 12, 2014)

exam_st_date = (11, 12, 2014)

# Extract day, month, and year from the tuple
day, month, year = exam_st_date

# Display the examination schedule
print(f"The examination will start on: {day:02d}/{month:02d}/{year}")