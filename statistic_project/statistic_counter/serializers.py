from rest_framework import serializers
from .models import Statistic
from statistic_project.settings import DATE_INPUT_FORMATS, DATE_FORMAT
from loguru import logger


class SingleStatisticSerializer(serializers.ModelSerializer):
    date = serializers.DateField(
        label='Дата',
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


class StatisticSerializer(serializers.ModelSerializer):
    date_from = serializers.DateField(
        required=True,
        allow_null=False,
        format=DATE_FORMAT,
        input_formats=DATE_INPUT_FORMATS,
        write_only=True
    )
    date_to = serializers.DateField(
        required=True,
        allow_null=False,
        format=DATE_FORMAT,
        input_formats=DATE_INPUT_FORMATS,
        write_only=True
    )
    class Meta:
        model = Statistic
        extra_kwargs = {
            'date': {'read_only': True},
            'views': {'read_only': True},
            'clicks': {'read_only': True},
            'cost': {'read_only': True},
            'cpc': {'read_only': True},
            'cpm': {'read_only': True}
        }
        exclude = ('id',)
    