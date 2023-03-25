import json

from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def fetch_javascript():
    """
    templatetag to get main javascript source
    """
    try:
        with open(f"{settings.BASE_DIR}/dist/manifest.json", "r") as f:
            manifest = json.load(f)
    except:
        raise Exception(
            f"Vite manifest file not found or invalid. Maybe your {settings.BASE_DIR}/dist/manifest.json file is empty?"
        )
    return f"{manifest['main.jsx']['file']}"
