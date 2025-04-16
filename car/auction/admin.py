from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import *

class BidInline(admin.TabularInline):
    model = Bid
    extra = 1

class AuctionInline(admin.TabularInline):
    model = Auction
    extra = 1

class CarImageInline(admin.TabularInline):  # же admin.StackedInline
    model = CarImage
    extra = 3
    max_num = 10


@admin.register(Car)
class CarAdmin(TranslationAdmin):
    inlines = [CarImageInline, AuctionInline]

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Auction)
class AuctionAdmin(admin.ModelAdmin):
    inlines = [BidInline]


@admin.register(Brand)
class BrandAdmin(TranslationAdmin):
    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Feedback)
class FeedbackAdmin(TranslationAdmin):
    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.site.register(CarModel)
admin.site.register(UserProfile)
admin.site.register(Bid)
