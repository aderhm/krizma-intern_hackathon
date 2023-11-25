from uuid import uuid4
from models import storage


class Recette():
    """
        The class Recette
    """
    def __init__(self, *args, **kwargs):
        """
        Initializing
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            storage.new(self)

    def __str__(self):
        """
        Returns the string format of the object.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
    
    def save(self):
        """
        Save object in the json file.
        """
        storage.save()

    def to_dict(self):
        """
        Returns the dict format of the object.
        """
        dict_format = self.__dict__.copy()
        dict_format['__class__'] = self.__class__.__name__
        return dict_format
