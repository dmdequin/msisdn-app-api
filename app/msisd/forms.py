"""
Forms for the MSISD API.
"""
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class GetMSISDNForm(forms.Form):
    """Class for the MSISD form."""
    msisdn = forms.CharField(
        help_text="Enter an MSISD number"
        )

    def clean(self):
        cleaned_data = super(GetMSISDNForm, self).clean()
        msisdn = int(cleaned_data.get('msisdn'))

        if type(msisdn) != str:
            raise ValidationError(_('Value must be an Integer!'))

        if not msisdn:
            raise ValidationError(_('You must enter an MSISDN!'))

        return msisdn
