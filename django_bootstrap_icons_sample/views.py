import re

from django.shortcuts import render
from django.views.generic.base import TemplateView

from django_bootstrap_icons.templatetags.bootstrap_icons import bs_icon, md_icon
from django_bootstrap_icons_sample.forms import IconForm


class HomePageView(TemplateView):
    template_name = "django_bootstrap_icons_sample/index.html"


def icon_view(request):

    if request.method == 'POST':
        form = IconForm(request.POST)
        if form.is_valid():
            icon_type = form.cleaned_data['icon_type']
            name = form.cleaned_data['icon_name']
            size_no = form.cleaned_data['icon_size']
            color = form.cleaned_data['icon_color']
            align = form.cleaned_data['icon_align']
            match = re.match(r"([0-9]+)([a-z]+)", size_no, re.I)
            if match:
                items = match.groups()
                size = items[0]
            else:
                size = size_no
            if icon_type == 'bi':
                tag = bs_icon(name, size=size, color=color, extra_classes=align)
            else:
                tag = md_icon(name, size=size, color=color, extra_classes=align)
            if icon_type == 'bi':
                text = f'bs_icon { name }'
            else:
                text = f'md_icon {name}'
            if size:
                text += f' size="{ size }"'
            if color:
                text += f' color="{ color }"'
            if align:
                text += f' extra_classes="{align}"'
            text = '{% ' + text + ' %}'
    else:
        tag = None
        text = ''
        size = '16'
        form = IconForm()

    return render(request, 'django_bootstrap_icons_sample/icon.html', {
        'form': form,
        'tag': tag,
        'text': text,
        'size': size
    })