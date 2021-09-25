from rest_framework import serializers
from .models import Statistic
from statistic_project.settings import DATE_INPUT_FORMATS, DATE_FORMAT
from loguru import logger
from django.db.models import Q

# logger.add('debug.log', level='DEBUG', format='{time} {level} {message}')


class SingleStatisticSerializer(serializers.ModelSerializer):
    date = serializers.DateField(
        format=DATE_FORMAT,
        input_formats=DATE_INPUT_FORMATS
        )
    class Meta:
        model = Statistic
        fields = ['date', 'clicks', 'cost', 'views']

    def create(self, validated_data):
        logger.debug(validated_data)
        clicks = validated_data.get('clicks')
        cost = validated_data.get('cost')
        views = validated_data.get('views')
        logger.debug(clicks)

        if cost and clicks:
            cpc = cost / clicks
        else:
            cpc = None

        if cost and views:
            cpm = cost / views * 1000
        else:
            cpm = None

        single_statistic = Statistic(
            date=validated_data['date'],
            views=views,
            clicks=clicks, 
            cost=cost, 
            cpc=cpc,
            cpm=cpm
            )

        single_statistic.save()
        return single_statistic


class StatisticListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
        fields = '__all__'
    

class StatisticSerializer(serializers.Serializer):
    date_from = serializers.DateField(
        format=DATE_FORMAT,
        input_formats=DATE_INPUT_FORMATS
    )
    date_to = serializers.DateField(
        format=DATE_FORMAT,
        input_formats=DATE_INPUT_FORMATS
    )
    
    # sort_field = serializers.CharField()
    class Meta:
        model = Statistic
        fields = '__all__'

    # def to_internal_value(self, data):
    #     # print('--------', data)
    #     date_from = data.get('date_from')
    #     date_to = data.get('date_to')
    #     # print('------', date_from, date_to)
    #     #Валидация
    #     return {
    #         'date_from': date_from,
    #         'date_to': date_to
    #     }

    # def create(self, validated_data):
    #     print('---val-data---', validated_data)
    #     # return Statistic.objects.filter(
    #     #     date__gte=validated_data['date_from'],
    #     return None
    #     #     )
    
    # def to_representation(self, values):
    #     print('-----val--', values)
    #     # date_from = values.get('date_from')
    #     # date_to = values.get('date_to')
    #     # queryset = Statistic.objects.filter(
    #     #     Q(date__gte=date_from) & Q(date__lte=date_to)
    #     # )
    #     # print('----Qs-----', queryset)
    #     serializer = StatisticListSerializer(values)
    #     return serializer.data
    #     # return {'success': True}

    # def to_representation(self, instance):
    #     print('---ins---', instance)
    #     serializer = StatisticListSerializer(instance, many=True)
    #     print('----res---', serializer.data)
    #     return serializer.data