from django import forms
from .models import Topic, Entry

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


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}


#       Um 'widget' é um elemento do formulário HTML, por exemplo, uma caixa de
#       texto de uma única linha, uma área de texto com várias linhas ou uma lista
#       suspensa. Ao incluir o atributo 'widgets', podemos sobrescrever opções
#       default de widgets de Django.