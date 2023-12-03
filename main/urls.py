from django.urls import path, include
from .views import Calendar, Reserve
urlpatterns = [
    path('calendar/<int:residence_id>', Calendar.as_view()),
    path('reserve', Reserve.as_view()),
]
