from django import forms
 
class UserForm(forms.Form):
    name = forms.CharField(min_length=3,required=True)
    age = forms.IntegerField(min_value=1, max_value=100,required=False)
    required_css_class = "field"
    error_css_class = "error"