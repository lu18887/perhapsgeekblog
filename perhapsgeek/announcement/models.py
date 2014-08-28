# coding=utf-8
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.utils import timezone

# Create your models here.

class Announcement(models.Model):
	ENABLE_CHOICES=((0,'停用'),
			(1,'启用'))
	add_date = models.DateTimeField('date added',default=timezone.now())
	modify_date=models.DateTimeField(_('date modified'),blank=True)
	title=models.CharField(max_length=100)
	content = models.TextField(_('content'), blank=True)
	enable_flag = models.BooleanField(default=False)
	def __unicode__(self):
		return self.title

	def save(self,*args,**kwargs):
		self.modify_date=timezone.now()
		super(Announcement, self).save(*args, **kwargs)