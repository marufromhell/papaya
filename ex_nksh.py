from stdio import *
import os
import readline

"""
lp < "str\\n"             # basically printf, low level sys stdout requires newlines  
p < "str"                 # lp but with auto-newline   
li < "str"                # low level input with sys stdin  
i < "str"                 # li but with auto newline
hg < ''                   # getch, args are ignored but required
b64de < "base64string"    # returns decoded str
cmd < "sh command"        # os.system wrapper  
pya < "PYTHON_CMD args"   # just a workaround for parenthesis cus i think its funny to not use them  
exe < "python"            # exec without formatting
"""

while True:
    cwd = pya<'os.getcwd  '
    inp = i < f'nksh:{cwd} $ '
    command = mkstr < inp
    try:
        cdcmd = f'"{command}".startswith cd'
        if pya < cdcmd:
            directory = mkstr < command[3:]
            try:
                p<'cd called'
                pya<f'os.chdir "{directory}"'
            
            except Exception as e:
                p < f"cd error: {e}"
        elif command:
            cmd < command
    except EOFError:
        pya<'sys.exit 0'

    except Exception as e:
        p < f"error: {e}"

    except KeyboardInterrupt:
        pass