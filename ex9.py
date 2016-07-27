# Here's some strange stuff, remember type it exactly

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\nSep\nOct\nNov\nDec"


print 'Here are the days: ', days
print 'Here are the months: ', months

print 'Here are the months: %r' % months
# escape sequence characters does not work with %r (raw)

print """
There is something going on here.
With the three double quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""

for i in ["/", "-", "|", "\\", "|"]:
    print "%s\r" % i,

# %r prints it the way you'd write it in your file,
# but %s prints it the way you'd like to see it
