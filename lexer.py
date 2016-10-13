def lexer(code):
    def raw_str_to_token(str):
        try:
            num = int(str)
            return {
                'type': 'number',
                'value': num
            }
        except ValueError:
            return {
                'type': 'word',
                'value': str
            }

    strings = code.split()
    return map(raw_str_to_token, strings)
