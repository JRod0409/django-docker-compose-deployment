from django import forms
from core.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'  # Form will include all fields defined on your Book model