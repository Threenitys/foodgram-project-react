from rest_framework import serializers
import constants


def validate_cooking_time(cooking_time):
    if int(cooking_time) < constants.MIN_COOKING_TIME:
        raise serializers.ValidationError(
            'Время приготовления должно быть больше 0!'
        )
