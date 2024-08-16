from abc import ABC ,abstractmethod

class LibraryItem(ABC):
    item_type = 'General'

    def __init__(self,title,available = True):
        self._title = title  # protected so that childs can access it
        self.__available = available # private only class members can access it

    # mot defining the real implementation of lending and returning a item
    @abstractmethod
    def lend_item(self):
        pass

    @abstractmethod
    def return_item(self):
        pass


    def is_available(self): # method to check availability
        return self.__available

    # method to update availability protected
    def _mark_as_available(self):
        self.__available = True


    def _mark_as_unavailable(self):
        self.__available = False
