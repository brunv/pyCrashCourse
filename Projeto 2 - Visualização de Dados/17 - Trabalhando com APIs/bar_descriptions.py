#
#       Acrescentando dicas de contexto personalizadas em gráficos de barras:
#

import pygal

chart = pygal.Bar(x_label_rotation=45, show_legend=False)
chart.title = 'Python Projects'
chart.x_labels = ['httpie', 'django', 'flask']

plot_dicts = [
    {'value': 16101, 'label': 'Description of httpie.'},
    {'value': 15028, 'label': 'Description of django.'},
    {'value': 14798, 'label': 'Description of flask.'}
]

chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions_test.svg')