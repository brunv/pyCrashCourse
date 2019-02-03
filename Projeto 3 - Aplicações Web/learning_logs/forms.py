from django import forms
from .models import Topic

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


#       Inicialmente importamos o módulos 'forms' e os modelos com os quais
#       trabalharemos.
#
#       A versão mais simples de 'ModelForm' é constituída de uma classe 'Meta'
#       aninhada que diz a Django em qual modelo o formulário deve se basear e
#       quais campos devem ser incluídos nesse formulário.
#
#       Em 'Meta', criamos um formulário a partir do modelo 'Topic' e incluímos
#       apenas o campo 'text'. Esse código diz a Django para não gerar um label
#       para o campo 'text'.