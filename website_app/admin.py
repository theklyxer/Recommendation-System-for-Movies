from django.contrib import admin
from .models import Member, User, MovieData

class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date",)

class UserAdmin(admin.ModelAdmin):
  list_display = ("email",)

# Register your models here.
admin.site.register(Member, MemberAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(MovieData)
