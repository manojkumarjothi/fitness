
from django.contrib import admin

from .models import Register
from .models import Login
from .models import Author
from .models import Book
from .models import Review

admin.site.register(Register)
admin.site.register(Login)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Review)