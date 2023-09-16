from rest_framework import viewsets
from label import models , serializers

class LabelTypesApiView(viewsets.ModelViewSet):
    queryset = models.LabelTypes.objects.all()
    ordering_fields = ['name']
    serializer_class = serializers.LabelTypesSerializer
    search_fields = ['name']

class SimpleLabelApiView(viewsets.ModelViewSet):
    queryset = models.SimpleLabel.objects.all()
    ordering_fields = ['name']
    serializer_class = serializers.SimpleLabelSerializer
    search_fields = ['name']

class AttributeLabelApiView(viewsets.ModelViewSet):
    queryset = models.AttributeLabel.objects.all()
    ordering_fields = ['name']
    serializer_class = serializers.AttributeLabelSerializer
    search_fields = ['name']

class MultiLabelApiView(viewsets.ModelViewSet):
    queryset = models.MultiLabel.objects.all()
    ordering_fields = ['name']
    serializer_class = serializers.MultiLabelSerializer
    search_fields = ['name']

class ImageApiView(viewsets.ModelViewSet):
    queryset = models.Image.objects.all()
    ordering_fields = ['name']
    serializer_class = serializers.ImageSerrializer
    search_fields = ['name']


