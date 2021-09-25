from rest_framework import generics
from .serializers import SingleStatisticSerializer, StatisticSerializer, StatisticListSerializer
from .models import Statistic
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.decorators import api_view


class StatisticCreateView(generics.CreateAPIView):
    serializer_class = SingleStatisticSerializer

# @api_view(['POST'])
# def statistic_view(request):
#     date_from = request.data.get('date_from')
#     date_to = request.data.get('date_to')
#     queryset = Statistic.objects.filter(
#         Q(date__gte=date_from) & Q(date__lte=date_to)
#     )
#     # print(queryset)
#     serializer = StatisticListSerializer(queryset, many=True)
#     # print('-----data--', serializer.data)
#     return Response(serializer.data)


class StatisticListView(generics.ListAPIView):
    serializer_class = StatisticSerializer
    queryset = Statistic.objects.all()

    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        date_from = self.request.data.get('date_from')
        date_to = self.request.data.get('date_to')
        queryset = Statistic.objects.filter(
            Q(date__gte=date_from) & Q(date__lte=date_to)
        )
        return queryset


    def list(self, request, *args, **kwargs):
        # print('-----req--', request.data)
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    

    # def show_stats(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=False)
    #     # headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    
    # def list(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)