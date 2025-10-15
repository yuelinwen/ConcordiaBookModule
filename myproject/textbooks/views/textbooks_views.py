from django.views.generic import ListView

class TextbookListView(ListView):
    template_name = 'textbooks/list.html'
    context_object_name = 'all_textbooks'

    def get_queryset(self):
        return ['textbook1', 'textbook2', 'textbook3']
        

