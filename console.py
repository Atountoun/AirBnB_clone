#!/usr/bin/python3
"""
This module defines a class which is the entry point of the command
interpreter.
"""
import cmd
import string
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
import re

classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
        }


class HBNBCommand(cmd.Cmd):
    """The class that represents the entry point of the command
    interpreter. It inherits Cmd class of python's cmd module.
    """
    prompt = "(hbnb) "
    identchars = string.ascii_letters + string.digits + '.)"(_'

    def get_data(self):
        return storage.all()

    def do_create(self, arg):
        """Create a new instance of BaseModel, saves it to the
        JSON file prints the id.
        Example: create BaseModel
        """
        class_name = arg
        if not class_name:
            print("** class name missing **")
            return
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        instance = classes[class_name]()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based
        on the class name and id.
        Example: show BaseModel 1234-1234-1234
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.strip().split(" ")
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        try:
            instance_id = args[1]
        except Exception:
            instance_id = None
        if not instance_id:
            print("** instance id missing **")
            return
        objects = self.get_data()
        if instance_id.startswith('"') and instance_id.endswith('"'):
            instance_id = instance_id[1:-1]
        object_id = class_name + "." + instance_id
        try:
            instance_dict = objects[object_id].to_dict()
        except Exception:
            instance_dict = None
        if not instance_dict:
            print("** no instance found **")
            return
        instance = classes[class_name](**instance_dict)
        print(instance)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id.
        The change is saved into the JSON file.
        Example: destroy BaseModel 121212
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.strip().split(" ")
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        try:
            instance_id = args[1]
        except Exception:
            instance_id = None
        if not instance_id:
            print("** instance id missing **")
            return
        objects = self.get_data()
        if instance_id.startswith('"') and instance_id.endswith('"'):
            instance_id = instance_id[1:-1]
        object_id = class_name + "." + instance_id
        if object_id not in objects.keys():
            print("** no instance found **")
            return
        del objects[object_id]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based on not
        on the class name.
        Format: all <class name>; all
        """
        class_name = arg
        instances = []
        objects = self.get_data()
        if class_name:
            if class_name not in classes:
                print("** class doesn't exist **")
                return
            for obj in objects.values():
                if obj.to_dict()["__class__"] == class_name:
                    instance = classes[obj.to_dict()["__class__"]](**obj.to_dict())
                    instances.append(str(instance))
        else:
            for obj in objects.values():
                instance = classes[obj.to_dict()["__class__"]](**obj.to_dict())
                instances.append(str(instance))
        print(instances)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding
        or updating attribute (it is saved into the JSON file.
        Example: update <class name> <id> <attribute name> <attribute value>
        """
        if not arg:
            print("** class name missing **")
            return
        arg = arg.replace(',', ' ')
        args_list = arg.split()
        class_name = args_list[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        try:
            instance_id = args_list[1]
        except Exception:
            print("** instance id missing **")
            return
        objects = self.get_data()
        if instance_id.startswith('"') and instance_id.endswith('"'):
            instance_id = instance_id[1:-1]
        object_id = class_name + "." + instance_id
        if object_id not in objects.keys():
            print("** no instance found **")
            return
        instance = objects[object_id].to_dict()
        try:
            attribute_name = args_list[2].replace('"', '')
            no_update_permit = ["id", "created_at", "updated_at"]
            if attribute_name in no_update_permit:
                raise Error("can't update this attribute")
        except Exception:
            print("** attribute name missing **")
            return
        others_args = args_list[3:]
        if len(others_args) == 0:
            print("** value missing **")
            return
        if others_args[0].startswith('"'):
            attribute_value = others_args[0][1:]
            if not attribute_value.endswith('"'):
                for ele in others_args[1:]:
                    if not ele.endswith('"'):
                        attribute_value += " " + ele
                    else:
                        attribute_value += " " + ele[:-1]
                        break
            else:
                attribute_value = others_args[0][1:-1]
        else:
            try:
                attribute_value = int(others_args[0])
            except ValueError:
                attribute_value = float(others_args[0])
            except Exception:
                print("** invalid type **")
                return
        attribute_name = attribute_name.strip()
        instance[attribute_name] = attribute_value
        instance_obj = classes[class_name](**instance)
        instance_obj.save()

    def do_count(self, arg):
        """Retrieve the number of instances of a class
        Format: count <class name>
        """
        if not arg:
            print("** class name missing **")
            return
        class_name = arg.split()[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        objects = self.get_data()
        number_of_instances = 0
        for obj in objects.values():
            if obj.to_dict()["__class__"] == class_name:
                number_of_instances += 1
        print(number_of_instances)

    def precmd(self, line):
        """Hook method executed just before the command line is interpreted,
        but after the input prompt is generated and issued.
        """
        class_name = line.split('.')[0]
        if class_name in classes:
            right_of_line = line.split('.')[1]
            cmd = re.split(r"\)|\(", right_of_line)[0]
            args = " ".join(re.split(r"\)|\(", right_of_line)[1:-1])
            reformated_cmd = cmd + " " + class_name + " " + args
            return reformated_cmd
        return line

    def parseline(self, line):
        """Parse the line into a command name and a string containing
        the arguments.
        Return:
            A tuple contaning (command, args, line).
        'command' and 'args' may be None if the line couldn't be parsed.
        """
        line = line.strip()
        if not line:
            return None, None, line
        if line[0] == '?':
            line = 'help ' + line[1:]
        elif line[0] == '!':
            if hasattr(self, 'do_shell'):
                line = 'shell ' + line[1:]
            else:
                return None, None, line
        i, n = 0, len(line)
        while i < n and line[i] in self.identchars:
            i += 1
        cmd, arg = line[:i], line[i:].strip()
        return cmd, arg, line

    def do_quit(self, arg):
        """Quit command to exit the program"""
        print()
        return True

    def do_EOF(self, arg):
        """ctrl + d command is dispatched to do_EOF which exit the
        command interpreter.
        """
        print()
        return True

    def emptyline(self):
        """Handle the repeat of the last command when an empty line
        is entered and the user press ENTER
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
