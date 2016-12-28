from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
  

class Photo(models.Model):
    title = models.CharField(max_length = 200)
    width = models.IntegerField(default = 0)
    height = models.IntegerField(default = 0)
    image = models.ImageField(null = False, blank = False, width_field = "width", height_field = "height")
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
    
    def get_absolute_url(self):
        return reverse('detail', kwargs = {'pk': self.pk})
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ["-timestamp"]