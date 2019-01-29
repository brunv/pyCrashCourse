from django.contrib import admin
from learning_logs.models import Topic, Entry

# Register your models here.
admin.site.register(Topic)
admin.site.register(Entry)

#       Esse código importa o modelo que queremos registrar e então usa
#       'admin.site.register()' para dizer a Django que administre nosso modelo por
#       meio do site de administração.