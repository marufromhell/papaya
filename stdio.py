"""
lp < "str\\n"             # basically printf, low level sys stdout requires newlines  
p < "str"                 # lp but with auto-newline   
li < "str"                # low level input with sys stdin
i < "str"                 # li wrapper, way better than li
hg < ''                   # getch, args are ignored but required
b64de < "base64string"    # returns decoded str
cmd < "sh command"        # os.system wrapper  
pya < "PYTHON_CMD args"   # just a workaround for parenthesis cus I think its funny to not use them
exe < "python"            # exec without formatting
"""
import os
import sys
import base64


class LowPrint:
    """Low level printing, requires newline at the end of string"""

    def __lt__(self, thing):
        try:
            sys.stdout.write(str(thing))
            sys.stdout.flush()
        except IOError as e:
            print(f"IO Error: {e}", file=sys.stderr)


lp = LowPrint()
"""Low level printing, requires newline at the end of string"""



class Print:
    """This is exactly the same as regular python builtin print()"""

    def __lt__(self, thing):  # __lt__ -< Less than allows redirection
        try:
            lp < f"{thing}\n"
        except IOError as e:
            lp < f"IO Error: {e}\n"


p = Print()
"""This is exactly the same as regular python builtin print()"""


class LowInput:
    def __lt__(self, thing):
        try:
            sys.stdout.write(str(thing))
            sys.stdout.flush()
            return sys.stdin.readline().rstrip('\n')
        except Exception as e:
            p < f'Error: {e}'
            return None


li = LowInput()
"""This is a low level input (doesnt format)"""


class Input:
    def __lt__(self, thing): # just a shorter version of li no real reason for it anymore
        try:
            a = li < str(thing)
            return a
        except Exception as e:
            p < e


i = Input()
"""Same as regular python input()"""


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()  # type: ignore # im on a linux system


class _Getch:
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self):
        return self.impl()


getch = _Getch()
"""Takes one key as input, win/linux only"""


class HighGetch:
    def __lt__(self, thing):
        return getch()


hg = HighGetch()
"""Takes one key as input, win/linux only"""


class B64d:
    def __lt__(self, thing):
        b64str = thing
        b64b = b64str.encode("ascii")
        strb = base64.b64decode(b64b)
        return strb.decode("ascii")


b64de = B64d()
"""Decodes a base64 string"""


class Command:
    def __lt__(self, thing):
        os.system(thing)


cmd = Command()
"""executes string with os.system"""


class Pyargs:
    def __lt__(self, string):
        import sys
        caller_globals = sys.modules['__main__'].__dict__
        parts = string.split(maxsplit=1)
        self.cmd = parts[0] if parts else ""
        self.args = parts[1] if len(parts) > 1 else ""
        return eval(f"{self.cmd}({self.args})", caller_globals)


pya = Pyargs()
"""Takes first word as argument and everything after in parenthesis"""


class Execute:
    def __lt__(self, string):
        caller_globals = sys.modules['__main__'].__dict__
        return eval(string, caller_globals)  # Using eval instead of exec to get return value


exe = Execute()
"""execs a string"""


class MoveToStdio:
    def __lt__(self, thing):
        caller_globals = sys.modules['__main__'].__dict__
        caller_globals[thing] = str(thing)


mov = MoveToStdio()
""" probably useless now, but moves anything into the outer scope"""


class MakeStr:
    def __lt__(self, thing):
        return str(thing)


mkstr = MakeStr()
"""str()"""


class MakeInt:
    def __lt__(self, thing):
        return int(thing)
mkint=MakeInt()
