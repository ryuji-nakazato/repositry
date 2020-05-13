from django.forms import ModelForm
from cms.models import Anken, Sintyoku, Todo, Task
from django import forms

class AnkenForm(ModelForm):
    """案件のフォーム"""
    class Meta:
        model = Anken
        fields = ('enduser', 'hansha', 'joukyo', 'product', 'sbkk', 'hansui', 'sisuisin', 'hitouch', 'donyusien', 'jutyu', 'donyu', 'kakudo', 'kyougou', 'mitumorigaku', 'arari', )
        """日付の入力をプルダウンで。"""
        widgets = {
            'jutyu': forms.SelectDateWidget(years=[x for x in range(2019, 2030)]),
            'donyu': forms.SelectDateWidget(years=[x for x in range(2019, 2030)])
        }


class SintyokuForm(ModelForm):
    """進捗のフォーム"""
    class Meta:
        model = Sintyoku
        fields = ('kinyubi', 'shosai', )

class TodoForm(forms.ModelForm):
    """Todoのフォーム"""
    class Meta:
        model = Todo
        fields = ('kanryoflg', 'task', 'kigen',)



class TaskForm(forms.ModelForm):
    """Taskのフォーム"""
    class Meta:
        model = Task
        fields = ('kanryoflg', 'task', 'kigen', 'tantou',)




