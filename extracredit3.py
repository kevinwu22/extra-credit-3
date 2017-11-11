from csv import *

inFile = open('gradesRaw.csv', 'r')
csvReader = reader(inFile, delimiter = ',')

results = []
for row in csvReader: # each row is a list
        results.append(row)
print(results)

value = len(results)
print(value)

#data = row[1]+row[2]+row[3]+row[4]

#print(data)

def gradeScores(grade):

    if grade >= 91 and grade <= 100:
        return("A")
    elif grade >= 81 and grade <= 90:
        return("B")

    elif grade >= 71 and grade <= 80:
        return("C")

    elif grade >= 60 and grade <= 70:
        return("D")

    else:
        return("F")

f = open('gradeSheet.csv', 'w')
csvwriter = writer(f, delimiter=',', lineterminator="\n")

headers = [["Name", "Total", "Letter Grade"]]
csvwriter.writerows(headers)

x = 0
while x < value:
    #CRAP GOES HERE
    if x != 0:
        print(x)
        currentStudent = results[x]
        print(currentStudent)
        name = currentStudent[0]
        data = int(currentStudent[1])+int(currentStudent[2])+int(currentStudent[3])+int(currentStudent[4])+int(currentStudent[5])
        grade = gradeScores(data)
        print(name)
        print(data)
        print(grade)
        studentData = [[name, data, grade]]
        csvwriter.writerows(studentData)
    #CRAP ENDS HERE
    x += 1

#Close Output File
f.close()

