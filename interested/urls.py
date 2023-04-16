from django.urls import path
from interested import views

urlpatterns = [
    path('interested/', views.InterestedList.as_view()),
    path('interested/<int:pk>/', views.InterestedDetail.as_view()),
]
