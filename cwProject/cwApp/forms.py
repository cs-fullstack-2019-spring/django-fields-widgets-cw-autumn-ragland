from django import forms
from .models import SuperHeroModel

# choices
POWERS = (
    ('Flight', 'Flight'), ('Speed', 'Speed'), ('Invisibility', 'Invisibility'), ('Telekenetic', 'Telekenetic'),
    ('Healing', 'Healing'),
    ('Other', 'Other'),)

EVIL = (('Good', 'Good'), ('kinda good', 'kinda good'), ('neutral', 'neutral'), ('little evil', 'little evil'),
        ('evil', 'evil'))


# model bound form
class SuperHeroForm(forms.ModelForm):
    class Meta:
        model = SuperHeroModel
        fields = '__all__'
        widgets = {
            'rich_or_superpowers': forms.RadioSelect(choices=(('R', 'Rich'), ('S', 'Superpowers'))),
            'powers': forms.SelectMultiple(choices=POWERS),
            'good_or_evil': forms.Select(choices=EVIL),
        }
