from django.urls import path
from . import views 

urlpatterns = [
    path('', views.TextbookListView.as_view(), name='textbook_list'),
    path('<str:course_code>/', views.TextbookListView.as_view(), name='textbook_by_course'),
    path('add/', views.TextbookListView.as_view(), name='add_book'),
]