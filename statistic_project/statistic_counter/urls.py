from django.urls import path
from .views import StatisticCreateView, StatisticListView, delete_all_statistics


urlpatterns = [
    path('create/', StatisticCreateView.as_view(), name='create'),
    path('view_stat/', StatisticListView.as_view(), name='view_stat'),
    path('del_all_stat/', delete_all_statistics, name='del_stat')
]



