import urllib
from bs4 import BeautifulSoup
from datetime import timedelta
import datetime
import pandas as pd

pd.set_option('display.max_row', 500)
pd.set_option('display.max_columns', 100)

C_RESET   = "\033[0m"
C_BOLD    = "\033[1m"

C_RED    = "\033[31m"
C_BLUE   = "\033[34m"
 
C_BGBLACK  = "\033[40m"
C_BGRED    = "\033[41m"
C_BGGREEN  = "\033[42m"
C_BGYELLOW = "\033[43m"
C_BGBLUE   = "\033[44m"
C_BGWHITE  = "\033[47m"



def get_collection_schema():    # 노션 생성 테이블 형식 지정
    return {
        "title" : {"name" : "title", "type" : "text"},
        "source" : {"name" : "source", "type" : "text"},
        "url" : {"name" : "url", "type" : "url"},
        "publisheddate" : {"name" : "publisheddate" , "type" : "text"}
    }


def mergeq(): #과학기술정책연구원, 산업연구원, 소프트웨어정책연구소, 한국콘텐츠진흥원, 한국관광공사
    askmuch = int(input("며칠 내 발간된 자료들을 찾으시겠습니까?"))
    todayd = datetime.datetime.today() + timedelta(days=-(askmuch)) # timedelta로 x일 빼기
    todayd_re = todayd.strftime("%Y-%m-%d")
    writer = pd.ExcelWriter('E:\Folder\한국공인회계사회\Crawling\crawling.xlsx')  # 엑셀 작성할 디렉토리 쿼리


    whichcom = input("다음 기업 중 고르시오\n[1]과학기술정책연구원\n[2]산업연구원\n[3]소프트웨어정책연구원\n[4]한국콘텐츠진흥원\n[5]한국관광공사\n[6]영화진흥위원회\n[7]한국보건산업진흥원\n[8]한국외식산업진흥원\n[9]한국무역협회\n[10]한국산업단지공단\n[11]한국인터넷진흥원\n[12]한국정보통신산업연구원\n[13]한국출판문화산업진흥원\n[14]서울디지털재단\n\n\nTo print EVERYTHING input 'everything'\n")

    dlist = []
    tlist = []
    ulist = []
    total_dict = []
    drop_list =[]

    if whichcom == "1": #과학기술정책연구원    ####### 수정 필요 STEPI 사이트가 대대적으로 리모델링에 들어갔었음 ######
        list_url_list = {"https://www.stepi.re.kr/site/stepiko/report/List.do?cateCont=A0501" : '과학기술정책연구원-STEPI Insight', "https://www.stepi.re.kr/site/stepiko/PeriodicReportList.do?cateCont=A0505" : '과학기술정책연구원-Future Horizon+'}
        for list_url in list_url_list:
            url = urllib.request.Request(list_url)
            result = urllib.request.urlopen(url).read().decode("utf-8")
            soup=BeautifulSoup(result, "html.parser") # 파싱하기  
            print('\n', C_BGRED + list_url_list[list_url] + C_RESET)
    
            title = soup.find_all('td', class_ = 'title')  # div태그 가져오기
            date1 = soup.find_all('td', class_ = "date")
            if list_url == "https://www.stepi.re.kr/site/stepiko/report/List.do?cateCont=A0501":
                urllink = soup.find("table", class_="list mCustom").find_all("td", class_='title')  # 가장 큰 틀부터 찾고, 세부적인 틀 find_all로 찾
            if list_url == "https://www.stepi.re.kr/site/stepiko/PeriodicReportList.do?cateCont=A0505":
                urllink = soup.find('div', class_ = "magazineBoardList").find_all('a', 'href')
                
    
            for i,j,k in zip(title, date1, urllink):
                temp_dict = {'title' : '', 'date': '', 'url': ''}
                title_re = i.get_text().strip()
                date1_re = j.get_text().strip()
                date2 = date1_re.replace('.', '-')
                urllink2 = k.find("a")["href"]
                urllink3 = "http://www.stepi.re.kr/app/publish/" + urllink2
                urllink4 = '<a href="'+ urllink3 + '" rel="noopener" target="_blank">링크</a>'

                
                if date2 >= todayd_re:
                    temp_dict['title'] = title_re
                    temp_dict['date'] = date2
                    temp_dict['url'] = urllink4
                    
                    total_dict.append(temp_dict)
    
            pantable = pd.DataFrame(total_dict)
            print(pantable)
            print(C_BOLD + C_BLUE + '\n링크 = ', list_url +C_RESET)
            
            if list_url == "https://www.stepi.re.kr/site/stepiko/report/List.do?cateCont=A0501":
                pantable.to_excel(writer, sheet_name='과학기술정책연구원-STEPI Insights',header=True)
            if list_url == "https://www.stepi.re.kr/site/stepiko/PeriodicReportList.do?cateCont=A0505":
                pantable.to_excel(writer, sheet_name='과학기술정책연구원-Future Horizon+', header=True)
                writer.save()
                
    if whichcom == "2" or whichcom == "everything":   # 산업연구원
        list_url_list = {"https://www.kiet.re.kr/kiet_web/?sub_num=8" : '산업연구원-연구보고서', "https://www.kiet.re.kr/kiet_web/?sub_num=12" : '산업연구원-KIET 산업경제'}
        for list_url in list_url_list:    
            url = urllib.request.Request(list_url)
            result = urllib.request.urlopen(url).read().decode("utf-8")
            soup=BeautifulSoup(result, "html.parser") # 파싱하기  
            print('\n', C_BGRED + list_url_list[list_url] + C_RESET)


            title = soup.find_all('td', class_ = 'tt')  # div태그 가져오기
            date1 = soup.find_all('td', class_ = "dt")
            urllink = soup.find('div', class_ = 'tbl').find_all('td', class_ = 'tt')
        
            for i,j,k in zip(title, date1, urllink):
                temp_dict = {'보고서명' : '', '출처' : '', '산업분류' : '', '분석 유형' : '', '보고서 유형' : '', '작성일자' : '', 'URL' : '', 'File' : ''}
                title_re = i.get_text().strip()
                date1_re = j.get_text().strip()
                date2 = date1_re.replace('.', '-')
                urllink2 = k.find("a")["href"]
                urllink3 = 'https://www.kiet.re.kr' + urllink2
                urllink4 = '<a href="' + urllink3 + '" rel="noopener" target="_blank">링크</a>'
                
                if date2 >= todayd_re:
                    temp_dict['보고서명'] = title_re
                    temp_dict['출처'] = '산업연구원'
                    temp_dict['작성일자'] = date2
                    temp_dict['URL'] = urllink4
                    
                    total_dict.append(temp_dict)
            print(C_BOLD + C_BLUE + '\n링크 = ', list_url +C_RESET)
        

    if whichcom == "3" or whichcom == "everything":  #소프트웨어정책연구소
        list_url_list = {"https://spri.kr/posts?code=insight" : '소프트웨어정책연구소-인사이트리포트', "https://spri.kr/posts?code=research" : '소프트웨어정책연구소-연구보고서', "https://spri.kr/posts?code=issue_reports" : '소프트웨어정책연구소-이슈리포트', "https://spri.kr/posts?code=column" : '소프트웨어정책연구소-SPRi 칼럼', "https://spri.kr/posts?code=industry_trend" : '소프트웨어정책연구소-SW산업동향'}
        for list_url in list_url_list:    
            url = urllib.request.Request(list_url)
            result = urllib.request.urlopen(url).read().decode("utf-8")
            soup=BeautifulSoup(result, "html.parser") # 파싱하기  
            print('\n', C_BGRED + list_url_list[list_url] + C_RESET)
        
            title = soup.find_all('h3', class_ = 'panel-title float-left')  # div태그 가져오기
            date1 = soup.find_all('p', class_ = "date")
            urllink = soup.find_all('h3', class_ ='panel-title float-left')
        
        
            for i,j,k in zip(title, date1, urllink):
                temp_dict = {'보고서명' : '', '출처' : '', '산업분류' : '', '분석 유형' : '', '보고서 유형' : '',  '작성일자' : '', 'URL' : '', 'File' : ''}
                title_re = i.get_text().strip()
                date1_re = j.get_text().strip()
                date2 = date1_re.replace('.', '-')
                urllink2 = k.find("a")['href']
                urllink3 = 'https://www.spri.kr' + urllink2
                urllink4 = '<a href="'+ urllink3 + '" rel="noopener" target="_blank">링크</a>'
                
                
                if date2 >= todayd_re:
                    temp_dict['보고서명'] = title_re
                    temp_dict['출처'] = "소프트웨어정책연구소"
                    temp_dict['작성일자'] = date2
                    temp_dict['URL'] = urllink4
                    
                    total_dict.append(temp_dict)
            
            print(C_BOLD + C_BLUE + '\n링크 = ', list_url +C_RESET)


    if whichcom == "4" or whichcom == "everything":  #한국콘텐츠진흥원
        list_url_list = {"https://www.kocca.kr/cop/bbs/list/B0000147.do?menuNo=201825" : '한국콘텐츠진흥원 연구보고서-보고서', "https://www.kocca.kr/cop/bbs/list/B0158949.do?menuNo=203779" : '한국콘텐츠진흥원 산업통계-반기별콘텐츠산업동향분석', "https://www.kocca.kr/cop/bbs/list/B0000141.do?menuNo=200898" : '한국콘텐츠진흥원 정기간행물-KOCCA포커스', "https://www.kocca.kr/cop/bbs/list/B0000146.do?menuNo=201826" : '한국콘텐츠진흥원 연구보고서-산업백서'}
        for list_url in list_url_list:
            url = urllib.request.Request(list_url)
            result = urllib.request.urlopen(url).read().decode("utf-8")
            soup=BeautifulSoup(result, "html.parser") # 파싱하기
            print('\n', C_BGRED + list_url_list[list_url] + C_RESET)

            title = soup.find('div', class_ = 'board_list_body').find_all('div', class_ = "subject")  # 제목 가져오기
            date1 = soup.find('div', class_ = 'board_list_body').find_all('div', class_ = "date")   # 날짜 가져오기
            urllink = soup.find('div', class_ = "board_list_body").find_all('div', class_='subject')


            for i,j,k in zip(title, date1, urllink):
                temp_dict = {'보고서명' : '', '출처' : '', '산업분류' : '', '분석 유형' : '', '보고서 유형' : '', '작성일자' : '', 'URL' : '', 'File' : ''}
                title_re = i.get_text().strip()
                date1_re = j.get_text().strip()
                date2 = date1_re.replace('.', '-')
                urllink2 = k.find("a")['href']
                urllink3 = 'https://www.kocca.kr' + urllink2
                urllink4 = '<a href="'+ urllink3 + '" rel="noopener" target="_blank">링크</a>'
                
                if date2 >= todayd_re:
                    temp_dict['보고서명'] = title_re
                    temp_dict['출처'] = '한국콘텐츠진흥원'
                    temp_dict['작성일자'] = date2
                    temp_dict['URL'] = urllink4
                    
                    total_dict.append(temp_dict)
                      
            print(C_BOLD + C_BLUE + '\n링크 = ', list_url +C_RESET)
            

    if whichcom == "5": # 한국관광공사 #컬럼을 숫자식으로 불러서 사이트 변경시 다시 재정립 필요
        list_url_list = {"http://kto.visitkorea.or.kr/kor/notice/data/report/org.kto" : '한국관광공사-공사발간보고서'}
        dcoln = 0
        for list_url in list_url_list:
            tlist = []
            dlist = []
            ulist = []
            url = urllib.request.Request(list_url)
            result = urllib.request.urlopen(url).read().decode("utf-8")
            soup=BeautifulSoup(result, "html.parser") # 파싱하기  
            print('\n', C_BGRED + list_url_list[list_url] + C_RESET)
            
            title = soup.find_all('td', class_ = 'txtL')  # div태그 가져오기
            date1 = soup.find_all('td')
            urllink = soup.find_all('td', class_ = 'txtL')
            

            
            for i,k in zip(title, urllink):
                title_re = i.get_text().strip()
                urllink2 = k.find("a")['href']
                urllink3 = 'http://kto.visitkorea.or.kr' + urllink2
                urllink4 = '<a href="'+ urllink3 + '" rel="noopener" target="_blank">링크</a>'
                tlist.append(title_re)
                ulist.append(urllink3)
            for j in date1:
                dcoln = dcoln +1
                if dcoln % 3 == 0:
                    date1_re = j.get_text().strip()
                    date2 = date1_re.replace('.', '-')
                    if date2 >= todayd_re:
                        dlist.append(date2)

                
            for a, b, c in zip(tlist, dlist, ulist):
                temp_dict = {'보고서명' : '', '출처' : '', '산업분류' : '', '분석 유형' : '', '보고서 유형' : '', '작성일자' : '', 'URL' : '', 'File' : ''}
                temp_dict['보고서명'] = a
                temp_dict['출처'] = "한국관광공사"
                temp_dict['작성일자'] = b
                temp_dict['URL'] = c
                
                total_dict.append(temp_dict)
                            
            pantable =  pd.DataFrame(total_dict)
            print(pantable)
            print(C_BOLD + C_BLUE + '\n링크 = ', list_url +C_RESET)
            
            if list_url == "http://kto.visitkorea.or.kr/kor/notice/data/report/org.kto":
                pantable.to_excel(writer, sheet_name='한국관광공사-공사발간보고서',header=True)
                writer.save()


    if whichcom == "6":  # 영화진흥위원회  #### error: java 형식 url이라 url을 가져올 수 없음
        list_url_list = {"https://www.kofic.or.kr/kofic/business/rsch/findPolicyList.do" : '영화진흥위원회-정책연구(전체보기)'}
        dcoln = 0
        for list_url in list_url_list: 
            tlist = []
            dlist = []
            ulist = []
            url = urllib.request.Request(list_url)
            result = urllib.request.urlopen(url).read().decode("utf-8")
            soup=BeautifulSoup(result, "html.parser") # 파싱하기  
            print('\n', C_BGRED + list_url_list[list_url] + C_RESET)
            
            title = soup.find_all('td', class_ = "subject")  # div태그 가져오기
            date1 = soup.find_all('td')
            urllink = soup.find_all('td', class_ = "subject")
            
            for i,k in zip(title, urllink):
                title_re = i.get_text().strip()
                urllink2 = k.find("a")['href']
                urllink3 = 'https://www.kofic.or.kr/' + urllink2
                urllink4 = '<a href="'+ urllink3 + '" rel="noopener" target="_blank">링크</a>'
                tlist.append(title_re)
                ulist.append(urllink4)
                
                
            for j in date1:
                dcoln = dcoln +1  # 사이트 게시판 내 컬럼 갯수
                if dcoln % 4 == 0:
                    date1_re = j.get_text().strip()
                    date2 = date1_re.replace('.', '-')
                    if date2 >= todayd_re:
                        dlist.append(date2)

            for a, b, c in zip(tlist, dlist, ulist):
                temp_dict = {'title' : '', 'date' : '', 'url' : ''}
                temp_dict['title'] = a
                temp_dict['date'] = b
                temp_dict['url'] = c
                
                total_dict.append(temp_dict)
                            
            pantable =  pd.DataFrame(total_dict)
            print(pantable)                    
            print(C_BOLD + C_BLUE + '\n링크 = ', list_url +C_RESET)
            
            if list_url == "https://www.kofic.or.kr/kofic/business/rsch/findPolicyList.do":
                pantable.to_excel(writer, sheet_name='영화진흥위원회-정책연구(전체보기)',header=True)
                writer.save()


    if whichcom == "7" or whichcom == "everything":   # 한국보건산업진흥원
        list_url_list = {"https://www.khidi.or.kr/board?menuId=MENU01783&siteId=SITE00002" : '한국보건산업진흥원-보건산업동향(브리프)','https://www.khidi.or.kr/board?menuId=MENU00085&siteId=SITE00002' : '한국보건산업진흥원-연구보고서', 'https://www.khidi.or.kr/board?menuId=MENU01435' : '한국보건산업진흥원-보건의료 R&D'}
        dcoln = 0
        for list_url in list_url_list:
            tlist = []
            dlist = []
            ulist = []
            url = urllib.request.Request(list_url)
            result = urllib.request.urlopen(url).read().decode("utf-8")
            soup=BeautifulSoup(result, "html.parser") # 파싱하기  
            print('\n', C_BGRED + list_url_list[list_url] + C_RESET)
            
            title = soup.find_all('td', class_= "ellipsis")  # div태그 가져오기
            date1 = soup.find_all('td')
            urllink = soup.find_all('td', class_= "ellipsis")
            
            for i,k in zip(title, urllink):
                title_re = i.get_text().strip()
                urllink2 = k.find("a")['href']
                urllink3 = 'https://www.khidi.or.kr' + urllink2
                urllink4 = '<a href="'+ urllink3 + '" rel="noopener" target="_blank">링크</a>'
                tlist.append(title_re)
                ulist.append(urllink4)
            
            if list_url == 'https://www.khidi.or.kr/board?menuId=MENU00085&siteId=SITE00002':
                for j in date1:
                    dcoln = dcoln +1
                    if dcoln% 6 == 0:
                        date1_re = j.get_text().strip()
                        date2 = date1_re.replace('.', '-')
                        if date2 >= todayd_re:
                            dlist.append(date2)
            else:
                for j in date1:
                    dcoln = dcoln +1  # 사이트 게시판 내 컬럼 갯수
                    if dcoln % 5 == 3:
                        date1_re = j.get_text().strip()
                        date2 = date1_re.replace('.', '-')
                        if date2 >= todayd_re:
                            dlist.append(date2)
                    
            for a, b, c in zip(tlist, dlist, ulist):
                temp_dict = {'보고서명' : '', '출처' : '', '산업분류' : '', '분석 유형' : '', '보고서 유형' : '', '작성일자' : '', 'URL' : '', 'File' : ''}
                temp_dict['보고서명'] = a
                temp_dict['출처'] = "한국보건산업진흥원"
                temp_dict['작성일자'] = b
                temp_dict['URL'] = c
                
                total_dict.append(temp_dict)
                             
            print(C_BOLD + C_BLUE + '\n링크 = ', list_url +C_RESET)

    
    if whichcom == "8" or whichcom == "everything":   #한국외식산업연구원
        list_url_list = {"https://www.kfiri.org/bbs/board.php?bo_table=report" : '한국외식산업연구원-정기연구보고서', "https://www.kfiri.org/bbs/board.php?bo_table=rnd" : '한국외식산업연구원-R&D 리포트'}
        dcoln = 0
        for list_url in list_url_list:
            tlist = []
            dlist = []
            ulist = []
            url = urllib.request.Request(list_url)
            result = urllib.request.urlopen(url).read().decode("utf-8")
            soup=BeautifulSoup(result, "html.parser") # 파싱하기  
            print('\n', C_BGRED + list_url_list[list_url] + C_RESET)
            
            title = soup.find_all('td', class_ = "list-subject")  # div태그 가져오기
            date1 = soup.find_all('td', class_ = "text-center en font-11")
            urllink = soup.find_all('td', class_ = "list-subject")
            
            for i,k in zip(title, urllink):
                title_re = i.get_text().strip()
                urllink2 = k.find("a")['href']
                urllink3 = '<a href="'+ urllink2 + '" rel="noopener" target="_blank">링크</a>'
                tlist.append(title_re)
                ulist.append(urllink3)
                
            for j in date1:
                dcoln = dcoln +1  # 사이트 게시판 내 컬럼 갯수
                if dcoln % 2 == 1:
                    date1_re = j.get_text().strip()
                    date2 = date1_re.replace('.', '-')
                    if date2[0] != '2':     # 첫번째 글자가 2가 아닐시 년도가 안 써있는 것으로 간주
                        date2='2021-'+date2   # 2021- 더해주기
                        if date2 >= todayd_re:
                            dlist.append(date2)
                    else:
                        if date2 >= todayd_re:
                            dlist.append(date2)
                    
            for a, b, c in zip(tlist, dlist, ulist):
                temp_dict = {'보고서명' : '', '출처' : '', '산업분류' : '', '분석 유형' : '', '보고서 유형' : '', '작성일자' : '', 'URL' : '', 'File' : ''}
                temp_dict['보고서명'] = a
                temp_dict['출처'] = "한국외식산업연구원"
                temp_dict['작성일자'] = b
                temp_dict['URL'] = c
                
                total_dict.append(temp_dict)
                            
            print(C_BOLD + C_BLUE + '\n링크 = ', list_url +C_RESET)
            

    # if whichcom == "9":   #한국무역협회   ####error: java 기반 URL이라 가져올 수가 없음
    #     list_url_list = {"https://www.kita.net/cmmrcInfo/rsrchReprt/rsrchReprt/rsrchReprtList.do" : '한국무역협회-연구보고서'}
    #     for list_url in list_url_list:
    #         url = urllib.request.Request(list_url)
    #         result = urllib.request.urlopen(url).read().decode("utf-8")
    #         soup=BeautifulSoup(result, "html.parser") # 파싱하기  
    #         print('\n', C_BGRED + list_url_list[list_url] + C_RESET)
    
    #         title = soup.find_all('a', class_ = "sbj")  # div태그 가져오기
    #         date1 = soup.find_all('span', class_ = "date")
    #         urllink = soup.find('div', class_ = "boardList type2")

    #         for i,j,k in zip(title, date1, urllink):
    #             temp_dict = {'title' : '', 'date' : '', 'url' : ''}
    #             title_re = i.get_text().strip()
    #             urllink2 = k.find("a")['href']
    #             urllink2 = urllink2.strip('javascript:fn_detail(1, ')
    #             urllink2 = urllink2.strip("')")
    #             urllink2 = urllink2.split(",'")
    #             urllink3 = "http://iit.kita.net/newtri2/report/iitreporter_view.jsp?sNo=" + urllink2[0] + "&sClassification=" + urllink2[1]
    #             date1_re = j.get_text().strip()
    #             date2 = date1_re.replace('.', '-')

                
    #             if date2 >= todayd_re:
    #                 temp_dict['title'] = title_re
    #                 temp_dict['date'] = date2
    #                 temp_dict['url'] = urllink
                    
    #                 total_dict.append(temp_dict)
                    
    #         pantable = pd.DataFrame(total_dict)
    #         print(pantable)
    #         print(C_BOLD + C_BLUE + '\n링크 = ', list_url +C_RESET)
            
    #         if list_url == "https://www.kita.net/cmmrcInfo/rsrchReprt/rsrchReprt/rsrchReprtList.do":
    #             pantable.to_excel(writer, sheet_name='한국무역협회-연구보고서', header=True)
    #             writer.save()



    if whichcom == "10" or whichcom == "everything":   #한국산업단지공단  ###ps:정기간행물을 포함시켜야 하나?
        list_url_list = {"https://www.kicox.or.kr/user/bbs/BD_selectBbsList.do?q_bbsCode=1020" : '한국산업단지공단-연구보고서'}
        dcoln = 0
        for list_url in list_url_list:
            tlist = []
            dlist = []
            ulist = []
            url = urllib.request.Request(list_url)
            result = urllib.request.urlopen(url).read().decode("utf-8")
            soup=BeautifulSoup(result, "html.parser") # 파싱하기  
            print('\n', C_BGRED + list_url_list[list_url] + C_RESET)
            
            title = soup.find_all('td', class_ = 'subject')  # div태그 가져오기
            date1 = soup.find('div', class_ = 'table').find_all('td')
            urllink = soup.find_all('td', class_ = 'subject')
            
            for i,k in zip(title, urllink):
                title_re = i.get_text().strip()
                urllink2 = k.find("a")['href']
                urllink3 = 'https://www.kicox.or.kr' + urllink2
                urllink4 = '<a href="'+ urllink3 + '" rel="noopener" target="_blank">링크</a>'
                tlist.append(title_re)
                ulist.append(urllink4)
            for j in date1:
                dcoln = dcoln +1
                if dcoln % 4 == 3:
                    date1_re = j.get_text().strip()
                    date2 = date1_re.replace('.', '-')
                    if date2 >= todayd_re:
                        dlist.append(date2)

                
            for a, b, c in zip(tlist, dlist, ulist):
                temp_dict = {'보고서명' : '', '출처' : '', '산업분류' : '', '분석 유형' : '', '보고서 유형' : '', '작성일자' : '', 'URL' : '', 'File' : ''}
                temp_dict['보고서명'] = a
                temp_dict['출처'] = '한국산업단지공단'
                temp_dict['작성일자'] = b
                temp_dict['URL'] = c
                
                total_dict.append(temp_dict)
                            
            print(C_BOLD + C_BLUE + '\n링크 = ', list_url +C_RESET)
        

    if whichcom == "11" or whichcom == "everything":   #한국인터넷진흥원
        list_url_list = {"https://www.kisa.or.kr/public/library/report_List.jsp" : '한국인터넷진흥원-연구보고서', "https://www.kisa.or.kr/public/library/IS_List.jsp" : "한국인터넷진흥원-KISA Report"}
        dcoln = 0
        for list_url in list_url_list:
            tlist = []
            dlist = []
            ulist = []
            url = urllib.request.Request(list_url)
            result = urllib.request.urlopen(url).read().decode("utf-8")
            soup=BeautifulSoup(result, "html.parser") # 파싱하기  
            print('\n', C_BGRED + list_url_list[list_url] + C_RESET)
            
            title = soup.find_all('td', class_ = 'lft')  # div태그 가져오기
            date1 = soup.find('tbody').find_all('td')
            urllink = soup.find_all('td', class_ = 'lft')
            
            for i,k in zip(title, urllink):
                title_re = i.get_text().strip()
                urllink2 = k.find("a")['href']
                urllink3 = 'https://www.kisa.or.kr' + urllink2
                urllink4 = '<a href="'+ urllink3 + '" rel="noopener" target="_blank">링크</a>'
                tlist.append(title_re)
                ulist.append(urllink4)
            for j in date1:
                dcoln = dcoln +1
                if dcoln % 4 == 3:
                    date1_re = j.get_text().strip()
                    date2 = date1_re.replace('.', '-')
                    if date2 >= todayd_re:
                        dlist.append(date2)

                
            for a, b, c in zip(tlist, dlist, ulist):
                temp_dict = {'보고서명' : '', '출처' : '', '산업분류' : '', '분석 유형' : '', '보고서 유형' : '', '작성일자' : '', 'URL' : '', 'File' : ''}
                temp_dict['보고서명'] = a
                temp_dict['출처'] = '한국인터넷진흥원'
                temp_dict['작성일자'] = b
                temp_dict['URL'] = c
                
                total_dict.append(temp_dict)
                            
            print(C_BOLD + C_BLUE + '\n링크 = ', list_url +C_RESET)
            


    if whichcom == "12" or whichcom == "everything":     # 한국정보통신산업연구원    ### 작성일자에 str이 섞여 나오는 경우 발생 ###
        list_url_list = {"http://www.kici.re.kr/%EC%A0%95%EB%B3%B4%ED%86%B5%EC%8B%A0%EC%82%B0%EC%97%85%EB%8F%99%ED%96%A5/" : '한국정보통신산업연구원-정보통신산업동향'}
        for list_url in list_url_list:
            url = urllib.request.Request(list_url)
            result = urllib.request.urlopen(url).read().decode("utf-8")
            soup=BeautifulSoup(result, "html.parser") # 파싱하기  
            print('\n', C_BGRED + list_url_list[list_url] + C_RESET)
    
            title = soup.find_all('div', class_ = 'cut_strings')  # div태그 가져오기
            date1 = soup.find('tbody').find_all('td', class_ = "kboard-list-date")
            urllink = soup.find_all('div', class_= 'cut_strings')  # 가장 큰 틀부터 찾고, 세부적인 틀 find_all로 찾
    
            for i,j,k in zip(title, date1, urllink):
                temp_dict = {'보고서명' : '', '출처' : '', '산업분류' : '', '분석 유형' : '', '보고서 유형' : '', '작성일자' : '', 'URL' : '', 'File' : ''}
                title_re = i.get_text().strip()
                date1_re = j.get_text().strip()
                date2 = date1_re.replace('.', '-')
                urllink2 = k.find("a")["href"]
                urllink3 = "http://www.kici.re.kr" + urllink2
                urllink4 = '<a href="'+ urllink3 + '" rel="noopener" target="_blank">링크</a>'
                
                if date2 >= todayd_re:
                    temp_dict['보고서명'] = title_re
                    temp_dict['출처'] = '한국정보통신산업연구원'
                    temp_dict['작성일자'] = date2
                    temp_dict['URL'] = urllink4
                    
                    total_dict.append(temp_dict)
                    
            print(C_BOLD + C_BLUE + '\n링크 = ', list_url +C_RESET)

                
    if whichcom == "13" or whichcom == "everything":  #한국출판문화산업진흥원   ####뭐지 왜 안돼지 #####
        list_url_list = {"http://www.kpipa.or.kr/info/studyrepotList.do?board_id=51" : '한국출판문화산업진흥원-조사연구 보고서'}
        for list_url in list_url_list:
            url = urllib.request.Request(list_url)
            result = urllib.request.urlopen(url).read().decode("utf-8")
            soup=BeautifulSoup(result, "html.parser") # 파싱하기
            print('\n', C_BGRED + list_url_list[list_url] + C_RESET)
    
            title = soup.find_all('td', class_ = 'title')  # div태그 가져오기
            date1 = soup.find_all('td', class_ = "postDay")
            urllink = soup.find_all('td', class_= 'title')  # 가장 큰 틀부터 찾고, 세부적인 틀 find_all로 찾
    
            for i,j,k in zip(title, date1, urllink):
                temp_dict = {'보고서명' : '', '출처' : '', '산업분류' : '', '분석 유형' : '', '보고서 유형' : '', '작성일자' : '', 'URL' : '', 'File' : ''}
                title_re = i.get_text().strip()
                date1_re = j.get_text().strip()
                date2 = date1_re.replace('.', '-')
                urllink2 = k.find("a")["onclick"]
                urllink2 = urllink2.strip('goView(')
                urllink2 = urllink2.strip(')')
                urllink2 = urllink2.split(', ')
                urllink3 = 'http://www.kpipa.or.kr/info/studyrepotView.do?board_id=51&article_id=' + urllink2[0] + '&pageInfo.page=&search_cond=&search_text=&list_no=' + urllink2[1]
                urllink4 = '<a href="'+ urllink3 + '" rel="noopener" target="_blank">링크</a>'
                
                if date2 >= todayd_re:
                    temp_dict['보고서명'] = title_re
                    temp_dict['출처'] = "한국출판문화산업진흥원"
                    temp_dict['작성일자'] = date2
                    temp_dict['URL'] = urllink4
                    
                    total_dict.append(temp_dict)
                    
            print(C_BOLD + C_BLUE + '\n링크 = ', list_url +C_RESET)

                
# =============================================================================
#     if whichcom == "14":   # 서울디지털재단         ########### 서울 디지털 재단 홈페이지 리뉴얼되었음. 따로 손봐서 수정하는 것이 필요할 예정 #######     ##### 새 웹사이트 주소   https://sdf.seoul.kr/index   ########
#         list_url_list = {"https://sdf.seoul.kr/web/pages/gc18621b.do" : '서울디지털재단-정기간행물', 'https://sdf.seoul.kr/web/pages/gc4491b.do' : '서울디지털재단-연구보고서'}
#         dcoln = 0
#         for list_url in list_url_list:
#             tlist = []
#             dlist = []
#             ulist = []
#             url = urllib.request.Request(list_url)
#             result = urllib.request.urlopen(url).read().decode("utf-8")
#             soup=BeautifulSoup(result, "html.parser") # 파싱하기  
#             print('\n', C_BGRED + list_url_list[list_url] + C_RESET)
#             
#             title = soup.find_all('td', class_ = 'tt le')  # div태그 가져오기
#             date1 = soup.find('tbody').find_all('td')
#             urllink = soup.find_all('td', class_ = 'tt le')
#             
#             for i,k in zip(title, urllink):
#                 title_re = i.get_text().strip()
#                 urllink2 = k.find("a")['href']
#                 urllink2 = urllink2.strip("javascript:fn_select_view('")
#                 urllink2 = urllink2.strip("')")
#                 urllink2 = urllink2.split("','")
#                 urllink3 = 'https://sdf.seoul.kr/web/pages/gc18621b.do?bbsFlag=View&bbsId=' + urllink2[0] + '&nttId=' + urllink2[1] + '&bbsTyCode=&bbsAttrbCode=&authFlag=&pageIndex=1'
#                 urllink4 = '<a href="'+ urllink3 + '" rel="noopener" target="_blank">링크</a>'
#                 tlist.append(title_re)
#                 ulist.append(urllink4)
#             for j in date1:
#                 dcoln = dcoln +1
#                 if dcoln % 5 == 4:
#                     date1_re = j.get_text().strip()
#                     date2 = date1_re.replace('.', '-')
#                     if date2 >= todayd_re:
#                         dlist.append(date2)
# 
#                 
#             for a, b, c in zip(tlist, dlist, ulist):
#                 temp_dict = {'보고서명' : '', '출처' : '', '산업분류' : '', '분석 유형' : '', '보고서 유형' : '', '작성일자' : '', 'URL' : '', 'File' : ''}
#                 temp_dict['보고서명'] = a
#                 temp_dict['출처'] = '서울디지털재단'
#                 temp_dict['작성일자'] = b
#                 temp_dict['URL'] = c
#                 
#                 total_dict.append(temp_dict)
# 
#             print(C_BOLD + C_BLUE + '\n링크 = ', list_url +C_RESET)
# =============================================================================
        
    if whichcom=="15" or whichcom == "everything":       # 한국문화관광연구원
        list_url_list = {"https://www.kcti.re.kr/web/board/boardContentsListPage.do?board_id=2" : '한국문화관광연구원-연구보고서', 'https://sdf.seoul.kr/web/pages/gc4491b.do' : '서울디지털재단-연구보고서'}
        for list_url in list_url_list:
            tlist = []
            dlist = []
            ulist = []
            url = urllib.request.Request(list_url)
            result = urllib.request.urlopen(url).read().decode("utf-8")
            soup=BeautifulSoup(result, "html.parser") # 파싱하기  
            print('\n', C_BGRED + list_url_list[list_url] + C_RESET)
            
            title = soup.select('div#contentsList > ul > h4')  # div태그 가져오기
            date1 = soup.select('tl#name > dd')
            urllink = soup.select('li > a')

            for i,k in zip(title, urllink):
                title_re = i.get_text().strip()
                urllink2 = k['href']
                urllink2 = urllink2.strip("javascript:contentsView(")
                urllink2 = urllink2.strip("')")
                urllink3 = 'https://www.kcti.re.kr/web/board/boardContentsView.do?miv_pageNo=&miv_pageSize=&total_cnt=&LISTOP=&mode=W&contents_id=' + urllink2 + '&board_id=2&report_start_year=&cate_id=&etc10=&searchkey=ALL&searchtxt=&link_g_topmenu_id=15f51238586a425'
                urllink4 = '<a href="'+ urllink3 + '" rel="noopener" target="_blank">링크</a>'
                tlist.append(title_re)
                ulist.append(urllink4)
            for j in date1:
                dcoln = dcoln +1
                if dcoln % 5 == 4:
                    date1_re = j.get_text().strip()
                    date2 = date1_re.replace('.', '-')
                    if date2 >= todayd_re:
                        dlist.append(date2)

                
            for a, b, c in zip(tlist, dlist, ulist):
                temp_dict = {'보고서명' : '', '출처' : '', '산업분류' : '', '분석 유형' : '', '보고서 유형' : '', '작성일자' : '', 'URL' : '', 'File' : ''}
                temp_dict['보고서명'] = a
                temp_dict['출처'] = '서울디지털재단'
                temp_dict['작성일자'] = b
                temp_dict['URL'] = c
                
                total_dict.append(temp_dict)

            print(C_BOLD + C_BLUE + '\n링크 = ', list_url +C_RESET)
            expantable = pd.DataFrame(total_dict)
            print(expantable)
        

    pantable = pd.DataFrame(total_dict)            
            

#####################################################################

    letscheck = pd.read_excel('E:/Folder/data/kicpantdata/kicpaUPLOADdragon.xlsx')

    for ctitle_index in range(len(pantable)):
        for atitle_index in range(len(letscheck)):
            if pantable['보고서명'][ctitle_index] in letscheck['보고서명'][atitle_index]:
                print(pantable['보고서명'][ctitle_index], '   =   ', letscheck['보고서명'][atitle_index])
                drop_list.append(ctitle_index)

    pantable2 = pantable.drop(drop_list)

#####################################################################
        
#### maybe its not working due to the fact that the excel file and python pandas are not compatible to each other #####
    print(pantable2)
    pantable2.to_excel(writer, sheet_name='TOTAL', header=True, index=False)
        
    writer.save()

    

mergeq()




### 제목과 날짜 출력되는 것 dictionary로 받기

######## 엑셀 파일에서 겹치는 것은 받아오지 않는 것으로 쿼리 한번 작성해보자 ########

####### VERY IMPORTANT!!!!! urllink4 만들어서 '<a href="'+ i + '" rel="noopener" target="_blank">링크</a>' 이거 더하는 것도 나쁘지 않을 듯 ###### 
