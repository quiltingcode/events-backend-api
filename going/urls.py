from django.urls import path
from going import views

urlpatterns = [
    path('going/', views.GoingList.as_view()),
    path('going/<int:pk>/', views.GoingDetail.as_view()),
]
