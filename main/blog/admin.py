# -*- encoding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.utils.translation import gettext_lazy as _
from django.contrib import admin

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("name", "published", "is_active", "user",)
    list_filter = ("published", "is_active",)
    search_fields = ("name", "user__username", "user__email",)
