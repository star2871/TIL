from django.shortcuts import render
import random
import numpy as np


# Create your views here.
def dinner(request):

    foods = ['삼겹살', '치킨', '피자', '파스타', '감자탕']

    food = random.choice(foods)
    

    context ={
        'food': food,
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



    