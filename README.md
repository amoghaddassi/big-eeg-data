# EEG meets big data

## High level

### Motivation

The goal of this project is to take advantage of the ~750gb EEG corpus found [here](https://www.isip.piconepress.com/projects/tuh_eeg/html/downloads.shtml).

Some high quality projects that inspired this:

- [Hybrid deep learning architecture on the TUH corpus](https://www.frontiersin.org/articles/10.3389/fnhum.2019.00076/full)
- [ML for seizure type classification](https://arxiv.org/abs/1902.01012)

### Architecture

To manage the complexity, there are 3 distinct parts of this repository, each detailed belowed:

- Data layer: This deals with moving data from a hard drive into python. Key abstractions are in ```data_api.py``` and ```data_helpers/```.
- Preprocessing layer: This deals with the usual preprocessing steps taken in EEG. e.g. ICA, artifact supression, etc.
- Analysis layer: This is where all the cool stuff happens. More to come.

### Dependencies

As of now:

- MNE: EEG processing library for python. Used when importing EDF files from hard drive.

### Misc.

- This project generally assumes all the structure from the TUH EEG corpus, including file hierarchy, naming conventions, etc. If something stops working for weird reasons, it might be because your files are not organized correctly.
- All testing is done in an environment where the data is on a hard disk wired to a computer. In the future, this might have to be adapted.

## Data layer

### data_api.py

This contains all the key functions for this layer. Main one is:

```data_api.yield_all_subjects(path)```: Given a path containing subject folders (using the TUH corpus file structure) at any layer of depth, yield subject objects from the path.

The code for all related data structures can be found in ```data_helpers/subject.py```
.

### Subject encapsulation


This is the broadest data abstraction used. Each subject may have recieved multiple EEG sessions; as such, a ```Subject``` object has the following attributes:

- ```Subject.sessions```: a list of session objects (more below) associated with this subject.
- ```Subject.annotations```: any specific notes about this subject (e.g. prior medical conditions) that might be relevant during analysis. THIS HAS NOT BEEN IMPLEMENTED YET.

For added flexability, subjects will not automattically parse all sessions in their path. To load ```Subject.sessions```, call ```Subject.load_subject()```.

### Session encapsulation

This has 2 primary attributes:

- ```Session.edfs```: these contain MNE raw_edf objects. No preprocessing of any kind occurs at this stage.
- ```Session.writeup```: this contains the human writeup of the eeg session by the healthcare practitioner. These are very detailed, and potentially a great source of natural language data.


