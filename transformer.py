from collections import deque


def _get_paper_node(node):
    paper_color_value = node['arguments'][0]['value']
    paper_color = paper_color_value or 100
    return {
        'type': 'patch',
        'shape': 'Rectangle',
        'attr': {
            'width': 100,
            'height': 100,
            'xy': (0, 0),
            'fc': '"{}"'.format(1 - 100 / paper_color)
        },
    }


def _get_pen_color(node):
    color_value = node['arguments'][0]['value']
    return '"{}"'.format(1 - color_value * 0.1)


def _get_line_node(node, color):
    args = node['arguments']
    return {
        'type': 'line',
        'shape': 'Line2D',
        'attr': {
            'xdata': (args[0]['value'], args[2]['value']),
            'ydata': (args[1]['value'], args[3]['value']),
            'color': '{}'.format(color)
        },
    }


def transformer(ast):
    matplot_ast = {
        'shape': 'Rectangle',
        'attr': {
            'width': 100,
            'height': 100,
        },
        'body': []
    }
    nodes = deque(ast['body'])
    pen_color = 1.0

    while True:
        try:
            current_node = nodes.popleft()
        except IndexError:
            break

        if current_node['name'] == 'Paper':
            matplot_ast['body'].append(_get_paper_node(current_node))
            continue
        elif current_node['name'] == 'Pen':
            pen_color = _get_pen_color(current_node)
            continue
        elif current_node['name'] == 'Line':
            matplot_ast['body'].append(_get_line_node(current_node, pen_color))
            continue

    return matplot_ast
