from django.shortcuts import render, redirect
from core.models import Branch, Inventory
from core.forms import BookForm


def book_list(request):
    selected_branch_id = request.GET.get('branch')
    branches = Branch.objects.all()

    if selected_branch_id:
        # Fetch inventory items filtered by selected branch
        inventories = Inventory.objects.filter(
            branch_id=selected_branch_id
        ).select_related('book', 'branch')
    else:
        # Fetch all inventory items across all branches
        inventories = Inventory.objects.select_related('book', 'branch').all()

    context = {
        'inventories': inventories,
        'branches': branches,
        'selected_branch_id': int(selected_branch_id) if selected_branch_id else None,
    }
    return render(request, 'books/book_list.html', context)


def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            # 1. Save the new Book instance
            book = form.save()

            # 2. Check if a branch and quantity were selected
            branch = form.cleaned_data.get('branch')
            quantity = form.cleaned_data.get('quantity') or 1

            if branch:
                Inventory.objects.create(
                    book=book,
                    branch=branch,
                    quantity=quantity
                )

            return redirect('book-list')
    else:
        form = BookForm()

    return render(request, 'books/book_form.html', {'form': form})
