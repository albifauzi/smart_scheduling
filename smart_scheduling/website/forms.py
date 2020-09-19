from django import forms

from smart_scheduling.apps.instructors.models import Instructor


class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ['name', 'hour', 'days']