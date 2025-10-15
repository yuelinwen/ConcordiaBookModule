from django.views.generic import ListView
from django.shortcuts import redirect

class TextbookListView(ListView):
    template_name = 'textbooks/list.html'
    context_object_name = 'all_textbooks'

    def dispatch(self, request, *args, **kwargs):
        if not request.session.get('student_id'):
            return redirect('/auth/login/')
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return ['textbook1', 'textbook2', 'textbook3']
