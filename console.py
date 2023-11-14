#!/usr/bin/python3
"""
Module defining the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNB command interpreter class
    """
    prompt = "(hbnb) "

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

    def emptyline(self):
        """
        Called when an empty line is entered in response to the prompt.
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
