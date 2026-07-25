from django.db import models

class Book(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    thumbnail_url = models.URLField(max_length=500)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.title

class Branch(models.Model):
    branch_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.branch_name

class Inventory(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='inventories')
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='inventories')
    quantity = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Inventories"

    def __str__(self):
        return f"{self.book.title} at {self.branch.branch_name} ({self.quantity})"