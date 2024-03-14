from django import forms

from .models import Details

select_gender = (
    ("male", "Male"),
    ("female", "Female"),
    ("other", "Other"),
)

select_purpose = (
    ("Order", "order"),
    ("Return ", "return ")
)

select_materials_provide = (
    ("Note Book", "note book"),
    ("Pen", "pen"),
    ("Exam Peppers", "exam peppers")
)


class DateInput(forms.DateInput):
    input_type = 'date'


class DetailsForms(forms.ModelForm):
    class Meta:
        model = Details
        fields = '__all__'
        widgets = {
            "gender": forms.RadioSelect(choices=select_gender),
            "date_of_brith": DateInput,
            "materials_provide": forms.RadioSelect(choices=select_materials_provide),
            "purpose": forms.Select(choices=select_purpose),
            "department": forms.Select(),
            "courses": forms.Select(),
        }
