#Use pie charts to visualize the distribution of Internet access at home (internet) among students.
import pandas as pd  #importing pandas
import matplotlib.pyplot as mat  #This is for importing matplotlib
import numpy as np  #This is for importing numpy
#Void Variables:
accessed_internet = 0
not_accessed_internet = 0
#Opening Csv File:
data = pd.read_csv("C:\\Users\Muhammad Usman\PycharmProjects\QCRSemesterProject\datafile.csv")
# To read a specific column in the cvs:
specific_column = data["internet"]
#To check the yes or no in the line:
for line in specific_column:
    if line == "no":
        not_accessed_internet = not_accessed_internet +1
    else:
        accessed_internet = accessed_internet +1
#For Ploting The Pie Chart:
y = np.array([accessed_internet, not_accessed_internet])
LabelsInIt = (["Internet Accessed", "Internet Not Acessed"])
ExplodeInIt = ([0.15, 0])
ColoursInIt = (["blue", "yellow"])
print("The {0} number of students have Internet access at Home.".format(accessed_internet))
print("The {0} number of students do not have Internet access at Home.".format(not_accessed_internet))
mat.pie(y, labels=LabelsInIt, startangle=180, explode=ExplodeInIt, shadow=True, colors=ColoursInIt,autopct='%1.1f%%')
mat.legend(title = "The ratio of students to Internet Access:")
mat.show()

