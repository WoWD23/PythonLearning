#learn from lanqiao

import os
import sys

def parse_file(path):
    '''
    Parses a given text file, returning information about its Spaces, tabs, 
    and lines.

    :arg path: the path of the file to parse

    :return: tuple containing the number of Spaces, tabs and lines
    '''
    fd=open(path)
    i=0
    spaces=0
    tabs=0
    for i,line in enumerate(fd):
        spaces += line.count(' ')
        tabs += line.count('\t')
    fd.close()

    return spaces,tabs,i+1


def main(path):
    '''
    print results   

    :arg path: the path of the file to parse
    :return: True if file exists, False otherwise
    '''

    if os.path.exists(path):
        spaces, tabs, lines = parse_file(path)
        print('Spaces {}, tabs {}, lines{} '.format(spaces,tabs,lines))

        return True
    else:
        return False


if __name__=='__main__':     
#Determines whether the file is executed directly as a script
    if len(sys.argv)>1:
        main(sys.argv[1])
    else:
        sys.exit(-1)
    sys.exit(0)
