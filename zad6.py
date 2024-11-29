class BigLettersDecorator:
    def __init__(self, function):
        self.function = function

    def __call__(self):
        result = self.function()
        if isinstance(result, str):
            return result.upper()
        return result


@BigLettersDecorator
def do_string():
    return "Robert Zubek"


print(do_string())
