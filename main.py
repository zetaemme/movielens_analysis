# ----------------------------------------------------------------------------------------------------------------------
# Big Data project. A.A. 2020/2021
#
# Mattia Zorzan - 2021 -
# Email:  mattia(dot)zorzan_01(at)studenti(dot)univr(dot)it
# ----------------------------------------------------------------------------------------------------------------------
from utils.read import read_fvecs

import numpy as np

if __name__ == "__main__":
	fv = read_fvecs("data/siftsmall_base.fvecs")

	"""
	Gets the dimensions from the dataset
	
	Variables:
	N (int): Size of the dataset
	dim (int): Starting dimensionality
	"""
	N, dim = fv.shape

	"""
	Dataset's mean
	
	Variables:
	mean (np.float32)
	"""
	mean = np.mean(fv)

	"""
	Centering
	
	Variables:
	h (np.ndarray of np.float64): 1xN Matrix used for centering purposes
	centered (np.ndarray of np.float64): Centered dataset
	"""
	h = np.ones((N, 1))
	centered = np.subtract(fv, (mean * h))

	"""
	Covariance matrix
	
	Variables:
	cov (np.ndarray of np.float64)
	"""
	cov = 1/(N - 1) * np.dot(centered, centered.T)

	"""
	Eigenvalues and Eigenvectors
	
	Variables:
	eigval (np.ndarray of): Eigenvalues 
	eigvec (np.ndarray of): Eigenvectors
	"""
	eigval, eigvec = np.linalg.eig(cov)

	print(f"{type(eigval[0])}, {type(eigvec[0])}")
