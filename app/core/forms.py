from django import forms
from core.models import Book, Branch


class BookForm(forms.ModelForm):
    # Extra fields not on the Book model directly, but used to create the Inventory record
    branch = forms.ModelChoiceField(
        queryset=Branch.objects.all(),
        required=False,
        empty_label="-- Select Branch (Optional) --"
    )
    quantity = forms.IntegerField(
        min_value=1,
        initial=1,
        required=False,
        label="Quantity at Branch"
    )

    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'thumbnail_url', 'price']
