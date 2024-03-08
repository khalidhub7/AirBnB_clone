from models.engine.file_storage import FileStorage
from models import storage
import shlex
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    # Prompt displayed for user input
    prompt = "(hbnb) "
    # List of classes available for creating instances
    classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

    def do_create(self, arg):
        # Command to create a new instance of a class
        class_name = arg.split()
        if len(class_name) == 0:
            print("** class name missing **")
        elif class_name[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            # Create a new instance of the specified class
            new_instance = eval(class_name[0])()
            storage.save()
            print(new_instance.id)

    def check_instance_exists(self, arg):
        # Helper function to check if an instance exists
        myargs = shlex.split(arg)
        if len(myargs) < 2 or myargs[0]+"."+myargs[1] not in storage.all():
            print("** no instance found **")
            return False
        return True

    def do_show(self, arg):
        # Command to show an instance
        if self.check_instance_exists(arg):
            print(storage.all()["{}.{}".format(*shlex.split(arg))])

    def do_destroy(self, arg):
        # Command to destroy an instance
        if self.check_instance_exists(arg):
            del storage.all()["{}.{}".format(*shlex.split(arg))]
            storage.save()

    def do_all(self, arg):
        # Command to display all instances of a class
        if not arg:
            print([str(storage.all()[key]) for key in storage.all()])
        elif arg in HBNBCommand.classes:
            print([str(storage.all()[key]) for key in storage.all() if arg in key])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        # Command to update an instance
        if self.check_instance_exists(arg) and len(shlex.split(arg)) >= 4:
            args = shlex.split(arg)
            obj = storage.all()["{}.{}".format(*args)]
            attr = args[2]
            try:
                value = eval(args[3])
            except NameError:
                value = args[3]
            setattr(obj, attr, value)
            obj.save()

    def do_quit(self, arg):
        # Command to quit the program
        return True

    def do_EOF(self, arg):
        # Command to handle end of file (Ctrl+D)
        return True

    def emptyline(self):
        # Handle an empty line
        pass

if __name__ == '__main__':
    # Start the command loop
    HBNBCommand().cmdloop()
