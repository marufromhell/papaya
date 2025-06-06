from stdio import *

"""
lp > "str\\n"                # basically printf, low level sys stdout requires newlines  
p > "str"                 # lp but with auto-newline   
li > "str"                # low level input with sys stdin  
hi > "str"                # input() wrapper  
hg > ''                   # args are ignored  
b64d > "base64string"     # returns decoded str  
cmd > "sh command"        # os.system wrapper  
pya > "PYTHON_CMD args"   # just a workaround for parenthesis cus i think its funny to not use them  
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