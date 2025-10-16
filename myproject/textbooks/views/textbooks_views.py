from django.views.generic import ListView
from django.shortcuts import redirect

# Import the Book model so get_queryset can return real objects
from textbooks.models.book import Book

class TextbookListView(ListView):
    template_name = 'base.html'
    context_object_name = 'all_textbooks'

    def dispatch(self, request, *args, **kwargs):
        if not request.session.get('student_id'):
            return redirect('/auth/login/')
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Book.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.session.get('username')
        return context