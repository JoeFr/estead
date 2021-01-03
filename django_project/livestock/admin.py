from django.contrib import admin

from .models import AnimalType, AnimalStatus, MeatType, Animal, AnimalHarvest

admin.site.site_header = "Growtopia"


admin.site.register(AnimalType)
admin.site.register(AnimalStatus)


@admin.register(MeatType)
class MeatTypeAdmin(admin.ModelAdmin):
    list_display = ("title", "type")
    list_filter = ("type",)
    search_fields = ("title", )


@admin.register(AnimalHarvest)
class AnimalHarvestAdmin(admin.ModelAdmin):
    list_display = ("date", "animal", "type", "weight", "count", "packages")
    list_filter = ("animal", "type", "date")


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ("title", "identification", "type")
    list_filter = ("type",)
    search_fields = ("title", )
