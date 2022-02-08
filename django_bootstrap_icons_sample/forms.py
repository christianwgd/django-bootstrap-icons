from django import forms

TYPE_CHOICES = (
    ('bi', 'Bootstrap Icon'),
    ('mdi', 'Material Design Icon'),
)

ALIGN_CHOICES = (
    ('', 'default'),
    ('bi-valign-top', 'top'),
    ('bi-valign-middle', 'middle'),
    ('bi-valign-bottom', 'bottom'),
    ('bi-valign-text-top', 'text-top'),
    ('bi-valign-text-bottom', 'text-bottom'),
)

class IconForm(forms.Form):
    icon_type = forms.ChoiceField(
        label='Type', choices=TYPE_CHOICES
    )
    icon_name = forms.CharField(
        label='Name', max_length=50, required=True,
        help_text='The name of an icon without any "bi" or "md" prefixes'
    )
    icon_size = forms.CharField(
        label='Size', max_length=10, required=False,
        help_text='Size number in pixel'
    )
    icon_color = forms.CharField(
        label='Color', max_length='20', required=False,
        help_text='Color string ("#808080") or name ("grey")'
    )
    icon_align = forms.ChoiceField(
        label='Alignment', choices=ALIGN_CHOICES, required=False
    )
