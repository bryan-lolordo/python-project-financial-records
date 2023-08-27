#!/usr/bin/env python
# coding: utf-8

# In[3]:


# import necessary dependencies
import os
import csv


# In[4]:


pybank_csv = os.path.join('.', 'Resources', 'budget_data.csv')

pybank_output = os.path.join('.', 'budget_analysis.txt')

pybank_csv


# In[5]:


total_months = 0
net_change = []
month_change = []
total_net = 0
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999]


# In[7]:


with open(pybank_csv) as financial_data:

    reader = csv.reader(financial_data)

#     print(reader)

    #sets header as Date, Profit/Losses
    header = next(reader)
#     print(header)
    
    #skips next row and looks at 1 row of data
    first_row = next(reader)
    
#     print(first_row)
    
    #looks at first row of data and column 1 which is the profit/loss and converts to an integer. 
    total_net += int(first_row[1])
#     print(total_net)
    
    previous_net = int(first_row[1])
#     print(previous_net)
    
    total_months += 1 
    
    
    #loops through reader to count the total rows and provides number for total months and total profit/loss.
    for row in reader:
#         print(row)
        total_months += 1
        total_net += int(row[1])
        

#         #net change
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        
        net_change_list.append(net_change)
        
        
        #greatest increase
        if(net_change> greatest_increase[1]):
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
        
        
        #greatest decrease
        if(net_change < greatest_decrease[1]):
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change
        
# print(net_change_list)

# print(greatest_increase)

# print(greatest_decrease)

net_monthly_average = sum(net_change_list) / len(net_change_list)


output = (
    f"Financial Analysis\n"
    f"-------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change ${net_monthly_average}\n"
    f"Greatest Increase In Profits: ${greatest_increase[1]}\n"
    f"Greatest Decrease In Profits: ${greatest_decrease[1]}\n"
)

print(output)

with open(pybank_output, "w") as txt_file:
    txt_file.write(output)


# In[ ]:


#   total_net += int(first_row[1])
#    previous_net = int(first_row[1])
    
# #     total_months = total_months + 1
#     total_months += 1
# #    total_net += int(first_row[1])
# #    previous_net = int(first_row[1])
    
    for row in reader:
        total_months += 1
#        total_net += 1
        
#        total_net += int(row[1])
#        previous_net = int(row[1])

#        print(row)

        #Total Number of Months is 86
print(total_months)


# In[ ]:


#code with tutor

with open(pybank_csv):
    reader = csv.reader(pybank_csv, delimiter = ',')
    
    header = next(reader)
    
    first_row = next(reader)
    
#     total_months = total_months + 1
    total_months += 1
    total_net += int(first_row[1])
    previous_net = int(first_row[1])
    

    
#        total_net += int(r[1])
#       first 2 lines tracking total, next track net change using previous variables, calculate greatest increase/dec by using
#  month change and net change. then calculate average 


# In[ ]:




