from django.contrib import admin

from .models import Author, Genre, Book, BookInstance, Language

"""
Superuser:

Username: admin
Email address: admin@jacagen.com
Password: admin 

Regular library user:
Username: albertu
Password: django1+

Regular library user:
Username: jamie
Password: django2+

Librarian:
Username: jamie_librarian
Password: django1+

Librarian:
Username: superman
Password: django1+
"""

class BooksInLine(admin.StackedInline):
    model = Book
    extra = 0
    

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInLine]

class BookInstancesInLine(admin.TabularInline):
    model = BookInstance
    extra = 0

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstancesInLine]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )

#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
#admin.site.register(BookInstance)
admin.site.register(Language)
