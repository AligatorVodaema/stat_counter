from rest_framework import filters
from rest_framework import generics
from .serializers import SingleStatisticSerializer, StatisticSerializer
from .models import Statistic
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.decorators import api_view


class StatisticCreateView(generics.CreateAPIView):
    """
    'View' for create one instance of statistic.
    """
    serializer_class = SingleStatisticSerializer


class StatisticListView(generics.ListCreateAPIView):
    """
    Takes two fields date_from and date_to, to
    return statistic for this date range.
    Also have filter for ordering on fields.
    """
    serializer_class = StatisticSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ('date', 'views', 'clicks', 'cost', 'cpc', 'cpm')
    ordering = ('date')

    def post(self, request, *args, **kwargs):
        return self.show_stats(request, *args, **kwargs)

    def get_queryset(self):
        """
        Special queryset for date range.
        """
        date_from = self.request.data.get('date_from')
        date_to = self.request.data.get('date_to')
        queryset = Statistic.objects.filter(
            Q(date__gte=date_from) & Q(date__lte=date_to)
        )
        return queryset

    def show_stats(self, request, *args, **kwargs):
        """
        Serialization, validation and filtering process.
        Returns serialized statistic for client.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, 
            status=status.HTTP_200_OK, 
            headers=headers
        )


@api_view(['DELETE'])
def delete_all_statistics(_):
    result = Statistic.objects.all().delete()
    return Response(
        {'success': True, 'deleted items': result[0]},
         status=status.HTTP_204_NO_CONTENT
    )
    