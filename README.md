# eulerPy
Euler problems in Python

The pieces of code here are my solutions to the Project Euler problems. 
Project Euler discourages posting solutions outside their discussion threads.
If you proceed to reading this code, you understand that you are depriving yourself the experience gained from solving the Euler problems yourself.

## Skipped problems:

### Problem 17: 
Easier to do by hand.
from 1-9 it's 3+3+5+4+4+3+5+5+4 = 36
from 10-19 it's 3+6+6+8+8+7+7+9+8+8 = 70
from 20-99 it's 10*(6+6+5+5+5+7+6+6)+8*36 = 748
which is 10 of whatever prefix (twenty, thirty, forty etc), and the 1-9 values again, per digit.
from 100-999 it's more complicated:
1-9 happens 100 times (ten per 100, for 10 100s) so 100*36 = 3600
1-99 happens happens 9 times, so 9*854 = 7686
'hundred' happens 9 times so  7*9 = 63
'hundred and' happens 999 times so 999*10 = 8910
summing up gives 3600 + 7686 + 63 + 8910= 20259

so now for all 854 + 20259 = 21113.
then we add 11 for 'one thousand'. 21124. 
