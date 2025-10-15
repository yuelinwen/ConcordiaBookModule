from django.urls import path
from . import views 

urlpatterns = [
    path('', views.TextbookListView.as_view(), name='textbook_list'),
    # path('',views.index, name='index'),
]