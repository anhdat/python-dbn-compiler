head = ['import matplotlib.pyplot as plt']

tail = [
'plt.axis("scaled")',
'plt.show()'
]


def matplot_generator(ast):
    def node_to_code(node):
        return 'plt.gca().add_{type}(plt.{name}({attr_string}))'.format(
            type=node['type'],
            name=node['shape'],
            attr_string=', '.join(['{}={}'.format(k, v) for (k, v) in node['attr'].items()])
        )

    node_codes = [node_to_code(node) for node in ast['body']]
    code = '\n'.join(head + node_codes + tail)
    return code
