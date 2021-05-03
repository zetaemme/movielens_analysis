# ----------------------------------------------------------------------------------------------------------------------
# Big Data project. A.A. 2020/2021
#
# Mattia Zorzan - 2021 -
# Email:  mattia(dot)zorzan_01(at)studenti(dot)univr(dot)it
# ----------------------------------------------------------------------------------------------------------------------
from utils.read import read_fvecs

import numpy as np
from matplotlib import pyplot as plt

if __name__ == "__main__":
	dataset = read_fvecs("data/siftsmall_base.fvecs")

	"""
	Dataset's mean and covariance
	
	Variables:
	mean (np.float32)
	"""
	mean = np.mean(dataset, axis=0)
	cov = np.cov(dataset, dtype=np.float32)

	"""
	Eigenvalues and Eigenvectors
	
	Variables:
	eigval (np.ndarray of np.complex128): Eigenvalues 
	eigvec (np.ndarray of np.ndarray of np.complex128): Eigenvectors
	"""
	eigval, eigvec = np.linalg.eig(cov)

	"""
	Sorting eigenvalues
	"""
	pairs = [(np.abs(eigval[i]), eigvec[:, i]) for i in range(len(eigval))]
	pairs.sort(key=lambda k: k[0], reverse=True)

	"""
	Getting the PCs at a given threshold 
	"""
	total = sum(eigval)

	var_exp = [(i/total) for i in sorted(eigval, reverse=True)]
	cum_var_exp = np.cumsum(var_exp)

	"""
	Projecting the 5/8 best PC
	"""
	w = np.hstack((
		pairs[0][1][:, np.newaxis],
		pairs[1][1][:, np.newaxis],
		pairs[2][1][:, np.newaxis],
		pairs[3][1][:, np.newaxis],
		pairs[4][1][:, np.newaxis],
	))
