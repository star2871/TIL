import sys
import os
import django
sys.dont_write_bytecode = True
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from db.models import *

# 아래에 코드를 기록하세요.
# 코드 실행은 터미널에서 shell을 실행시켜서 해주세요. 
# $ python manage.py shell_plus

import datetime
artist = Artist()
artist.name = '브루노마스'
artist.debut = datetime.date(2010, 10, 4)
artist.save()
