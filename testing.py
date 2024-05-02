from bokeh.plotting import figure
import panel as pn

pn.extension()

p1 = figure(name='Scatter')
p1.scatter([0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 2, 1, 0])

p2 = figure(width=300, height=300, name='Line')
p2.line([0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 2, 1, 0])

p3 = figure(width=300, height=300, name='Scatter')
p3.scatter([0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 2, 1, 0])

p4 = figure(width=300, height=300, name='Line')
p4.line([0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 2, 1, 0])

p5 = figure(width=300, height=300, name='Scatter')
p5.scatter([0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 2, 1, 0])

p6 = figure(width=300, height=300, name='Line')
p6.line([0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 2, 1, 0])

tabs = pn.Tabs(
    ('Scatter', p1),
    ('Hello', p2),
    ('How', p3),
    ('are', p4),
    ('We', p5),
    ('Today?', p6),
    dynamic=True)

tabs.servable()
