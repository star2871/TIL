# from django.urls import path
# from accountapp.views import hello_world, hello_world_drf
# from . import views
# urlpatterns = [
#     path('', views.hello_world, name='hello_world'),
#     path('hello_world_drf', hello_world_drf),
# ]
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns =[
    path('blog/', views.BlogList.as_view()),
    path('blog/<int:pk>/', views.BlogDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)