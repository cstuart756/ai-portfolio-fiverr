from django import forms

class AIScoperForm(forms.Form):
    idea = forms.CharField(
        label="Describe your idea",
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "rows": 6,
            "placeholder": "Example: I need a dashboard that summarizes weekly sales from CSV, emails reports, and includes role-based access...",
        })
    )
