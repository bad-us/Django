from django.contrib import admin
from users.models import User

# Register your models here.
# admin.site.register(User)
from baskets.admin import BasketAdmin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = (BasketAdmin,)
