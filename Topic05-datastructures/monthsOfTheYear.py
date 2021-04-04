#A tuple that stores the months of the year
#then another tuple which lists just 
#the summer months of the year
#one at a time
#Author: Carolyn Moorhouse

months = ("January",
             "February",
             "March",
             "April",
             "May",
             "June",
             "July",
             "August",
             "September",
             "October",
             "November",
             "December"
)
summer = months[4:7]
for month in summer:
    print(month)