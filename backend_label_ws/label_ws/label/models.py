from django.db import models


class LabelTypes(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        ordering = ['name']

'''
class Label(models.Model):
    label_type = models.ForeignKey(
        LabelTypes,
        related_name='',
        on_delete=models.PROTECT
    )

    name = models.CharField(max_length=150)
    label_assignment = models.BooleanField(default=True)
    label_exclusivity = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Labels'


    def __str__(self):
        return self.name
'''

class BaseLabel(models.Model):
    name = models.CharField(max_length=150)
    label_assignment = models.BooleanField(default=True)
    label_exclusivity = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Base attributes'

class SimpleLabel(BaseLabel):

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Simple attributes'

    def __str__(self):
        return self.name

class AttributeLabel(BaseLabel):
    attribute_name = models.CharField(max_length=150,
                                      verbose_name= 'attributes name')

    class Meta:
        ordering = ['attribute_name']
        verbose_name_plural = 'attributes'
    
    def __str__(self):
        return self.name
    
class MultiLabel(BaseLabel):

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'multilabels'




class Level(models.Model):
    level_name = models.CharField(max_length=150)
    multillabel = models.ForeignKey(
        MultiLabel,
        on_delete=models.CASCADE,
        related_name='levels'
    )

    class Meta:
        ordering = ['level_name']
        verbose_name_plural = 'levels'
    
    def __str__(self):
        return self.level_name




class Image(models.Model):
    name = models.CharField(max_length=150)
    data_type = models.CharField(max_length=150)
    annotation_type = models.CharField(max_length=150)
    labels = models.ManyToManyField(
        'BaseLabel',
        related_name='labels',
        blank=True
    )

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Images'


