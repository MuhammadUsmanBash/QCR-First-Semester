#Use bar plots to visualize the relationship between the mother's education level (Medu) and the final grade (G3)
import pandas as pd  #importing pandas
import matplotlib.pyplot as mat  #This is for importing matplotlib
import numpy as np  #This is for importing numpy
import seaborn as sns

#Void lists:
List_of_1 = []
List_of_2 = []
List_of_3 = []
List_of_4 = []


data = pd.read_csv("C:\\Users\Muhammad Usman\PycharmProjects\QCRSemesterProject\datafile.csv")

# To read a specific column in the cvs:
Medu = data["Medu"]
G3 = data["G3"]
line = 0
for lines_Medu in Medu:
    if lines_Medu == 1.0:
        data_in_G3_line = G3[line]
        List_of_1.append(data_in_G3_line)
        line = line+1
    elif lines_Medu == 2.0:
        data_in_G3_line = G3[line]
        List_of_2.append(data_in_G3_line)
        line = line + 1
    elif lines_Medu == 3.0:
        data_in_G3_line = G3[line]
        List_of_3.append(data_in_G3_line)
        line = line + 1
    elif lines_Medu == 4.0:
        data_in_G3_line = G3[line]
        List_of_4.append(data_in_G3_line)
        line = line + 1
list1 = np.mean(List_of_1)
list2 = np.mean(List_of_2)
list3 = np.mean(List_of_3)
list4 = np.mean(List_of_4)

#For plot:
# Data for the plot
x = ['1', '2', '3', '4']
y = [list1, list2, list3, list4]
names = ['< high school', 'High school', 'Higher education', 'University']
# Create the bar plot
mat.bar(x, y)

# Add labels and title
mat.xlabel('Levels of Mother Education')
mat.ylabel('Final Results of Students')
mat.title('Effect of mothers education on final results of students')
mat.xticks(x, names)
# Display the plot
mat.show()

