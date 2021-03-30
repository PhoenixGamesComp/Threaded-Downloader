import requests
import sys
import validators
from partial_download import Downloader
from combiner import combiner


def arg_handler():

    if len(sys.argv) == 1:

        print("Type python3 main.py --help for usage list.")
        sys.exit(0)

    if len(sys.argv) == 2:

        if sys.argv[1] == "--help":

            print("Usage:")
            print("\t -n [number_of_threads] [url]")
            sys.exit(0)

        else:

            print("Type python3 main.py --help for usage list.")
            sys.exit(0)
    
    if len(sys.argv) == 4:

        if sys.argv[1] != "-n":

            print("Type python3 main.py --help for usage list.")
            sys.exit(0)

        valid = validators.url(sys.argv[3])

        if valid is True:
            
            return [int(sys.argv[2]), sys.argv[3]]
        
        else:

            print("Invalid url")
            sys.exit(0)

    print("Type python3 main.py --help for usage list.")
    sys.exit(0)


if __name__ == "__main__":

    # Handle the console input
    number_of_threads, url = arg_handler()

    # Get total size of the file
    with requests.get(url, stream=True) as r:

        size = int(r.headers['content-length'])

    # Get part size
    part_size = int(size / number_of_threads)
    downloaders = []

    # Create n download threads
    for _ in range(number_of_threads):

        d = Downloader(url, part_size, _ * (part_size + 1), _)
        d.start()

        downloaders.append(d)
    
    for d in downloaders:

        d.join()

    # Combine the part files into one using n writers
    combiner(str(url.rsplit('/', 1)[-1]), size, part_size)
