#!/usr/bin/env python
# coding: utf-8

# In[2]:


# import necessary dependencies
import os
import csv


# In[3]:


#files to load and output
pypoll_csv = os.path.join('.', 'Resources', 'election_data.csv')

pypoll_output = os.path.join('.', 'election_analysis.txt')

pypoll_csv


# In[4]:


#variables
total_votes = 0
candidate_votes = {}
candidate_options = []
winner = ""
win_count = 0


# In[5]:


with open(pypoll_csv) as election_data:

    reader = csv.reader(election_data)

    #sets header as Ballot ID, County, Candidate
    header = next(reader)
#     print(header)
        
    #loops through reader to count the total rows 
    for row in reader:

        total_votes = total_votes + 1
        
        #gets candidate's name from each row
        candidate_name = row[2]
        
        
        if candidate_name not in candidate_options:
            
            #add to list of candidates in the running
            candidate_options.append(candidate_name)
            
            candidate_votes[candidate_name] = 0
            
        candidate_votes[candidate_name] += 1
                   
# print(candidate_votes)           
# print(candidate_options)
# print(total_votes)        

    
    

with open(pypoll_output, "w") as txt_file:
    output = (
    f"Election Results\n"
    f"-------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------\n"
    )
    print(output)  
    txt_file.write(output)

    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
    
        if(votes > win_count):
            win_count = votes
            winner = candidate
        
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"

        # print(votes)
        # print(vote_percentage)
        # print(winning_candidate) 
        print(voter_output)
        txt_file.write(voter_output)


    winning_candidate_summary = (
        f"-------------------\n"
        f"Winner: {winner}\n"
        f"-------------------\n"
    )
    print(winning_candidate_summary)
   
    txt_file.write(winning_candidate_summary)



# In[ ]:




