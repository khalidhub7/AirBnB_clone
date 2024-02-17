#!/usr/bin/python3
'''
AirBnB_ console'''
import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    '''
    define HBNBCommand class'''

    classes_defined = {'BaseModel', 'User', 'State',\
'City', 'Place', 'Amenity', 'Review'}

    prompt = '(hbnb)  '

    def do_EOF(self, line):
        '''
        EOF command'''
        return True

    def do_quit(self, line):
        '''
        Quit command to exit the program'''
        return True

    def emptyline(self):
        '''
        emptyline haldle'''
        pass

    '''def do_create(self, arg):
        """create command to creates a new instance\n"""
        className = arg.split()
        if len(className) == 0:
            print("** class name missing **")
        elif className[0] not in HBNBCommand.classes_defined:
            print("** class doesn't exist **")
        else:
            new_obj = eval(className[0])()
            storage.save()
            print(new_obj.id)'''

    def do_create(self, arg):
        '''
        create command to creates a new instance
        '''
        spliter = arg.split()
        if len(spliter) == 0:
            print('** class name missing **')
        if spliter[0] not in HBNBCommand.classes_defined:
            print('** class doesn\'t exist **')
        for i in HBNBCommand.classes_defined:
            if spliter[0] == i:
                new = i
if __name__ == '__main__':
    HBNBCommand().cmdloop()
