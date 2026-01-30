from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .forms import AIScoperForm
from .openai_client import generate_scope

def home(request):
	return render(request, "home.html")

def services(request):
	return render(request, "services.html")

def portfolio(request):
	# Add real projects here over time.
	projects = [
		{
			"title": "AI Project Scoper (this site)",
			"desc": "Turns a rough idea into clarifying questions + a build plan. Great lead magnet for Fiverr.",
			"stack": "Django, OpenAI API, Bootstrap, Postgres",
		},
		{
			"title": "Ops Automation Dashboard (sample)",
			"desc": "Internal admin panel pattern: KPIs, CSV ingestion, exports, and role-based access.",
			"stack": "Django Admin, Postgres, Charts",
		},
		{
			"title": "Customer Support Copilot (sample)",
			"desc": "A structured Q&A assistant over a company knowledge base (pattern).",
			"stack": "Django, OpenAI, Vector DB (optional)",
		},
	]
	return render(request, "portfolio.html", {"projects": projects})

@require_http_methods(["GET", "POST"])
def ai_assistant(request):
	result = None
	form = AIScoperForm(request.POST or None)

	if request.method == "POST" and form.is_valid():
		idea = form.cleaned_data["idea"]
		result = generate_scope(idea)

	return render(request, "ai_assistant.html", {"form": form, "result": result})

def contact(request):
	return render(request, "contact.html")
