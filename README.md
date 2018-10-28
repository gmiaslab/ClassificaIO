# ClassificaIO
This repository contains ClassificaIO, a Python package that provides a graphical user interface (GUI) for machine learning algorithms from scikit-learn.

# ClassificaIO Installation Instructions
## A. INSTALLATION

### Recommended Pre-Installation Requirements
To install ClassificaIO on any platform you need:
1. A Python distribution - ClassificaIO was built using python 3.6

### Installation Instructions

#### 1. Mac or Windows
To install the current release use pip:

```bash
pip install ClassificaIO
```
Alternatively, you can install directly from github using:

```bash
pip install git+https://github.com/gmiaslab/ClassificaIO/
```


#### 2. Linux
First install the current release of tkinter and pip:

```bash
sudo apt-get install python3-tk
sudo apt-get install python3-pip
```

To install the current ClassificaIO release use pip:

```bash
pip3 install ClassificaIO
```
Alternatively, you can install directly from github using:

```bash
pip3 install git+https://github.com/gmiaslab/ClassificaIO/
```


## B. RUNNING ClassificaIO
After installation you can run:

```python
>>> from ClassificaIO import ClassificaIO
>>> ClassificaIO.gui()
```

Once run, ClassificaIO’s main window appears on your screen: 
![1_mainwindow_bmc](https://user-images.githubusercontent.com/39611565/47616405-97b37100-da92-11e8-8165-11ea470d5950.jpg)

## C. Illustrative example using the Iris dataset: 
(a) ‘Use My Own Training Data’ window with uploaded training and testing data files, selected logistic regression classifier, populated classifier parameters, and output classification results, (b) ‘Already Trained My Model’ window with uploaded logistic regression ClassificaIO trained model and testing data file, and output result.
![fig3](https://user-images.githubusercontent.com/39611565/47617792-773ee300-daa1-11e8-8c96-4d1820f7c78a.jpg)

## D. DOCUMENTATION
Documentation for ClassificaIO is provided in the manual, available online at:
* https://github.com/gmiaslab/manuals/blob/master/ClassificaIO/ClassificaIO_UserManual.pdf

The manual can also be accessed directly through the Help menu in ClassificaIO that points to the above location.

## E. LICENSING
ClassificaIO is provided under an MIT license

## F. OTHER CONTACT INFORMATION
* Contributions:
Raeuf Roushangar,
George I. Mias
* G. Mias Lab (https://georgemias.org)
* e-mail: gmiaslab@gmail.com
* twitter: @gmiaslab
