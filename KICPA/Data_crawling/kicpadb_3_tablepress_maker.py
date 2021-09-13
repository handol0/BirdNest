import pandas as pd


###### kicpadb.com에 전체 테이블 import 용으로 활용 #######

###### 업로드 전용 xlsx 파일인 kicpaUPLOADdragon.xlsx 를 만드는 쿼리 ######
###### 전체 내용이 들어가고, dummy가 빠진 버전을 만드는 것  ######


# 업종별 분류 디렉토리
catdir = {'E:/Folder/data/kicpantdata/financial/bank/bank-all.xlsx' : '금융산업/은행',
          'E:/Folder/data/kicpantdata/financial/insurance/insurance-all.xlsx' : '금융산업/보험',
          'E:/Folder/data/kicpantdata/financial/stock/stock-all.xlsx' : '금융산업/증권',
          'E:/Folder/data/kicpantdata/financial/card/card-all.xlsx' : '금융산업/신용카드',
          'E:/Folder/data/kicpantdata/financial/other/financial-other-all.xlsx' : '금융산업/기타',
          'E:/Folder/data/kicpantdata/cpnr/cloth/cloth-all.xlsx' : '소비재산업/의류업',
          'E:/Folder/data/kicpantdata/cpnr/cosmetic/cosmetic-all.xlsx' : '소비재산업/화장품',
          'E:/Folder/data/kicpantdata/cpnr/distribute/delive/delive-all.xlsx' : '소비재산업/유통업/택배',
          'E:/Folder/data/kicpantdata/cpnr/distribute/departs/departs-all.xlsx' : '소비재산업/유통업/백화점',
          'E:/Folder/data/kicpantdata/cpnr/distribute/discounts/discounts-all.xlsx' : '소비재산업/유통업/대형할인점',
          'E:/Folder/data/kicpantdata/cpnr/distribute/distribute-other/distribute-other-all.xlsx' : '소비재산업/유통업/기타',
          'E:/Folder/data/kicpantdata/cpnr/food/food-all.xlsx' : '소비재산업/식품업',
          'E:/Folder/data/kicpantdata/cpnr/other/cpnr-other-all.xlsx' : '소비재산업/기타',
          'E:/Folder/data/kicpantdata/service/edu/edu-all.xlsx' : '서비스업/교육',
          'E:/Folder/data/kicpantdata/service/hotel/hotel-all.xlsx' : '서비스업/호텔',
          'E:/Folder/data/kicpantdata/service/realest/realest-all.xlsx' : '서비스업/부동산',
          'E:/Folder/data/kicpantdata/service/restaurant/restaurant-all.xlsx' : '서비스업/요식업',
          'E:/Folder/data/kicpantdata/service/sports/sports-all.xlsx' : '서비스업/레저',
          'E:/Folder/data/kicpantdata/service/tour/tour-all.xlsx' : '서비스업/관광',
          'E:/Folder/data/kicpantdata/service/other/service-other-all.xlsx' : '서비스업/기타',
          'E:/Folder/data/kicpantdata/bio/medicine/medicine-all.xlsx' : '제약·바이오/제약',
          'E:/Folder/data/kicpantdata/bio/bio/bio-all.xlsx' : '제약·바이오/바이오',
          'E:/Folder/data/kicpantdata/bio/hcare/hcare-all.xlsx' :'제약·바이오/헬스케어',
          'E:/Folder/data/kicpantdata/manufacturing/army/army-all.xlsx' : '제조업/방위산업',
          'E:/Folder/data/kicpantdata/manufacturing/car/car-all.xlsx' : '제조업/자동차',
          'E:/Folder/data/kicpantdata/manufacturing/const/const-all.xlsx' : '제조업/건설업',
          'E:/Folder/data/kicpantdata/manufacturing/engineering/engineering-all.xlsx' : '제조업/엔지니어링',
          'E:/Folder/data/kicpantdata/manufacturing/machinery/machinery-all.xlsx' : '제조업/기계장비',
          'E:/Folder/data/kicpantdata/manufacturing/medeq/medeq-all.xlsx' : '제조업/의료기기',
          'E:/Folder/data/kicpantdata/manufacturing/paper/paper-all.xlsx' : '제조업/제지산업',
          'E:/Folder/data/kicpantdata/manufacturing/ship/ship-all.xlsx' : '제조업/조선해양',
          'E:/Folder/data/kicpantdata/manufacturing/soc/soc-all.xlsx' : '제조업/SOC',
          'E:/Folder/data/kicpantdata/manufacturing/other/manufacturing-other-all.xlsx' : '제조업/기타',
          'E:/Folder/data/kicpantdata/it/ai/ai-all.xlsx' : 'IT·미디어·통신/인공지능',
          'E:/Folder/data/kicpantdata/it/commo/commo-all.xlsx' : 'IT·미디어·통신/통신기술',
          'E:/Folder/data/kicpantdata/it/dataind/dataind-all.xlsx' : 'IT·미디어·통신/데이터',
          'E:/Folder/data/kicpantdata/it/display/display-all.xlsx' : 'IT·미디어·통신/디스플레이',
          'E:/Folder/data/kicpantdata/it/ecommerce/ecommerce-all.xlsx' : 'IT·미디어·통신/이커머스',
          'E:/Folder/data/kicpantdata/it/electro/electro-all.xlsx' : 'IT·미디어·통신/전자',
          'E:/Folder/data/kicpantdata/it/media/game/game-all.xlsx' : 'IT·미디어·통신/미디어/게임',
          'E:/Folder/data/kicpantdata/it/media/movie/movie-all.xlsx' : 'IT·미디어·통신/미디어/영화',
          'E:/Folder/data/kicpantdata/it/media/music/music-all.xlsx' : 'IT·미디어·통신/미디어/음악',
          'E:/Folder/data/kicpantdata/it/media/other/media-other-all.xlsx' : 'IT·미디어·통신/미디어/기타',
          'E:/Folder/data/kicpantdata/it/semicon/semicon-all.xlsx': 'IT·미디어·통신/반도체',
          'E:/Folder/data/kicpantdata/it/sns/sns-all.xlsx' : 'IT·미디어·통신/포탈',
          'E:/Folder/data/kicpantdata/it/other/it-other-all.xlsx' : 'IT·미디어·통신/기타',
          'E:/Folder/data/kicpantdata/energy/airline/airline-all.xlsx' : '에너지·자원/항공',
          'E:/Folder/data/kicpantdata/energy/chemic/chemic-all.xlsx' : '에너지·자원/화학',
          'E:/Folder/data/kicpantdata/energy/energy/energy-all.xlsx' : '에너지·자원/에너지',
          'E:/Folder/data/kicpantdata/energy/nosteel/nosteel-all.xlsx' : '에너지·자원/비철금속',
          'E:/Folder/data/kicpantdata/energy/steel/steel-all.xlsx' : '에너지·자원/철강',
          'E:/Folder/data/kicpantdata/energy/shipping/shipping-all.xlsx' : '에너지·자원/해운',
          'E:/Folder/data/kicpantdata/energy/other/energy-other-all.xlsx' : '에너지·자원/기타'}


indall = pd.read_excel('E:/Folder/data/kicpantdata/kicpabird.xlsx')


for xyz in catdir:
    writer =  pd.ExcelWriter(xyz)
    
    indnorm1 = indall["산업분류"].str.contains(catdir[xyz])
    indnorm = indall[indnorm1]

    indnorm.to_excel(writer, sheet_name='New', header=True, index=False)
    writer.save()


#####  전체 데이터베이스(즉, 보여주는 용도) 업로드용 ######
    
ind_sav = indall[indall['보고서명'] == 'i am a dummy'].index
indall2 = indall.drop(ind_sav)

writer2 = pd.ExcelWriter('E:/Folder/data/kicpantdata/kicpaUPLOADdragon.xlsx')
indall2.to_excel(writer2, sheet_name='DummyFree', header=True, index=False)
writer2.save()

print("completed")
