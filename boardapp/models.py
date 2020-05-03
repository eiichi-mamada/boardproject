from django.db import models

class BoardModel(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  author = models.CharField(max_length=50)
  image = models.ImageField(upload_to='')
  good = models.IntegerField(null=True, blank=True, default=0)
  read = models.IntegerField(null=True, blank=True, default=0)
  readtext = models.CharField(max_length=100,null=True, blank=True, default='a')

  # class Meta:
  #       verbose_name = _("BoardModel")
  #       verbose_name_plural = _("BoardModels")

  #   def __str__(self):
  #       return self.name

  #   def get_absolute_url(self):
  #       return reverse("BoardModel_detail", kwargs={"pk": self.pk})
