'''
How to use Modules, Packages, and The Python Standard Library

1.  Python Standard Library:
    a) I'll show 3 methods available in the os package.
       i)   To describe what the method does.
       ii)  To show a sample usage of the method.
       iii) and To display the help() page for the method.

'''

os.getegid()
        This method returns the effective group id of the current process. This correspondace to the "set id" bit on the file being executed
        in the current process.
    Example: Import os
                os.getegid()
                20
    To view the help page for that method, help(os.getegid)

os.getgroups()
        This method returns the list of supplemental group ids associated with the current process.
    Example: Import os
                os.getgroups()
                [20,19,26,27,32,100,204,395]

os.getlogin()
        This method return the name of the user logged in on the controlling terminal of the process.
    Example: Import os
                os.getlogin()
                'Arun'
'''

    b) This is an example of how to use the logging package.

'''
Logging means tracking events in software applications, Python provides Logging API which includes our own messages integrated with
messages from third-party modules.
Example:
    logger = logging.getLogger('tcpserver')
    logger.warning('Protocol problem: %s','connection reset')
 This returns Protocol problem when it failed to connect with tcpserver.
'''

    c) Working on Package available in the Python Standard Library.
       i)   Illustrate the usage of the module you choose.
       ii)  Explained where and why someone would use it.

'''
I have chose enum.py package, it is a set of symbolic names (members) bound to unique , constant values.This modulw defines two enumeration classes that can be
used to define unique sets of names and values: Enum and IntEnumself.

These two classes can be used to enumerated constants. Enumeration members have human readable string representations.
Example :   from enum import Enum
            class Color(Enum)
                red = 1
                green = 2
                blue = 3
        Here class Color is an enumaeration (or enum)
        And attributes Color.red, Color.green , etc are enumeration members
        >>> print(Color.red)
            "Color.red"
        >>> print(repr(Color.red))
            <Color.red : 1>
    To view the help page for that method, help, then type enum
