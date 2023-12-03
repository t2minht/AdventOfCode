'''
p1 sudo code
We only care about numbers attached to symbols
So parse through each line, check for the first instance of a symbol that isn't numeric or a period
Get that j value, check all values i-1, i, i+1 on levels j-1, j, j+1 for smtg numeric
If numberic, check values j-1 and j+1 repeatedly to find the full number
* recursive outside function? check left and right of current value, if numeric, run again, if not, return upper value.
* kinda 2 pointer-y?
once you have full number, add to sum
'''
