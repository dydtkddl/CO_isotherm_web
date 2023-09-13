from django.shortcuts import render, redirect
from django.http import HttpResponse , JsonResponse 
from django.forms.models import model_to_dict 
from .data import *
# Create your views here.

def home(request):
  return render(request, "app/home.html")

## 모델들의 각셀에 데이터프레임같은 복잡한 데이터가 들어갈때, 역직렬화를 사용하자

## Users -> UnionData -> Datas -> Data가 외래키로 1:N관계로 엮어지게 만들자.
## 임시 유저는 코드로 Users테이블에 잠시 이름을 올리되, 단기간내에 삭제하는 코드를 만들자

# NIST데이터를 크롤링해서 각 흡착 가스들에 대한 메타데이터(분자량) 온도에 따른 밀도 데이터같은 것들을
# 고정 테이블 화 하자.

# 시각화는 Chart.Js로 예쁘게 만들자