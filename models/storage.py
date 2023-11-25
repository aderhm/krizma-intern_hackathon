import json
import importlib


class Storage:
    """
    Stores data in a JSON file.
    """

    __file_path = 'karizmahack_db.json'
    __objects = {}

    def all(self):
        """
        Returns all object from __objects.
        """
        return Storage.__objects

    def new(self, obj):
        """
        Create a new object and store it in __objects.
        """
        key_obj = "{}.{}".format(obj.__class__.__name__, obj.id)
        Storage.__objects[key_obj] = obj

    def save(self):
        """
        Save the new object in karizmahack_db.
        """
        new_dict = {}
        for key, value in Storage.__objects.items():
            new_dict[key] = value.to_dict()

        with open(Storage.__file_path, 'w') as file:
            json.dump(new_dict, file)

    def reload(self):
        """
        Loads all objects from karizmahack_db.
        """
        try:
            with open(Storage.__file_path, 'r') as file:
                data = json.load(file)
            
            for key, value in data.items():
                class_name = key.split('.')[0]
                model_path = 'models.{}{}'.format(
                    class_name[0].lower(), class_name[1:]
                )
                model = importlib.import_module(model_path)
                cls = getattr(model, class_name)
                Storage.__objects[key] = cls(**value)

        except FileNotFoundError:
            return
