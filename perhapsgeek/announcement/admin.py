from django.contrib import admin
from announcement.models import Announcement

# Register your models here.




class  AnnouncementAdmin(admin.ModelAdmin):
	pass	



























admin.site.register(Announcement,AnnouncementAdmin)
