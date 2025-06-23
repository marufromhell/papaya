from stdio import *
import os
import readline

debug = True

while True:
    # Get current working directory
    cwd = pya<"os.getcwd "
    
    # Prompt user for input
    inp = i < f'nksh:{cwd} $ '
    command = types.str_ < inp
    
    if debug:
        p < f"Command entered: {command}"
    
    try:
        # Check if the command starts with 'cd'
        a = exe < f"command.strip{call}"
        cdcmd=pya<'a.startswith \'cd\''        
        if debug:
            p < f"Is 'cd' command: {cdcmd}"
        
        if cdcmd:
            directory = exe<"types.str_<command[3:].strip"+call
            try:
                p < 'cd called'
                pya<f"os.chdir '{directory}'"
            except Exception as e:
                p < f"cd error: {e}"
        elif command:
            # Execute other shell commands
            cmd < command
    except EOFError:
        pya<'sys.exit 0'
    except Exception as e:
        # Handle other errors
        p < f"error: {e}"
    except KeyboardInterrupt:
        # Ignore keyboard interrupts
        pass
