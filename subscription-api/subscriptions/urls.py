from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from subscriptions import views

urlpatterns = [
    path('subscriptions/', views.SubscriptionList.as_view()),
    path('subscriptions/<int:pk>/', views.SubscriptionDetail.as_view()),
     path('metadata/', views.metadataList.as_view()),
    path('metadata/<int:pk>/', views.metadataDetail.as_view()),
]
