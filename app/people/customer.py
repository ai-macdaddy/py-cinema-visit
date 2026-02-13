class Customer:


    def __init__(self, name: int, food: int) -> None:
        self.name = name
        self.food = food

    def watch_movie(self, movie) -> None:
        print(f'{self.name} is watching "{movie}".')
