from queue import Queue
from collections import deque


def get_paper_expr(tokens):
    expression = {
        'type': 'CallExpression',
        'name': 'Paper',
        'arguments': []
    }

    # if current_token is Paper, next token should be a Color in number
    try:
        argument = tokens.popleft()
    except IndexError:
        raise Exception('Paper should be followed by a number')

    if argument['type'] == 'number':
        expression['arguments'].append({
            'type': 'NumberLiteral',
            'value': argument['value'],
        })
    else:
        raise Exception('Paper should be followed by a number')

    return (expression, tokens)


def get_pen_expr(tokens):
    expression = {
        'type': 'CallExpression',
        'name': 'Pen',
        'arguments': []
    }

    # if current_token is Paper, next token should be a Color in number
    try:
        argument = tokens.popleft()
    except IndexError:
        raise Exception('Pen should be followed by a number')

    if argument['type'] == 'number':
        expression['arguments'].append({
            'type': 'NumberLiteral',
            'value': argument['value'],
        })
    else:
        raise Exception('Pen should be followed by a number')

    return (expression, tokens)


def get_line_expr(tokens):
    expression = {
        'type': 'CallExpression',
        'name': 'Line',
        'arguments': []
    }

    # if current_token is Paper, next token should be a Color in number
    try:
        args = [tokens.popleft() for __ in range(0, 4)]
    except IndexError:
        raise Exception('Line should be followed by 4 numbers')

    is_all_number_tokens = filter(lambda x: x['type'] == 'number', args)

    if is_all_number_tokens:
        def add_number_args(arg, expression):
            expression['arguments'].append({
                'type': 'NumberLiteral',
                'value': arg['value'],
            })

        for arg in args:
            add_number_args(arg, expression)
    else:
        raise Exception('Line should be followed by 4 numbers')

    return (expression, tokens)


def parser(tokens):
    ast = {
        'type': 'Drawing',
        'body': []
    }
    tokens = deque(tokens)

    while True:
        try:
            current_token = tokens.popleft()
        except IndexError:
            break

        _type = current_token['type']
        _value = current_token['value']

        if _type == 'word':
            if _value == 'Paper':
                expression, tokens = get_paper_expr(tokens)
                ast['body'].append(expression)
                continue
            elif _value == 'Pen':
                expression, tokens = get_pen_expr(tokens)
                ast['body'].append(expression)
                continue
            elif _value == 'Line':
                expression, tokens = get_line_expr(tokens)
                ast['body'].append(expression)
                continue

    return ast
