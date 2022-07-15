from django.contrib import admin

from claims.models import Claim


@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']
    list_filter = ['type']
