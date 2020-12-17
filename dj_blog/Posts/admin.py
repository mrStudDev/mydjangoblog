from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ["__str__", "data",]
    list_filter = ["data"]
    search_fields = ["titulo", "conteudo"]
    prepopulated_fields = {"slug": ("titulo",)}

    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)