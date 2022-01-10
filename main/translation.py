  from modeltranslation.translator import translator, TranslationOptions

from .models import Ad

class AdTranslationOption(TranslationOptions):
    fields = ('title', 'location', 'price', 'description')

translator.register(Ad, AdTranslationOption)