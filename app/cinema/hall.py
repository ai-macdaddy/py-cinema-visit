class CinemaHall:


    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
            self,
            movie_name: str,
            customers: list[customers: Customer],
            cleaning_staff: Cleaner
    ) -> None:
        '''This method prints about movie start, calls
   customers method `watch_movie`, prints about movie end,
   calls cleaner method `clean_hall`. So, we are expecting
   that everything listed above will be performed in `movie_session` function.'''
