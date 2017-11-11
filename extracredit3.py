from csv import *

inFile = open('gradesRaw.csv', 'r')
csvReader = reader(inFile, delimiter = ',')


def gradeScores(totalGrade):

    if grade >= 91 and grade <= 100:
        return("A")
    elif grade >= 81 and grade < 90:
        return("B")

    elif grade >= 71 and grade < 80:
        return("C")

    elif grade >= 60 and grade < 70:
        return("D")

    else:
        return("F")




f = open('gradeSheet.csv', 'w')
csvwriter = writer(f, delimiter=',', lineterminator="\n")
headers = [["Name", "Total", "Letter Grade"]]
csvwriter.writerows(headers)
