"""
Forms for the MSISD API.
"""
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class GetMsisdForm(forms.Form):
    """Class for the MSISD form."""
    msisdn = forms.IntegerField(
        help_text="Enter the MSISD number."
        )

    def clean(self):
        cleaned_data = super(GetMsisdForm, self).clean()
        msisdn = cleaned_data.get('msisdn')

        if not msisdn:
            raise ValidationError(_('You must enter an MSISDN!'))

        return msisdn
