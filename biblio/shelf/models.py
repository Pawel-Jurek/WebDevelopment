from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        ordering = ('last_name', 'first_name')
        verbose_name_plural = 'Authors'


class Publisher(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name
    

class BookCategory(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    categories = models.ManyToManyField(BookCategory)

    def __str__(self):
        return self.title
    

class BookEdition(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=17, blank=True)
    date = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.book.title},  {self.publisher.name}'


COVER_TYPES = (
    ('soft', 'Soft'),
    ('hard', 'Hard'),        #(wartość w bazie, wartość wyświetlana)
)


class BookItem(models.Model):
    edition = models.ForeignKey(BookEdition, on_delete=models.CASCADE)
    catalogue_number = models.CharField(max_length=30)
    cover_type = models.CharField(max_length=4, choices=COVER_TYPES)

    def __str__(self):
        return f'{self.edition}, {self.get_cover_type_display()}'