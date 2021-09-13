### completed ###
import pandas as pd


##### kicpabird.xlsx 내에 있는 URL과 File 컬럼을 링크로 바꿔주는 쿼리 #####
##### Planning to discard this. there is no longer any use of this query due to the fact #####
##### crawling.ipynb has been updated to crawl file and URL as a link #####


writer = pd.ExcelWriter('E:/Folder/AUTOtrans.xlsx')  # 엑셀 쓰는 쿼리
indall = pd.read_excel('E:/Folder/data/kicpantdata/kicpabird.xlsx')


num=0
num2=0

for i in indall["URL"]:
    if type(indall["URL"][num]) ==str:
        if indall["URL"][num][0:8] == "<a href=":
            num=num+1
        elif indall["URL"][num][0:8] != "<a href=":
            indall["URL"][num] = '<a href="'+ i + '" rel="noopener" target="_blank">링크</a>'
            num=num+1
    else:
        num = num +1
        
for j in indall["File"]:
    if type(indall["File"][num2]) ==str:
        if indall["File"][num2][0:8] == "<a href=":
            num2 = num2+1
        elif indall["File"][num2][0:8] != "<a href=":  
            indall["File"][num2]= '<a href="'+ j + '" rel="noopener" target="_blank">파일</a>'
            num2 = num2 +1
    else:
        num2 = num2 +1        

indall["작성일자"].replace('-', '년 ')

indall.to_excel(writer, sheet_name='YES',header=True, index=False)

writer.save()
print('COMPLETED')
