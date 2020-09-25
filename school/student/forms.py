from django import forms
from student.models import Score


class ScoreForm(forms.ModelForm):
    class Meta():
        model = Score
        fields = ['name', 'physics', 'chemistry', 'mathematics', 'english', 'computer']
