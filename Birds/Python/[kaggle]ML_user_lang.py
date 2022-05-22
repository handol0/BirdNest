## Load and Import Datas & Library ##
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv(".../jupytersnake/data/Kaggle_data_2020ML/kaggle_survey_2020_responses.csv", low_memory=False)


basic_info = ['Q1', 'Q3', 'Q4', 'Q5', 'Q6', ]
tableau_uses = ['Q31_A_Part_5']
tableau_hopes = ['Q31_B_Part_5']

prs_lang = ['Q7_Part_1',
'Q7_Part_2',
'Q7_Part_3',
'Q7_Part_4',
'Q7_Part_5',
'Q7_Part_6',
'Q7_Part_7',
'Q7_Part_8',
'Q7_Part_9',
'Q7_Part_10',
'Q7_Part_11',
'Q7_Part_12']

data_prs_lang = data[prs_lang]
data_prs_lang.head()
data.info()
# Rows = 20037개 이다 #


prs_lang_checklist = ["Python", "R", "SQL", "C", "C++", "Java", "Javascript", "Julia", "Swift", "Bash", "MATLAB"]

data_prs_dict = {'Python' : '',
'R' : '',
'SQL' : '',
'C' : '',
'C++' : '',
'Java' : '',
'Javascript' : '',
'Julia' : '',
'Swift' : '',
'Bash' : '',
'MATLAB' : ''}

def language_usage():
    python_num = 0
    r_num = 0
    sql_num = 0
    c_num = 0
    cplus_num = 0
    java_num = 0
    javascript_num = 0
    julia_num = 0
    swift_num = 0
    bash_num = 0
    matlab_num = 0
    for i in data_prs_lang['Q7_Part_1']:
        if i == prs_lang_checklist[0]:
            python_num = python_num + 1
        data_prs_dict["Python"] = python_num

    for i in data_prs_lang['Q7_Part_2']:
        if i == prs_lang_checklist[1]:
            r_num = r_num + 1
        data_prs_dict["R"] = r_num
        
    for i in data_prs_lang['Q7_Part_3']:
        if i == prs_lang_checklist[2]:
            sql_num = sql_num + 1
        data_prs_dict["SQL"] = sql_num

    for i in data_prs_lang['Q7_Part_4']:
        if i == prs_lang_checklist[3]:
            c_num = c_num + 1
        data_prs_dict["C"] = c_num
        
    for i in data_prs_lang['Q7_Part_5']:
        if i == prs_lang_checklist[4]:
            cplus_num = cplus_num + 1
        data_prs_dict["C++"] = cplus_num
        
    for i in data_prs_lang['Q7_Part_6']:
        if i == prs_lang_checklist[5]:
            java_num = java_num + 1
        data_prs_dict["Java"] = java_num
        
    for i in data_prs_lang['Q7_Part_7']:
        if i == prs_lang_checklist[6]:
            javascript_num = javascript_num + 1
        data_prs_dict["Javascript"] = javascript_num
        
    for i in data_prs_lang['Q7_Part_8']:
        if i == prs_lang_checklist[7]:
            julia_num = julia_num + 1
        data_prs_dict["Julia"] = julia_num
        
    for i in data_prs_lang['Q7_Part_9']:
        if i == prs_lang_checklist[8]:
            swift_num = swift_num + 1
        data_prs_dict["Swift"] = swift_num
        
    for i in data_prs_lang['Q7_Part_10']:
        if i == prs_lang_checklist[9]:
            bash_num = bash_num + 1
        data_prs_dict["Bash"] = bash_num
        
    for i in data_prs_lang['Q7_Part_2']:
        if i == prs_lang_checklist[1]:
            matlab_num = matlab_num + 1
        data_prs_dict["MATLAB"] = matlab_num

language_usage()

#print(data_prs_dict)


labels = []
sizes = []

for x, y in data_prs_dict.items():
    labels.append(x)
    sizes.append(y)

# Plot
plt.pie(sizes, labels=labels)

plt.axis('equal')
plt.show()


#testing page!!!!!

#for i in range(1,12):
#    print("'Q7_Part_"+ str(i)+ "'," )
#



#abc = ["C,C++", "C,Python", "C++", "C"]
#checklist = ['C', 'C++', 'Python']
#test_num =0
#if checklist[0] in i:
#    test_num = test_num+1
        
#print(test_num)

#for i in prs_lang_checklist:
#    print("'" + i + "' : " + i.lower() + '_num,')



#Testing the push