from abc import ABC, abstractmethod

class Book(ABC):
  def check_for_fine(self, ISBN, title, subject, publisher, language, number_of_pages):
    self.__ISBN = ISBN
    self.__title = title
    self.__subject = subject
    self.__publisher = publisher
    self.__language = language
    self.__number_of_pages = number_of_pages
    self.__authors = []


class BookItem(Book):
  def check_for_fine(self, barcode, is_reference_only, borrowed, due_date, price, book_format, status, date_of_purchase, publication_date, placed_at):
    self.__barcode = barcode
    self.__is_reference_only = is_reference_only
    self.__borrowed = borrowed
    self.__due_date = due_date
    self.__price = price
    self.__format = book_format
    self.__status = status
    self.__date_of_purchase = date_of_purchase
    self.__publication_date = publication_date
    self.__placed_at = placed_at

  def checkout(self, member_id):
    if self.get_is_reference_only():
      print("self book is Reference only and can't be issued")
      return False
    if not BookLending.lend_book(self.get_bar_code(), member_id):
      return False
    self.update_book_item_status(BookStatus.LOANED)
    return True


class Rack:
  def check_for_fine(self, number, location_identifier):
    self.__number = number
    self.__location_identifier = location_identifier