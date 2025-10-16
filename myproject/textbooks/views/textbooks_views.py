from django.views.generic import ListView
from django.shortcuts import redirect
from textbooks.models.book import Book
from django.contrib import messages
import datetime


class TextbookListView(ListView):
    template_name = "base.html"
    context_object_name = "all_textbooks"

    def dispatch(self, request, *args, **kwargs):
        if not request.session.get("student_id"):
            return redirect("/auth/login/")
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        course_code_q = self.request.GET.get("courseCode", "").strip()
        availability = self.request.GET.get("availability", "").lower() == "true"

        queryset = Book.objects.all()

        # read course code from url if provided
        path_course_code = self.kwargs.get("course_code")
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
        context["username"] = self.request.session.get("username")
        context["selected_course"] = self.kwargs.get("course_code")
        current_year = datetime.datetime.now().year
        context["year_range"] = range(current_year, current_year - 100, -1)
        return context


# function-based view POST request to add a book
def add_book(request):
    if not request.session.get("student_id"):
        return redirect("/auth/login/")

    if request.method == "POST":
        title = request.POST.get("title")
        year = request.POST.get("year") or 0
        edition = request.POST.get("edition")
        author = request.POST.get("author")
        course_code = request.POST.get("course_code")
        condition = request.POST.get("condition")

        Book.objects.create(
            title=title,
            year=int(year),
            edition=edition,
            author=author,
            course_code=course_code,
            condition=condition,
            availability_status=True,
        )
        messages.success(request, "Book added successfully!")
        return redirect("/")
    return redirect("/")
