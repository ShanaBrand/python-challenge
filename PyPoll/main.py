import os

import csv

i=0
totalvotes = 0
NumVotes1 = 0 
NumVotes2 = 0 
NumVotes3 = 0 
NumVotes4 = 0 
NumVotes5 = 0 

Candidates = []
Votes =[]
perVote = []

os.chdir('/Users/Shanakay/Desktop/PythonHomework')

electionPath = os.path.join('..','PythonHomework','electionData1.csv')

with open(electionPath,newline = "")as elData:
    csvreader = csv.reader(elData,delimiter = ",")
   #Skip the header
    next(csvreader)
    for row in csvreader:
        totalvotes = totalvotes+1
        
        #if Candidates.contain(row[2])
        if row[2] not in Candidates:
            Candidates.append(row[2]) 
    
        numCan = len(Candidates)    
        
        if row[2] == Candidates[0]:
               NumVotes1 += 1
        elif row[2] == Candidates[1]:
               NumVotes2 += 1
        elif row[2] == Candidates[2]:
               NumVotes3 += 1
        else:
               NumVotes4 += 1
         
    totalvotes          
    VotePer1 = round((NumVotes1/totalvotes)*100,2)
    VotePer2 = round((NumVotes2/totalvotes)*100,2)
    VotePer3 = round((NumVotes3/totalvotes)*100,2)
    VotePer4 = round((NumVotes4/totalvotes)*100,2)
   
    Votes.append(NumVotes1)
    Votes.append(NumVotes2)
    Votes.append(NumVotes3)
    Votes.append(NumVotes4)
    
    perVote.append(VotePer1)
    perVote.append(VotePer2)
    perVote.append(VotePer3)
    perVote.append(VotePer4)
    
     
    #electionArray.append(Candidates)
    #electionArray.append(perVote)
    #electionArray.append(Votes)    
      
    #electionDictionary["Candidates"] = Candidates   
    #electionDictionary["Percentage Vote"] = perVote
    #electionDictionary["Number of Votes"] = Votes 
    
print(totalvotes)
print(row[2])
#print(electionDictionary.values())


print("-------------------------------")
print("Total Votes: ",(totalvotes))
print("-------------------------------")

#df = pd.dataFrame(electionDictionary)

results = zip(Candidates,perVote,Votes)
#print(*results,"\n")

for row in results:
    print(row)

electionpath = os.path.join('..','PythonHomework','electionResults.csv')
with open(electionpath,'w',newline="")as csvfile:
    csvwriter = csv.writer(csvfile,delimiter = ",")
    csvwriter.writerow(['Candidate','Percentage Vote','NumberofVotes'])
    results = zip(Candidates,perVote,Votes)
    for row in results:
        csvwriter.writerows(results)
        print(row)

     
   
    
