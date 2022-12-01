from django.shortcuts import render
from django.views import generic
# Create your views here.
from .models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    paginate_by = 2
    context_object_name = 'book_list'   # your own name for the list as a template variable
    # queryset = Book.objects.all()[:5] # Get 5 books 
    template_name = 'book_list.html'  # Specify your own template name/location
    
    def get_queryset(self):
        return Book.objects.all()[:5]
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book_details.html'

class AuthorListView(generic.ListView):
    model = Author
    template_name = 'author_list.html'

class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'author_details.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # or whatever
        context['books'] = Book.objects.all()  # or whatever
        return context


