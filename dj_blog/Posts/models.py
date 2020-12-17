from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Post(models.Model):
    titulo = models.CharField(max_length=120)
    tag = models.CharField(max_length=30)
    resumo = RichTextUploadingField(blank=True)
    conteudo = RichTextUploadingField(blank=True)
    data = models.DateTimeField(auto_now=False, auto_now_add=True)
    slug = models.SlugField()
    
    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse("singular", kwargs={"id": self.id, "slug": self.slug})
