from .models import *
from modeltranslation.translator import TranslationOptions, register

@register(Brand)
class BrandTranslationOptions(TranslationOptions):
    fields = ('brand_name',)


@register(Car)
class CarTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(Feedback)
class FeedbackTranslationOptions(TranslationOptions):
    fields = ('comment',)

