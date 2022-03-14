from django import forms

from .models import Womt 

class WomtForm(forms.ModelForm):
    work_order_name = forms.SlugField(
        widget=forms.TextInput(attrs={"placeholder": "WO-########"})
        )

    class Meta:
        model = Womt 
        fields = [
            'work_order_name',
            'status',
            'assigned_to'
        ]
    
    def clean_work_order_name(self, *args, **kwargs):
        work_order_name = self.cleaned_data.get("work_order_name")
        if work_order_name[:3].lower() != "wo-":
            raise forms.ValidationError("This is not a valid work order name")
        return work_order_name
    
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(WomtForm, self).__init__(*args, **kwargs)
    
    def save(self, *args, **kwargs):
        cur_womt = super(WomtForm, self).save(commit=False)
        cur_womt.created_by = str(self.user)
        cur_womt.save()
        return cur_womt
