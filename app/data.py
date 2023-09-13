import pandas as pd
class Data:
  def __init__(self, setting):
    self.setting = setting #setting의 키값은 ["set_temp", "transform_unit", "gas_name"]
    # self.density_of_gas = data베이스를 뒤져서 찾는 구문
    # self.MW_of_gas = data베이스를 뒤져서 찾는 구문
  def set_Data(self, df): # df의 열이름은 X, Y
    self.original_data = df
  
  def TransformOriginalData(self):
    ## self.original_data랑 self.density_of_gas랑 MW를 이용해 변환
    # self.TransformOriginalData = transformed_DF할당
    return 
  def reset_transform_unit(self, new_unit):
    return 

class Datas: # 새로운 온도 범위에 데이터 추가되면 자동으로 생성
  def __init__(self,setting):
    self.setting = setting
    self.datas = {}
    self.union_data = None 
    self.fitting_data = None 
    self.inverse_regression_info = None
    return
  def append(self, name, Data):
    ## if self.setting == Data.setting
    self.datas[name] = Data
    ## self.change_union_data(Data)
  def change_union_data(self, Data):
    # 추가되는 Data를 평균과 표준편차에 반영하는 코드
    return 
  def fitting_data(self, method_setting):
    ## if method_setting["initial_parameter"]
    ##    사전 파라미터 토대로 피팅
    ## else
    ##    자동 피팅
    ## inverse_regression_info값이 있으면 삭제하고 None으로 만들어주는 코드
    return ## 피팅파라미터 딕셔너리(로스값 포함)
  def set_inverse_regression_info(self):
    ## union_data를 통해서 다항회귀 곡선 정보 구하고 
    ## self.inverse_regression_info에 반영{ 차수, 계수리스트 , R^2}
    return
class Union_Data:
  def __init__(self):
    self.union_datas ={"temp" : {}}
    self.inverse_info =None
    self.range = {}
    self.inverse_result = None
    self.predict_result = None
    self.result = None
  def set_range(self): ## union_datas안의 데이터가 조금이라도 바뀔때마다 호출되어야함
    #datas의 모든 Datas객체들의 union_data들의 첫번째 N과 마지막 N을 가지고 range를 구해서, P의 range N의 range를 구한다
   #range멤버변수의 값을 바꾼다
    return
  def get_inverse_info(self):
    '''각 온도의 Datas객체에서 inverse_regression_info가 있으면 Datas.set_inverse_regression_info함수를 호출하지 않고 없으면 호출하는 코드
    return 인버스 정보'''
    return
  def predict(self):
    ''' get_inverse() > 인버스정보와 ,range정보를 통해서
     range의 동일 간격으로 동일 N 구간에서 P예측
    lnP를 구하고, 온도별 조합을 통해서 평균 흡착열 도출, sTDEV값 도출'''
    return 
  def get_xlsx(self):
    return

    
    

  
    

  