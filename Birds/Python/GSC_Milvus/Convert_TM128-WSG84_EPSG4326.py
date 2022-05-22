#Code :  https://domdom.tistory.com/entry/pandas-%EC%A2%8C%ED%91%9C%EA%B3%84-xy%ED%96%89-%EB%AA%A8%EB%91%90-%EB%8B%A4%EB%A5%B8-%EC%A2%8C%ED%91%9C%EA%B3%84%EB%A1%9C-%EB%B3%80%EA%B2%BD%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95
#Tableau Description :  http://www.datavisualization.co.kr/%ED%83%9C%EB%B8%94%EB%A1%9C-utm-k-%EC%A2%8C%ED%91%9C-%EA%B0%92%EC%9D%84-%EC%9D%B4%EC%9A%A9%ED%95%B4-%EC%A7%80%EB%8F%84%EB%A1%9C-%ED%91%9C%ED%98%84%ED%95%98%EA%B8%B0/

from pyproj import Proj, transform
 
##TM128 변환기 설정 
TM128 = {'proj':'tmerc', 'lat_0':'38N', 'lon_0':'128E', 'ellps':'bessel', 'x_0':'400000', 'y_0':'600000', 'k':'0.9999', 'towgs84':'-146.43,507.89,681.46'}


wgs84=Proj(init='epsg:4326')
 

 #963775 와 1941125에 들어갈 알맞은 값 가져오기
transform(Proj(**TM128), wgs84, 963775,1941125)

