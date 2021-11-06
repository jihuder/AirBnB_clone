#!/usr/bin/python3
"""Module: console.py"""
import cmd
import models
import re
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ command line interpreter"""

    prompt = '(hbnb) '

    def do_create(self, new_obj):
        """ Creates a new instance of different classes,
            saves it (to the JSON file) and prints the id\n """
        new_obj.split()
        if not new_obj:
            print("** class name missing **")
            return
        classes = ["BaseModel", "User", "State",
                   "City", "Amenity", "Place", "Review"]
        if new_obj not in classes:
            print("** class doesn't exist **")
            return
        for _class in classes:
            if _class == new_obj:
                obj = eval(_class + "()")
        obj.save()
        print(obj.id)

    def do_show(self, args):
        """ Prints the string representation of an instance
            based on the class name and id\n """
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        name_class = args[0]
        if name_class not in ["BaseModel", "User", "State",
                              "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return
        if len(args) > 1:
            obj_id = args[1]
        else:
            print("** instance id missing **")
            return
        all_objs = models.storage.all()
        for value in all_objs.values():
            if obj_id == value.id:
                if name_class == value.__class__.__name__:
                    print(value)
                    return
        print("** no instance found **")

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id\n """
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        name_class = args[0]
        if name_class not in ["BaseModel", "User", "State",
                              "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return
        if len(args) > 1:
            obj_id = args[1]
        else:
            print("** instance id missing **")
            return
        all_objs = models.storage.all()
        for key, value in all_objs.items():
            if obj_id == value.id:
                if name_class == value.__class__.__name__:
                    del all_objs[key]
                    models.storage.save()
                    return
        print("** no instance found **")

    def do_all(self, args):
        """ Prints all string representation of all instances
            based or not on the class name\n"""
        all_objs = models.storage.all()
        all_list = []
        if not args:
            for obj in all_objs.values():
                all_list.append(str(obj))
            print(all_list)
            return
        else:
            if args not in ["BaseModel", "User", "State",
                            "City", "Amenity", "Place", "Review"]:
                print("** class doesn't exist **")
                return
            for obj in all_objs.values():
                if obj.__class__.__name__ == args:
                    all_list.append(str(obj))
            print(all_list)

    def do_update(self, args):
        """ Updates an instance based on the class name and id
            by adding or updating attribute
            (save the change into the JSON file)
            Usage:
            update <class name> <id> <attribute name> "<attribute value>\n"""
        if not args:
            print("** class name missing **")
            return
        if "{" in args:
            args = args.replace("{", "").replace("}", "").replace("'", "")
            args = args.replace(":", "").split(",")
            for element in range(1, len(args)):
                go = self.do_update(args[0] + " " + args[element])
                if go == -1:
                    return
            return
        args = args.replace(',', '')
        args = args.split()
        name_class = args[0]
        if name_class not in ["BaseModel", "User", "State",
                              "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return
        if len(args) > 1:
            obj_id = args[1]
        else:
            print("** instance id missing **")
            return
        all_objs = models.storage.all()
        found = False
        for key, value in all_objs.items():
            if obj_id == value.id:
                if name_class == value.__class__.__name__:
                    found = True
                    if len(args) > 2:
                        if len(args) > 3:
                            break
                        else:
                            print("** value missing **")
                            return
                    else:
                        print("** attribute name missing **")
                        return
        if not found:
            print("** no instance found **")
            return (-1)
        attr_name = args[2]
        attr_value = args[3].replace('"', '')
        # print("args_2:", args)
        if attr_value.isdigit():
            attr_value = int(attr_value)
        else:
            try:
                attr_value = float(attr_value)
            except:
                pass
        all_objs[key].__dict__[attr_name] = attr_value
        models.storage.save()

    def do_count(self, arg):
        all_objs = models.storage.all()
        count = 0
        for key in all_objs:
            if arg in key:
                count += 1
        print(count)

    def precmd(self, line):
        """Hook method executed just before the
            command line line is interpreted.
            Modify to allow comands in the way arg.command()"""
        if "." in line:
            # arg_n = re.search('\((.+?)\)', line[1])
            line = line.replace("(", " ")
            line = line.replace(")", " ")
            line = line.replace(".", " ")
            line = line.split()
            command = line[1]
            args = line[0]
            for index in range(2, len(line)):
                args += " " + line[index].replace('"', '')
            return command + " " + args
        else:
            return line

    def do_quit(self, line):
        """ Quit command to exit the program\n """
        return True

    def do_EOF(self, line):
        """ Quit command to exit the program\n """
        print()
        return True

    def emptyline(self):
        """ Handle empty lines"""
        return

if __name__ == '__main__':
    HBNBCommand().cmdloop()