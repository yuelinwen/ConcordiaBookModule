from django.urls import path
from . import views 

urlpatterns = [
    path('', views.TextbookListView.as_view(), name='textbook_list'),
    path('add/', views.add_book, name='add_book'),
    path('<str:course_code>/', views.TextbookListView.as_view(), name='textbook_by_course'),
]