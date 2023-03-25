import json

from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def fetch_css():
    """
    template tag to get main css file's source
    """
    try:
        with open(f"{settings.BASE_DIR}/dist/manifest.json", "r") as f:
            manifest = json.load(f)
    except:
        raise Exception(
            f"Vite manifest file not found or invalid. Maybe your {settings.BASE_DIR}/dist/manifest.json file is empty?"
        )
    return f"{manifest['main.jsx']['css'][0]}"
