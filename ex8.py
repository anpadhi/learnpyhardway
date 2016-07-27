formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ('One', 'Two', 'Three', 'Four')
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
# 'I had this thing.' 'That you could type up right.' "But it didn't sing."
# 'So I said goodnight.' --- why the double quote in the third string ?

# %s - Any string
# %r - raw string, only use for getting debugging information about something
