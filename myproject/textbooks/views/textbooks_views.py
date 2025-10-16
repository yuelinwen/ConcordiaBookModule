from django.views.generic import ListView
from django.shortcuts import redirect
from textbooks.models.book import Book

class TextbookListView(ListView):
    template_name = 'base.html'
    context_object_name = 'all_textbooks'

    def dispatch(self, request, *args, **kwargs):
        if not request.session.get('student_id'):
            return redirect('/auth/login/')
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        q = self.request.GET.get('q', '').strip()
        if q:
            if ' ' not in q and len(q) <= 20:
                return Book.objects.filter(course_code__iexact=q)
            return Book.objects.filter(title__icontains=q)
        course_code = self.kwargs.get('course_code')
        if course_code:
            return Book.objects.filter(course_code__iexact=course_code)
        return Book.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.session.get('username')
        context['selected_course'] = self.kwargs.get('course_code')
        return context
    