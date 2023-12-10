class Colorizer:
    colors = {
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'purple': '\033[95m',
        'default': '\033[0m'
    }

    def __init__(self, color):
        self.color = color

    def __enter__(self):

        return print(self.colors.get(self.color, self.colors['default']), end='')

    def __exit__(self, exc_type, exc_value, traceback):
        print(self.colors['default'], end='')


with Colorizer('red'):
    print('printed in red')
print('printed in default color')

print('\033[93m', end='')
print('aaa')
print('bbb')
print('\033[0m', end='')
print('ccc')

