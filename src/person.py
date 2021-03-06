from abc import ABCMeta, abstractmethod
import uuid


class Person(object):
    __metaclass__ = ABCMeta
    

    def __init__(self, name, email):
        self.person_id = str(uuid.uuid4())[:8]
        self.name = name
        self.email = email
        self.office = None

    def set_office(self, office):
        self.office = office

    def __del__(self):
      return None


class Staff(Person):
    """"
      Creates staff
    """

    def __init__(self, name, email):
        self.person_type = "Staff"
        super(Staff, self).__init__(name, email)



class Fellow(Person):
    """
    Creates a fellow.
    
    """

    living_space = None

    def __init__(self, name, email, wants_accomodation='N'):
        self.person_type ="Fellow"
        self.wants_accomodation = wants_accomodation

        super(Fellow, self).__init__(name, email)

    def set_livingspace(self, new_space):
        if self.wants_accomodation == "Y":
            self.living_space = new_space
        else:
            return -1

