from django.contrib import admin
from .models import Categoria, Post, Creador

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title','author','thumbnail','video_url','description','category','tags',
                    'external_links','upload_date','created_at')
    

admin.site.register(Categoria)
admin.site.register(Creador)