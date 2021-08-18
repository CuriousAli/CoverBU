from rest_framework import serializers
from cbu_app.models import CBU


class CBUSerializer(serializers.ModelSerializer):
    class Meta:
        model = CBU
        fields = ('unit', 'reach')

    def validate(self, data):
        reach_array = data['reach']

        prev_number = 101

        if len(reach_array) != 10:
            raise serializers.ValidationError("Reach need to contain ten elements")

        if data['unit'] < 0:
            raise serializers.ValidationError("Unit must be bigger or equal zero")

        for elem in reach_array:

            try:
                check_number = float(elem)
                return check_number
            except ValueError:
                raise serializers.ValidationError("All element must be integer or float numbers")

        for elem in reach_array:

            check_number = float(elem)

            if 0 > check_number or check_number > 100:
                raise serializers.ValidationError("All elements of reach field must be positive number and less or "
                                                  "equal than 100")

            if check_number >= prev_number:
                raise serializers.ValidationError("One of elements from 'reach' is bigger than previous")

            prev_number = check_number

