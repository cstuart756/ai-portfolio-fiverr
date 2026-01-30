from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .forms_quote import QuoteRequestForm

@require_http_methods(["GET", "POST"])
def request_quote(request):
    submitted = False
    if request.method == "POST":
        form = QuoteRequestForm(request.POST)
        if form.is_valid():
            # Here you would send an email or save to DB
            submitted = True
    else:
        form = QuoteRequestForm()
    return render(request, "request_quote.html", {"form": form, "submitted": submitted})
