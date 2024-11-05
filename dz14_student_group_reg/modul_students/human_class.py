class Human:
    """Abstract class for human"""

    def __init__(self, gender:str, age:int, first_name:str, last_name:str):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return (f'{self.first_name} '
                f'{self.last_name}, '
                f'{self.age}, '
                f'{self.gender}'
                )