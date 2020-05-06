"""Contains all the datastructures to encapsulate a patient in the TUH EEG corpus."""
import os
import mne
from data_helpers.utils import *

class Subject:
	def __init__(self, path, eager_load = False):
		"""path (str) is the folder containing all of the subjects eeg sessions.
		eager_load: if true, will load the sessions objects on init"""
		self.path = path
		if eager_load:
			self.load_subject

	def load_subject(self):
		"""This will create all the sessions for a subject, don't do this 
		automatically when working with bigger datasets."""
		self.sessions = []
		# unpacks the subject directory and creates session objects
		subdirs = listdir_better(self.path)
		for d in subdirs:
			full_path = join_path(self.path, d)
			sess = Session(full_path)
			self.sessions.append(sess)

class Session:
	def __init__(self, path):
		"""path (str) is the folder containing the .edf and .txt files."""
		# sets the date of the session from the path name.
		self.date = self.get_date(path)
		self.edfs = []
		# unpacks the session directory
		subdirs = listdir_better(path)
		for d in subdirs:
			full_path = join_path(path, d, True)
			# get the file type so I know what to do with it
			file_type = d.split(".")[-1]
			if file_type == "txt":
				# this is the writeup file, 1 per directory ideally
				self.writeup = self.parse_writeup(full_path)
			elif file_type == "edf":
				# makes an mne raw object from this
				mne_obj = mne.io.read_raw_edf(full_path)
				self.edfs.append(mne_obj)
			# for now am not collecting any other files

	def get_date(self, path):
		"""Given a path (that's passed into init), returns the date contained
		in the last folder's name."""
		sess_name = path.split("/")[-2]
		date_list = sess_name.split("_")[1:]
		return "-".join(date_list)

	def parse_writeup(self, full_path):
		"""Deals with the text file writeup in the session folder."""
		text = open(full_path).read()
		return text # can this much more complicated
		