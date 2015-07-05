t = input()
if t%10!=0: print -1
else: print t/300,; t-=(t/300)*300;print t/60,; t-=(t/60)*60; print t/10
