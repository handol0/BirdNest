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
merged_tableau = data[basic_info + tableau_uses + tableau_hopes]
using_tableau = data[basic_info+ tableau_uses] 

## Q31_A_Part_5와 Q31_B_Part_5가 null이 아닌 row만 ##

#merged_tableau[tableau_uses].isnull().any(axis=1)
#merged_tableau[merged_tableau[tableau_uses].isnull().any(axis=1) & merged_tableau[tableau_hopes].isnull().any(axis=1)]



## Q31_A_Part_5가 null이 아닌 row만 ##
using_tableau[using_tableau[tableau_uses].isnull().any(axis=1)]



# 결측치 제거!!! ####
tableau_usingf = using_tableau.dropna()
tableau_usingf


# 프로그래밍 랭귀지 테이블과 tableau user 테이블 합치기 #
tableau_using2 = pd.merge(tableau_usingf, data_prs_lang, left_index=True, right_index=True, how="inner")



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
for i in tableau_using2['Q7_Part_1']:
    if i == prs_lang_checklist[0]:
        python_num = python_num + 1
    data_prs_dict["Python"] = python_num

for i in tableau_using2['Q7_Part_2']:
    if i == prs_lang_checklist[1]:
        r_num = r_num + 1
    data_prs_dict["R"] = r_num

for i in tableau_using2['Q7_Part_3']:
    if i == prs_lang_checklist[2]:
        sql_num = sql_num + 1
    data_prs_dict["SQL"] = sql_num

for i in tableau_using2['Q7_Part_4']:
    if i == prs_lang_checklist[3]:
        c_num = c_num + 1
    data_prs_dict["C"] = c_num

for i in tableau_using2['Q7_Part_5']:
    if i == prs_lang_checklist[4]:
        cplus_num = cplus_num + 1
    data_prs_dict["C++"] = cplus_num

for i in tableau_using2['Q7_Part_6']:
    if i == prs_lang_checklist[5]:
        java_num = java_num + 1
    data_prs_dict["Java"] = java_num

for i in tableau_using2['Q7_Part_7']:
    if i == prs_lang_checklist[6]:
        javascript_num = javascript_num + 1
    data_prs_dict["Javascript"] = javascript_num

for i in tableau_using2['Q7_Part_8']:
    if i == prs_lang_checklist[7]:
        julia_num = julia_num + 1
    data_prs_dict["Julia"] = julia_num

for i in tableau_using2['Q7_Part_9']:
    if i == prs_lang_checklist[8]:
        swift_num = swift_num + 1
    data_prs_dict["Swift"] = swift_num

for i in tableau_using2['Q7_Part_10']:
    if i == prs_lang_checklist[9]:
        bash_num = bash_num + 1
    data_prs_dict["Bash"] = bash_num

for i in tableau_using2['Q7_Part_2']:
    if i == prs_lang_checklist[1]:
        matlab_num = matlab_num + 1
    data_prs_dict["MATLAB"] = matlab_num

print(data_prs_dict)


labels = []
sizes = []

for x, y in data_prs_dict.items():
    labels.append(x)
    sizes.append(y)

# Plot
plt.pie(sizes, labels=labels)

plt.axis('equal')
plt.show()
