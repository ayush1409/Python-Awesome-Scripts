
import shelve				# to store data
import pyperclip			# to copy and paste to and from clipboard
import sys					# to read commandline

mcbshelf = shelve.open('save_clipboard_data')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
	mcbshelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
	if sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(mcbshelf.keys())))
	elif sys.argv[1] in mcbshelf:
		pyperclip.copy(mcbshelf[sys.argv[1]])

mcbshelf.close()
