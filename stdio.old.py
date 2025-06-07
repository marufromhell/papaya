
"""
lp < "str\\n"               # basically printf, low level sys stdout requires newlines  
p < "str"                 # lp but with auto-newline   
li < "str"\\n                # low level input with sys stdin  
i < "str"                 # li with newline
hg < ''                   # args are ignored  
b64de < "base64string"    # returns decoded str  
cmd < "sh command"        # os.system wrapper  
pya < "PYTHON_CMD args"   # just a workaround for parenthesis cus i think its funny to not use them  
exe < "python"            # exec without formatting
"""
import os
import sys
exec("""\nclass LowPrint:\n    def __lt__(self, thing):\n        try:\n            sys.stdout.write(str(thing))\n            sys.stdout.flush()\n        except IOError as e:\n            print(f"IO Error: {e}", file=sys.stderr)\n""");lp=LowPrint();# type: ignore
exec("""\nclass Print:\n    def __lt__(self, thing): # __lt__ -< Less than allows redirection\n        try:\n            lp < f"{thing}\\n"\n        except IOError as e:\n            lp < f"IO Error: {e}\\n"\n""");p = Print()# type: ignore
exec("""\nclass LowInput:\n    def __lt__(self, thing):\n        try:\n            sys.stdout.write(str(thing))\n            sys.stdout.flush()\n            return sys.stdin.readline().rstrip('\\n')\n        except Exception as e:\n            p<f'Error: {e}'\n            return None\n""");li=LowInput();# type: ignore
exec("""\nclass Input:\n    def __lt__(self,thing):\n        try:\n            li<str(thing)+"\\n"\n        except Exception as e:\n            p < e\n""");i=Input()# type: ignore
exec("""\nclass _GetchUnix:\n    def __init__(self):\n        import tty, sys\n    def __call__(self):\n        import sys, tty, termios\n        fd = sys.stdin.fileno()\n        old_settings = termios.tcgetattr(fd)\n        try:\n            tty.setraw(sys.stdin.fileno())\n            ch = sys.stdin.read(1)\n        finally:\n            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)\n        return ch\nclass _GetchWindows:\n    def __init__(self):\n        import msvcrt\n    def __call__(self):\n        import msvcrt\n        return msvcrt.getch() # type: ignore im on a linux system\nclass _Getch:\n    def __init__(self):\n        try:\n            self.impl = _GetchWindows()\n        except ImportError:\n            self.impl = _GetchUnix()\n    def __call__(self): return self.impl()\n""");getch = _Getch();# type: ignore
exec("""\nclass HighGetch:\n    def __lt__(self, thing):\n        thing = ''\n        return getch()\n""");hg = HighGetch();# type: ignore
exec("""\nimport base64 \nclass b64d:\n    def __lt__(self, thing):\n        b64str=thing\n        b64b = b64str.encode("ascii")\n        strb = base64.b64decode(b64b)\n        return strb.decode("ascii")\n""");b64de=b64d();# type: ignore
exec("""\nclass Command:\n    def __lt__(self, thing):\n        os.system(thing)\n""");cmd=Command();# type: ignore
exec("""\nclass pyargs:\n    def __lt__(self, string):\n        import sys\n        caller_globals = sys.modules['__main__'].__dict__\n        parts = string.split(maxsplit=1)\n        self.cmd = parts[0] if parts else ""\n        self.args = parts[1] if len(parts) < 1 else ""\n        exec(f"{self.cmd}({self.args})", caller_globals)\n""");pya=pyargs();# type: ignore
exec("""\nclass MoveToStdio:\n    def __lt__(self, thing):\n        import sys\n        caller_globals = sys.modules['__main__'].__dict__\n        caller_globals[thing] = thing\n""");mov=MoveToStdio();# type: ignore
exec("""\nclass execute:\n    def __lt__(self,string):\n        caller_globals = sys.modules['__main__'].__dict__;exec(string, caller_globals);\n""");exe=execute()#type: ignore
