from rest_framework import serializers
from cbu_app.models import CBU


# serializer for CBU model
class CBUSerializer(serializers.ModelSerializer):
    class Meta:
        model = CBU
        fields = ('unit', 'reach')

    # Unit value must be positive integer
    def validate_unit(self, value):
        if value < 0:
            raise serializers.ValidationError("Unit must be bigger or equal zero")
        return value

    # Validation of reach field
    def validate(self, data):
        reach_string = data['reach']
        reach_array = reach_string.split(',')

        # All elements must be float or integers
        try:
            last_elem = float(reach_array[-1])
        except ValueError:
            raise serializers.ValidationError("All element must be integer or float numbers")

        for i in range(len(reach_array)):

            # All elements must be float or integers
            try:
                check_number = float(reach_array[i])
            except ValueError:
                raise serializers.ValidationError("All element must be integer or float numbers")

        for i in range(len(reach_array)-1):
            check_number = float(reach_array[i])
            next_number = float(reach_array[i+1])

            # Every element must be bigger or equal 0 and less or equal 100
            if 0 > check_number or check_number > 100:
                raise serializers.ValidationError("All elements of reach field must be positive numbers and less or "
                                                  "equal 100")

            # Next element must be less than previous
            if check_number <= next_number:
                raise serializers.ValidationError("One of elements from 'reach' is bigger than previous")

        # Last element must be bigger or equal 0 and less or equal 100
        if 0 > last_elem or last_elem > 100:
                raise serializers.ValidationError("All elements of reach field must be positive number and less or "
                                                  "equal 100")

        # Quantity element equals ten everytime
        if len(reach_array) != 10:
            raise serializers.ValidationError("Reach need to contain ten elements")

        return data