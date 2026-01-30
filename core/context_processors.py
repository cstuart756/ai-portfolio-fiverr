from django import template

def site_branding(request):
    return {
        "SITE_NAME": "Stuart Carey",
        "SITE_TAGLINE": "AI Web Application Developer",
    }
