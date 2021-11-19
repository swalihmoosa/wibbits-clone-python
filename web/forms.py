from django.db.models import fields
from django.forms import ModelForm, models
from web.models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"