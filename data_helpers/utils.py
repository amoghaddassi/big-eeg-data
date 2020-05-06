import os

def join_path(path1, path2, path2_is_file = False):
	"""Makes sure that there is a / between path1 and path2."""
	if path2[-1] != "/" and not path2_is_file:
		# don't want to add backslash if path2 is a filename
		path2 = path2 + "/"
	if path1[-1] != "/":
		return path1 + "/" + path2
	else:
		return path1 + path2

def listdir_better(path):
	"""Just like os.listdir, but doesn't return stupid files."""
	bad = os.listdir(path)
	good = []
	for b in bad:
		# checks all the exclusion conditions
		if b[0] == ".": continue
		good.append(b)
	return good

def subjdir_traversal(parent_dir):
	"""Generator that yields all subject directories from parent_dir.
	Say a subject dir is the first dir which contains session dirs."""
	subdirs = listdir_better(parent_dir)
	if subdirs[0][0] == "s":
		# means we have a subject dir
		yield parent_dir
	else:
		for d in subdirs:
			full_path = join_path(parent_dir, d)
			yield from subjdir_traversal(full_path)
			