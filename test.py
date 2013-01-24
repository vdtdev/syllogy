from syllogism import Terms
from syllogism import Form
from syllogism import Statement
from syllogism import Syllogism
t = Terms("P","Q")
a = Form(True,True)
b=Form(False,False)
u = Terms("Q","S")
c=Form(False,True)
v = Terms("S","P")
M=Statement(t,a)
m=Statement(u,b)
C=Statement(v,c)

s = Syllogism(M,m,C)
s.formal()
s.figure()
