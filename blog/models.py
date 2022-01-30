from django.db import models
from django.conf import settings
# Create your models here.

class Post(models.Model):
  author_id = models.IntegerField(null=True,
                                       blank=True,
                                       verbose_name='author id Value',
                                       help_text='author id Value')
  created_at = models.DateTimeField(db_index=False, )
  modified_at = models.DateTimeField(db_index=False, )
  published_at = models.DateTimeField(db_index=False, )
  title = models.CharField(max_length=128,
                                 db_index=False,
                                 verbose_name='Title',
                                 help_text='')
  slug = models.SlugField(unique=True)
  summary = models.CharField(max_length=500,
                                 db_index=False,
                                 verbose_name='summary',
                                 help_text='')
  content = models.CharField(max_length=500,
                                 db_index=False,
                                 verbose_name='content',
                                 help_text='')

  def __str__(self):
        return str("{}:{}".format(self.id, self.title))
