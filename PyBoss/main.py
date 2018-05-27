import os
import csv
from datetime import datetime

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

empList=[]
FirstN = []
LastN = []
newDate =[]
maskedSSN =[]
firstSSN =[]
stateList=[]
DateList = []

lastSSN = ""
newSSN = ""
stateAbrev = ""
state = ""

fiveA = ""
fiveB = ""
fiveC = ""
newSSN = ""

os.chdir('/Users/Shanakay/Desktop/PythonHomework')

employeePath = os.path.join('..','PythonHomework','employeeData2.csv')

with open(employeePath, newline="")as empfile:
    csvReader = csv.reader(empfile, delimiter = ",")
    next(csvReader)
    
    for row in csvReader:
        #Get and store the EmployeeID
         empID = row[0]
         empList.append(empID)
         
         #split the NAME column into FirstName and LastName 
         splitName = row[1].split(" ")
         FirstName = splitName[0]
         LastName = splitName[1]
         FirstN.append(FirstName)
         LastN.append(LastName)
         
         #Reformat the DOB Column
         dateOB = row[2]
         DateList.append(dateOB)
         for d in DateList:
             objDate = datetime.strptime(d,'%Y-%m-%d')
             convertDate = datetime.strftime(objDate, '%m/%d/%Y')
             newDate.append(convertDate)
         
         #Rewrite the SSN to hide the first five(5) digits
         splitSSN = row[3]
         firstFive = splitSSN[:6]
         lastFour = splitSSN[6:]
         for s in firstFive:
             fiveA = s[:0:3].replace('%','xxx')
             fiveB = s[:4]
             fiveC = s[:5:6].replace('%','xx')
             newSSN = fiveA+fiveB+fiveC+lastFour
             maskedSSN.append(lastFour)
         #Rewrite State column to display two letter state abbreviation    
         for key in us_state_abbrev:
            if row[4] == key:
                 state = us_state_abbrev[key]
                 stateList.append(state)
                 
results = zip(empList,FirstN,LastN,newDate,maskedSSN,stateList) 
for rows in results:
    print(rows)               
 
bosspath=os.path.join('..', 'PythonHomework','PyBossResults.csv')
# open the output file, create a header row, and then write the zipped object to the csv
with open(bosspath,'w',newline="")as bossfile:
    csvwriter = csv.writer(bossfile,delimiter = ",")
    csvwriter.writerow(['EmpID', 'FirstName', 'LastName','DOB','SSN', 'State'])
    results = zip(empList,FirstN,LastN,newDate,maskedSSN,stateList)
    for row in results:
        csvwriter.writerows(results)
        print(row)
        
  
  









