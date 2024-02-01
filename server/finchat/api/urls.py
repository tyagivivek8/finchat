from django.urls import path
from .views import process_api

urlpatterns = [
    path('chatbot/', process_api, name="chatbotApi")
]