import json

from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def render_vite_bundle():
    """
    Template tag to render a vite bundle.
    Supposed to only be used in production.
    For development, see other files.
    """

    try:
        fd = open(f"{settings.BASE_DIR}/dist/manifest.json", "r")
        manifest = json.load(fd)
    except:
        raise Exception(
            f"Vite manifest file not found or invalid. Maybe your {settings.BASE_DIR}/dist/manifest.json file is empty?"
        )

    return mark_safe(
        f"""<script type="module" src="/static/{manifest["main.jsx"]['file']}"></script>
        <link rel="stylesheet" type="text/css" href="/static/{manifest["main.jsx"]['css'][0]}" />"""
    )
