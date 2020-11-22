class City:
  def __init__(self, name, state, zip_code):
    self.__name = name
    self.__state = state
    self.__zip_code = zip_code


class Cinema:
  def __init__(self, name, total_cinema_halls, address, halls):
    self.__name = name
    self.__total_cinema_halls = total_cinema_halls
    self.__location = address

    self.__halls = halls


class CinemaHall:
  def __init__(self, name, total_seats, seats, shows):
    self.__name = name
    self.__total_seats = total_seats

    self.__seats = seats
    self.__shows = shows