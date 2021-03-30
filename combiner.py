from os import listdir, remove
from os.path import isfile, join
from fallocate import fallocate
from offset_writer import Writer


def combiner(name, size, part_size):

    # Preallocate the file
    with open(name, "w+b") as f:

        fallocate(f, 0, size)

    writers = []
    onlyfiles = [f for f in listdir("./temp") if isfile(join("./temp", f))]
    k = 0

    onlyfiles.sort()
    
    for file in onlyfiles:

        w = Writer("./temp/" + file, name, k * (part_size + 1))
        writers.append(w)
        k = k + 1

    for w in writers:

        w.start()

    for w in writers:

        w.join()
