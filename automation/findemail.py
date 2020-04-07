import re,pyperclip
emailRegex = re.compile(r'''(
	[a-zA-Z0-9._%+-]+
	@
	[a-zA-Z0-9.-]+
	(\.[a-zA-Z]{2,4})
	)''', re.VERBOSE)
	
text = str(pyperclip.paste())
for groups in emailRegex.findall(text):
	emails = matches.append(groups[0])
    if len(emails) > 0:
        pyperclip.copy('\n'.join(emails))
        print('Copied to clipboard:')
        print('\n'.join(emails))
    else:
        print('No email addresses found.')
  