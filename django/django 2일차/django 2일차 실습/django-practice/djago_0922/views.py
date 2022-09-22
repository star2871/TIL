from django.shortcuts import render
import random
import numpy as np


# Create your views here.
def dinner(request):

    foods = ['삼겹살', '치킨', '피자', '파스타', '감자탕']
    images ={
      '삼겹살': 'https://cdn.mindgil.com/news/photo/202103/70839_7148_1250.jpg',
      '치킨': 'http://www.bhc.co.kr/upload/bhc/menu/410x271_view_%EC%B9%98%ED%90%81%EB%8B%B9%ED%95%9C%EB%A7%88%EB%A6%AC(0).png',
      '피자': 'https://w.namu.la/s/8c2aebf04d4c6e0ae24ebf3b3789cb064f353da40f0a2916630ee33cc34742414ac8427b8765569e84d615a24cac7bc389ada2e5c60579541ea8b41be9b22db6d0ce58f59fd1ac01912436c928605cd86974e360258a66ac0374662e70b0ae73',
      '파스타': 'https://static.wtable.co.kr/image/production/service/recipe/1802/9c556903-01f9-4850-bcf8-1f9c62a0d680.jpg?size=1050x590',
      '감자탕': 'https://recipe1.ezmember.co.kr/cache/recipe/2018/12/05/ae4988aeb11d9351478f37168b19f4b41.jpg'
    }
    food = random.choice(foods)
    
    image = images[food]

    context ={
        'food': food,
        'image':image
    }
    return render(request, 'dinner.html', context)


def lotto(request):
  win = [3, 11, 15, 29, 35, 44, 10]
  bonus = 10
  cnt = 0
  cnts = []
  res = []

  for i in range(5):
    numbers = []
    
    while(len(numbers) < 6):
      x = random.randint(1, 46)
      
      if (x not in numbers):
        numbers.append(x)
    
    res.append(numbers)

  for nums in res:
    cnt = 0
    for num in nums:
      
      if num in win:
        cnt += 1
    cnts.append(cnt)
  
  ranks = []
  
  for i in range(len(cnts)):
    if cnts[i] == 6: ranks.append('1등') 
    elif cnts[i] == 5 and bonus in res[i]:
      ranks.append('2등')
    elif cnts[i] == 5:
      ranks.append('3등')
    elif cnts[i] == 4:
      ranks.append('4등')
    elif cnts[i] == 3:
      ranks.append('5등')
    else:
      ranks.append("꽝!")

  context = {
    'lotto': res,
    'ranks':ranks,
  }
  
  return render(request, 'lotto.html', context)



    