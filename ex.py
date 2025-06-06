from stdio import *

"""
lp < "str\\n"             # basically printf, low level sys stdout requires newlines  
p < "str"                 # lp but with auto-newline   
li < "str"                # low level input with sys stdin  
i < "str"                 # li but with auto newline
hg < ''                   # args are ignored  getch's input Linux and windows(no darwin)
b64d < "base64string"     # returns decoded str  
cmd < "sh command"        # os.system wrapper  
pya < "PYTHON_CMD args"   # just a workaround for parenthesis cus i think its funny to not use them  
exe < var OR "python code"# exec wrapper
"""

a='hi'
b='hello'
pya<"print a,b"
p < "hi"
cmd < 'echo hi from cli'
p<'hello';
lp<'hello\n';
p<'HI';
x=li < 'input: ';
p<x;
q=b64de < "R2VuZXJpYyBRdWVzdGlvbiAoeS9uKQ==";
p<q;
r=hg < ''
rsp=f"You responded: {r}";
p<rsp;
