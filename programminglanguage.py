class ProgrammingLanguage:
    def __init__(self, language = '', typing = '', reflection = '', year = ''):
        self.language = language
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
       return self.typing == "Dynamic"


    def __str__(self):
        return "{}, {} typing, Reflection={}, First appeared in {}". \
            format(self.language, self.typing, self.reflection, self.year)