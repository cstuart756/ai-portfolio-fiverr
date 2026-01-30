from django import forms

class QuoteRequestForm(forms.Form):
    name = forms.CharField(label="Your Name", max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(label="Your Email", widget=forms.EmailInput(attrs={"class": "form-control"}))
    details = forms.CharField(label="Project Details", widget=forms.Textarea(attrs={"class": "form-control", "rows": 6, "placeholder": "Describe your project, data sources, users, deadlines, etc."}))
