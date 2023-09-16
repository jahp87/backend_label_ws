from rest_framework import serializers
from label import models



class LabelTypesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.LabelTypes
        fields = '__all__'
    
class SimpleLabelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SimpleLabel
        fields = '__all__'

class AttributeLabelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.AttributeLabel
        fields = '__all__'

class MultiLabelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.MultiLabel
        fields = '__all__'

class ImageSerrializer(serializers.ModelSerializer):

    class Meta:
        model = models.Image
        fields = '__all__'

