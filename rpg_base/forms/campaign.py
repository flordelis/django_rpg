from django.forms import ModelForm
from crispy_forms.helper import FormHelper

class CampaignForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CampaignForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

