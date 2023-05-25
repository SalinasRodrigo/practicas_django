from django.db import models

class Book(models.Model):
	title = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
class Publisher(models.Model):
	name = models.CharField(max_length=255)
	books = models.ManyToManyField(Book, related_name="publishers")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


if __name__ == "__main__":
    my_book = Publisher.objects.create(name="Publisher 1")
    Publisher.objects.all()
    my_book = Book.objects.create(title="Sherlock Holmes")
    Book.objects.all()