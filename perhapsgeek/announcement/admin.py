from django.contrib import admin
from announcement.models import Announcement

# Register your models here.




class  AnnouncementAdmin(admin.ModelAdmin):
	date_hierarchy ='modify_date'	
	fields = ('title','content','enable_flag')
	exclude = ('add_date','modify_date')
	list_display = ('title','modify_date','add_date','enable_flag')
	list_filter = ('add_date','modify_date')



























admin.site.register(Announcement,AnnouncementAdmin)
