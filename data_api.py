"""Set of functions that make accessing raw EEG corpus data easier."""
from data_helpers.subject import *
from data_helpers.utils import *

DISK_PATH = "/Volumes/1TB DRIVE/tuh-eeg/edf/" # edf dir on the external drive

def yield_all_subjects(path):
	"""Generator that yields all subjects in the directory"""
	subj_gen = subjdir_traversal(path)
	for subj_path in subj_gen:
		yield Subject(subj_path)