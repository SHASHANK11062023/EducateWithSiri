from django.contrib import admin
from   App1.models import EducationalVideo
# Register your models here.
class EducationalVideoAdmin(admin.ModelAdmin):
    list_display=["title","description","video_url"]

admin.site.register(EducationalVideo,EducationalVideoAdmin)
