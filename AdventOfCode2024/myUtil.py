import os


def openFile(fileName: str = "") -> list[str]:

    workingDirectory = os.path.dirname(os.path.abspath(__file__))

    if fileName == "":
        return open(os.path.join(workingDirectory, "test.txt")).readlines()
    else:
        return open(os.path.join(workingDirectory, fileName)).readlines()
