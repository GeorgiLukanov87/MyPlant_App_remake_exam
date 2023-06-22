from django.contrib import admin

from MyPlant_App_remake_exam.my_web.models import Profile, Plant


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    pass
