from django import newforms as forms
from polling.core.models import Poll


class PollForm(forms.Form):
    question = forms.CharField(max_length=200)

    def clean_question(self):
        question = self.cleaned_data['question']
        count = Poll.objects.filter(question=question).count()
        if count != 0:
            raise forms.ValidationError('The question "%s" is already in use.' % question)
        return question
