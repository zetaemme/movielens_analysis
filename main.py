from utils.read import read_fvecs
from matplotlib import pyplot as plt


if __name__ == "__main__":
    fv = read_fvecs("data/siftsmall_base.fvecs")

    plt.title("Line by line plot of Dataset")

    for line in fv:
        plt.plot(line)

    plt.show()
