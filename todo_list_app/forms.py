from datetime import datetime

from django import forms
from django.core.exceptions import ValidationError

from todo_list_app.models import Tag, Task


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Task
        fields = [
            "content",
            "deadline",
            "is_completed",
            "tags",
        ]
        widgets = {
            "deadline": forms.DateInput(attrs={"type": "date"}),
        }

    def clean_deadline(self):
        deadline = self.cleaned_data["deadline"]
        today = datetime.now().date()

        if deadline < today:
            raise ValidationError(
                "The deadline must be a date in the future."
            )

        return deadline
