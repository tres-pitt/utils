from os import listdir, path
from pathlib import Path
from shutil import copy
from sys import exit

# helper function
# case sensitive
def xtn_match(x, xtns):
	print(x)
	for xtn in xtns:
		if len(x) > len(xtn) + 1 and '.' in x:
			if x[x.find('.'):] == '.' + xtn:
				print("TRUE")
				return True
	print("FALSE")
	return False


# script to copy all ppt's to another dir at same level
# currently, only go one level deep		
if __name__ == '__main__':
	OTHER_DIR = "_lectures"
	XTNS = ['ppt', 'pptx']
	#contents = os.listdir('.')
	if OTHER_DIR not in listdir('.'):
		raise ValueError(OTHER_DIR + ' NOT FOUND')
	ppath = Path('./')
	#for f in filter(Path.is_dir, ppath.iterdir()):
	#for x in os.walk('.'):
	for x in ppath.iterdir():
		if not x.is_dir() or str(x) == OTHER_DIR:
			continue
		print(str(x))
		for y in listdir(x):
			if xtn_match(str(y), XTNS):
				if str(y) not in listdir(OTHER_DIR):
					copy(path.join(x, y), path.join(OTHER_DIR, y))

# https://stackoverflow.com/questions/973473/getting-a-list-of-all-subdirectories-in-the-current-directory