#!/usr/bin/python3
"""
Module defining the command interpreter
"""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    HBNB command interpreter class
    """
    prompt = "(hbnb) "
    classes = ["BaseModeli", "User"]

    def do_quit(self, line):
        """
        Method to exit the program
        """
        return True

    def help_quit(self, line):
        """
        Method to define exit command
        """
        print("Quit command to exit the program")

    def do_EOF(self, line):
        """
        Method to exit the program
        """
        print()
        return True

    def do_create(self, line):
        """
        Method to create a new instance of BaseModel and
        save it to the JSON file.
        """
        cmds = shlex.split(line)

        if len(cmds) == 0:
            print("** class name missing **")
        elif cmds[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            new_objct = eval(f"{cmds[0]}()")
            storage.save()
            print(new_objct.id)

    def do_show(self, line):
        """
        Method show the string representation of an instance.
        """
        cmds = shlex.split(line)

        if len(cmds) == 0:
            print("** class name missing **")
        elif cmds[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(cmds) < 2:
            print("** instance id missing **")
        else:
            Objs = storage.all()

            key = "{}.{}".format(cmds[0], cmds[1])
            if key in Objs:
                print(Objs[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """
        Method to delete an instance based on the class name and id.
        """
        cmds = shlex.split(line)

        if len(cmds) == 0:
            print("** class name missing **")
        elif cmds[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(cmds) < 2:
            print("** instance id missing **")
        else:
            Objs = storage.all()
            key = "{}.{}".format(cmds[0], cmds[1])
            if key in Objs:
                del Objs[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """
        Method to print the string representation of
        all instances or a specific class.
        """
        Objs = storage.all()

        cmds = shlex.split(line)

        if len(cmds) == 0:
            for key, value in Objs.items():
                print(str(value))
        elif cmds[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            for key, value in Objs.items():
                if key.split('.')[0] == cmds[0]:
                    print(str(value))

    def do_update(self, line):
        """
        Method to update an instance by adding or updating an attribute.
        """
        cmds = shlex.split(line)

        if len(cmds) == 0:
            print("** class name missing **")
        elif cmds[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(cmds) < 2:
            print("** instance id missing **")
        else:
            Objs = storage.all()

            key = "{}.{}".format(cmds[0], cmds[1])
            if key not in Objs:
                print("** no instance found **")
            elif len(cmds) < 3:
                print("** attribute name missing **")
            elif len(cmds) < 4:
                print("** value missing **")
            else:
                obj = Objs[key]
                att_name = cmds[2]
                att_value = cmds[3]
                try:
                    att_value = eval(att_value)
                except Exception:
                    pass
                setattr(obj, att_name, att_value)

                obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
