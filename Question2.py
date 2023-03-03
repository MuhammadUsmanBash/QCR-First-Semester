#Create a violin plot to compare the distribution of the final grade (G3) between students who have extra educational support (schoolsup) and students who do not
import pandas as pd  #importing pandas
import matplotlib.pyplot as mat  #This is for importing matplotlib
import numpy as np  #This is for importing numpy
import seaborn as sns #This is for importing seaborn
#Void lists:
Yes_List = []
No_List = []
data = pd.read_csv("C:\\Users\Muhammad Usman\PycharmProjects\QCRSemesterProject\datafile.csv")
# To read a specific column in the cvs:
schoolsup = data["schoolsup"]
G3 = data["G3"]
#The real Logic:
line = 0
for lines_schoolup in schoolsup:
    if lines_schoolup == "yes":
        data_in_G3_line = G3[line]
        Yes_List.append(data_in_G3_line)
        line = line+1
    elif lines_schoolup == "no":
        data_in_G3_line = G3[line]
        No_List.append(data_in_G3_line)
        line = line + 1
#For plotting graph:
data = [Yes_List, No_List]
fig, ax = mat.subplots()
ax.violinplot(data, showmeans=True, showextrema=True, showmedians=True, bw_method=0.5, widths=0.7, positions=[1,2])
ax.set_xticks([1,2])
ax.set_xticklabels(['With Extra Educational Support', 'Without Extra Educational Support'])
ax.set_ylabel('Final Grade of Students')
ax.set_title('Distribution of Final Grades by Extra Educational Support')
mat.show()
















