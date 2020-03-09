from django.db import models
from django.utils import safestring

# Create your models here.

class Activity(models.Model):
    activity_id = models.AutoField(primary_key=True)
    activity_user = models.CharField(max_length=50, default='', verbose_name='User')
    activity_vid = models.CharField(max_length=100, default='', verbose_name='Video Title')
    activity_addr = models.CharField(max_length=50, default='', verbose_name='User IP')
    activity_loc = models.CharField(max_length=100, default='', verbose_name='User Location')
    activity_reg = models.CharField(max_length=100, default='', verbose_name='User Region')
    activity_isp = models.CharField(max_length=100, default='', verbose_name='User ISP')
    activity_url = models.URLField(default='', verbose_name='YouTube Address')
    activity_path = models.CharField(max_length=100, default='', verbose_name='File Path', help_text='The file might not exist.')
    activity_pubdate = models.DateTimeField(auto_now=True)

    def __str__(self):
        space_sym = "&nbsp"*10 # hardcode magic-number of indent spaces
        return safestring.mark_safe('{}{}{}{}{}{}{}'.format(self.activity_addr, space_sym, self.activity_url[:15]+'..', space_sym, self.activity_loc, space_sym, self.activity_pubdate.time()))

    class Meta:
        verbose_name = "Activity"
        verbose_name_plural = "Activities"
