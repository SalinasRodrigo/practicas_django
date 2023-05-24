from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name="books", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


if __name__ == "__main__":
    my_book = Author.objects.create(name="Arthur Conan Doyle")
    Author.objects.all()
    my_book = Book.objects.create(title="Sherlock Holmes", author=Author.objects.get(id=3))
    Book.objects.all()