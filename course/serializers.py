from rest_framework import serializers
from .models import ShortCourse, Amount

class AmountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amount
        fields = "__all__"

# class ShortCourseSerializer(serializers.ModelSerializer):
#     print('serializer.......................')
#     amount_values = serializers.ListField(write_only=True)
#     amount_texts = serializers.ListField(write_only=True)
#     amounts = AmountSerializer(many=True, read_only=True)

#     class Meta:
#         model = ShortCourse
#         fields = "__all__"
        
    # def create(self, validated_data):
    #     print('inside create serializer.......................')
    #     amount_values = validated_data.pop('amount_values')
    #     amount_texts = validated_data.pop('amount_texts')

    #     short_course = ShortCourse.objects.create(**validated_data)
    #     print(short_course,'short_course..............')  

    #     for value, text in zip(amount_values, amount_texts):
    #         Amount.objects.create(value=value, text=text, short_course=short_course)
          

    #     return short_course    
