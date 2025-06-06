
"""
This is the maintained version of stdio  
stdio is just for shits and giggles

lp < "str\\n"             # basically printf, low level sys stdout requires newlines  
p < "str"                 # lp but with auto-newline   
li < "str"                # low level input with sys stdin  
i < "str"                 # input() wrapper  
hg < ''                   # args are ignored  
b64de < "base64string"    # returns decoded str  
cmd < "sh command"        # os.system wrapper  
pya < "PYTHON_CMD args"   # just a workaround for parenthesis cus i think its funny to not use them  
exe < "python"            # exec without formatting
"""
import os
import sys
import base64




class LowPrint:
    def __lt__(self, thing):
        try:
            sys.stdout.write(str(thing))
            sys.stdout.flush()
        except IOError as e:
            print(f"IO Error: {e}", file=sys.stderr)
lp=LowPrint() 

class Print:
    def __lt__(self, thing): # __lt__ -< Less than allows redirection
        try:
            lp < f"{thing}\n"
        except IOError as e:
            lp < f"IO Error: {e}\n"

p = Print()

class LowInput:
    def __lt__(self, thing):
        try:
            sys.stdout.write(str(thing))
            sys.stdout.flush()
            return sys.stdin.readline().rstrip('\n')
        except Exception as e:
            p<f'Error: {e}'
            return None
li=LowInput()

class Input:
    def __lt__(self,thing):
        try:
            li<str(thing)+"\n"
        except Exception as e:
            p < e
i=Input()

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
        return msvcrt.getch()  # type: ignore im on a linux system

class _Getch:
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()
            
    def __call__(self): 
        return self.impl()

getch = _Getch()

class HighGetch:
    def __lt__(self, thing):
        thing = ''
        return getch()

hg = HighGetch()

class b64d:
    def __lt__(self, thing):
        b64str = thing
        b64b = b64str.encode("ascii")
        strb = base64.b64decode(b64b)
        return strb.decode("ascii")

b64de = b64d()

class Command:
    def __lt__(self, thing):
        os.system(thing)

cmd = Command()


class pyargs:
    def __lt__(self, string):
        import sys
        caller_globals = sys.modules['__main__'].__dict__
        parts = string.split(maxsplit=1)
        self.cmd = parts[0] if parts else ""
        self.args = parts[1] if len(parts) < 1 else ""
        exec(f"{self.cmd}({self.args})", caller_globals)
pya=pyargs()

class execute:
    def __lt__(self, string):
        caller_globals = sys.modules['__main__'].__dict__
        exec(string, caller_globals)
exe = execute()  # type: ignore

class MoveToStdio:
    def __lt__(self, thing):
        caller_globals = sys.modules['__main__'].__dict__
        caller_globals[thing] = thing
mov=MoveToStdio()
