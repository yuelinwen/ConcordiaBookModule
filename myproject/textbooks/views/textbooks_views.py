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
        course_code_q = self.request.GET.get('courseCode', '').strip()
        availability = self.request.GET.get('availability', '').lower() == 'true'

        queryset = Book.objects.all()
        
        # read course code from url if provided
        path_course_code = self.kwargs.get('course_code')
        if path_course_code:
            queryset = queryset.filter(course_code__iexact=path_course_code)
            
        # if query parameter courseCode is provided, filter again
        if course_code_q:
            queryset = queryset.filter(course_code__iexact=course_code_q)
        if availability:
            queryset = queryset.filter(availability_status=True)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.session.get('username')
        context['selected_course'] = self.kwargs.get('course_code')
        return context
    