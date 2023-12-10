"""H3. Modify old style format into #1 string with format() and #2 f-string."""

# 1 string with format()
norway_text_format_method = 'Automatisering akselererer {0}yeblikket da roboter vil erobre planeten v{1}r. ({2})'.format('ø', 'å', 'Æ')
print(norway_text_format_method)

# 2 f-string
first_var = 'ø'
second_var = 'å'
third_var = 'Æ'
fstring = (f'Automatisering akselererer {first_var}yeblikket da '
           f'roboter vil erobre planeten v{second_var}r. ({third_var})')
print(fstring)
