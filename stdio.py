"""
lp < "str\\n"             # basically printf, low level sys stdout requires newlines  
p < "str"                 # lp but with auto-newline   
li < "str"                # low level input with sys stdin
i < "str"                 # li wrapper, way better than li
hg < ''                   # getch, args are ignored but required
hc < ''                   # uses escape chars for clear, unless system is windows, then system cls
b64de < "base64string"    # returns decoded str
cmd < "sh command"        # os.system wrapper  
pya < "PYTHON_CMD args"   # just a workaround for parenthesis cus I think its funny to not use them
exe < "python"            # exec without formatting
"""

import os
import sys
import base64
if os.name == "nt":
    import msvcrt
else:
    import tty
    import termios






call="()"





# -------------------------
# Printing Functions
# -------------------------

class LowPrint:
    """Low level printing, requires newline at the end of string"""
    def __lt__(self, thing):
        try:
            sys.stdout.write(str(thing))
            sys.stdout.flush()
        except IOError as e:
            print(f"IO Error: {e}", file=sys.stderr)
lp = LowPrint()

class Print:
    """This is exactly the same as regular python builtin print()"""
    def __lt__(self, thing):
        try:
            lp < f"{thing}\n"
        except IOError as e:
            lp < f"IO Error: {e}\n"
p = Print()












# -------------------------
# Input Functions
# -------------------------

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

class Input:
    def __lt__(self, thing):
        try:
            a = li < str(thing)
            return a
        except Exception as e:
            p < e
i = Input()


class _GetchUnix:
    def __call__(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

class _GetchWindows:
    def __call__(self):
        return msvcrt.getch()  # type: ignore

class _Getch:
    def __init__(self):
        if os.name == "nt":
            self.impl = _GetchWindows()
        else:
            self.impl = _GetchUnix()
    def __call__(self):
        return self.impl()
getch = _Getch()

class HighGetch:
    def __lt__(self, thing):
        return getch()
hg = HighGetch()








# -------------------------
# Terminal Control
# -------------------------

class clear:
    def __lt__(self, thing):
        if os.name == "nt":
            os.system('cls')
        else:
            lp < '\033c'
        return thing
hc = clear()











# -------------------------
# System/Utility Functions
# -------------------------

class Command:
    def __lt__(self, thing):
        os.system(thing)
cmd = Command()









# -------------------------
# PAPAYA WORKAROUNDS
# -------------------------

class Def:
    def __lt__(self, thing):
        """
        thing: a string like "foo x, y: return x + y"
        Defines a function named foo with args x, y and body 'return x + y'
        """
        import sys
        caller_globals = sys._getframe(1).f_globals
        name, rest = thing.split(' ', 1)
        args, body = rest.split(':', 1)
        code = f"def {name}({args.strip()}):\n    {body.strip()}"
        exec(code, caller_globals)
def_ = Def()

class Pyargs:
    def __lt__(self, string):
        caller_globals = sys.modules['__main__'].__dict__
        parts = string.split(maxsplit=1)
        self.cmd = parts[0] if parts else ""
        self.args = parts[1] if len(parts) > 1 else ""
        return eval(f"{self.cmd}({self.args})", caller_globals)
pya = Pyargs()

class Execute:
    def __lt__(self, string):
        caller_globals = sys.modules['__main__'].__dict__
        return eval(string, caller_globals)
exe = Execute()

class MoveToStdio:
    def __lt__(self, thing):
        caller_globals = sys.modules['__main__'].__dict__
        caller_globals[thing] = str(thing)
mov = MoveToStdio()


#  Typing functions
class types:
    class Type:
        def __lt__(self, thing):
            return type(thing)
    type_ = Type()
        
    class MakeStr:
        def __lt__(self, thing):
            return str(thing)
    str_ = MakeStr()

    class MakeInt:
        def __lt__(self, thing):
            return int(thing)
    int_ = MakeInt()

    class MakeFloat:
        def __lt__(self, thing):
            return float(thing)
    float_ = MakeFloat()

    class MakeBool:
        def __lt__(self, thing):
            return bool(thing)
    bool_ = MakeBool()

    class MakeList:
        def __lt__(self, thing):
            return list(thing)
    list_ = MakeList()

    class MakeTuple:
        def __lt__(self, thing):
            return tuple(thing)
    tuple_ = MakeTuple()

    class MakeDict:
        def __lt__(self, thing):
            return dict(thing)
    dict_ = MakeDict()

    class MakeSet:
        def __lt__(self, thing):
            return set(thing)
    set_ = MakeSet()

    class MakeBytes:
        def __lt__(self, thing):
            return bytes(thing)
    bytes_ = MakeBytes()

    class MakeComplex:
        def __lt__(self, thing):
            return complex(thing)
    complex_ = MakeComplex()




    # input validation
    class IsStr:
    
        def __lt__(self, thing):
            return isinstance(thing, str)
    isstr = IsStr()

    class IsInt:
        def __lt__(self, thing):
            return isinstance(thing, int)
    isint = IsInt()

    class IsFloat:
        def __lt__(self, thing):
            return isinstance(thing, float)
    isfloat = IsFloat()

    class IsBool:
        def __lt__(self, thing):
            return isinstance(thing, bool)
    isbool = IsBool()

    class IsList:
        def __lt__(self, thing):
            return isinstance(thing, list)
    islist = IsList()

    class IsTuple:
        def __lt__(self, thing):
            return isinstance(thing, tuple)
    istuple = IsTuple()

    class IsDict:
        def __lt__(self, thing):
            return isinstance(thing, dict)
    isdict = IsDict()

    class IsSet:
        def __lt__(self, thing):
            return isinstance(thing, set)
    isset = IsSet()

    class IsNone:
        def __lt__(self, thing):
            return thing is None
    isnone = IsNone()

    class IsBytes:
        def __lt__(self, thing):
            return isinstance(thing, bytes)
    isbytes = IsBytes()

    class IsComplex:
        def __lt__(self, thing):
            return isinstance(thing, complex)
    iscomplex = IsComplex()

    class IsCallable:
        def __lt__(self, thing):
            return callable(thing)
    iscallable = IsCallable()

    class IsObject:
        def __lt__(self, thing):
            return isinstance(thing, object)
    isobject = IsObject()













# -------------------------
# OTHER
# -------------------------
class B64d:
    def __lt__(self, thing):
        b64str = thing
        b64b = b64str.encode("ascii")
        strb = base64.b64decode(b64b)
        return strb.decode("ascii")
b64de = B64d()






#test
def main():
    def_ < "test arg1: lp<arg1"
    pya < 'test \'hi\'';lp<'\n'

if __name__ == "__main__":
    main()
