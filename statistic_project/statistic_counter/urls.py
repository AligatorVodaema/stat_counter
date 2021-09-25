from django.urls import path
from .views import StatisticCreateView, StatisticListView


urlpatterns = [
    path('create/', StatisticCreateView.as_view()),
    path('view_stat/', StatisticListView.as_view())
]



