from django.db.models import fields
from django.forms import ModelForm
from django.forms.widgets import EmailInput, TextInput
from web.models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            "email" : EmailInput(attrs={"placeholder" : "Enter Your Email"}),
            "first_name" : TextInput(attrs={"placeholder" : "Enter Your First Name"}),
            "last_name" : TextInput(attrs={"placeholder" : "Enter Your Last Name"}),
            "company" : TextInput(attrs={"placeholder" : "Enter Your Company"}),
            # "company" : EmailInput(attrs={"placeholder" : "Enter Your Company"})
            # "email" : EmailInput(attrs={"placeholder" : "Enter Your Email"})
        }