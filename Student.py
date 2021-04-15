import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    student_marks = []
    days_present = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            student_marks.append(float(row['Marks In Percentage']))
            days_present.append(float(row['Days Present']))

    return{"x": student_marks, "y": days_present}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print('Correlation between student marks and days present:\n>', correlation[0, 1])

def setup():
    data_path = "Student Marks vs Days Present.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)
setup()