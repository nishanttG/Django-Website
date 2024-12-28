from django.contrib import admin

from blog.models import Home,Contact,Category,Post,Comment

# Register your models here.
admin.site.register(Home)
admin.site.register(Contact)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
