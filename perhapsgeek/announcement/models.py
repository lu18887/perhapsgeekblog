# coding=utf-8
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.utils import timezone

# Create your models here.

class Announcement(models.Model):
	ENABLE_CHOICES=((0,'停用'),
			(1,'启用'))
	add_date = models.DateTimeField('date added')
	content = models.TextField(_('content'), blank=True)
	enable_flag = models.BooleanField(default=False)
	add_date=timezone.now()
