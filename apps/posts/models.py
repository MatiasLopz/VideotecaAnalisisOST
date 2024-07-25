from django.db import models
from django.utils import timezone

# Create your models here.



# Categoría
class Categoria(models.Model):
    nombre = models.CharField(max_length=30, null=False)
    
    def __str__(self) -> str:
        return self.nombre

class Creador(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    
    def __str__(self) -> str:
        return self.nombre    
    

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Creador, on_delete=models.SET_NULL, null=True, default=None)
    thumbnail = models.ImageField(null=True, blank=True, upload_to='media/', default='./static/post_default.png')
    video_url = models.URLField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, default=None)
    tags = models.CharField(max_length=200)
    external_links = models.TextField(null=True, default=None)
    upload_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-created_at',)
    
    def __str__(self):
        return self.title
    
    def delete(self,using=None, keep_parents=False):
        self.thumbnail.delete(self.thumbnail.name)
        super().delete()