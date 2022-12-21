#!/usr/bin/env python3
import sys
def file_extensions(filename):
    '''Returns a list of filenames with no extensions and a dictionary of file extensions and file names in the file filename.'''
    with open(filename) as f:
        files = []
        extensions = {}
        for line in f:
            line = line.strip()
            if '.' in line:
                extension = line.split('.')[-1]
                if extension in extensions:
                    extensions[extension].append(line)
                else:
                    extensions[extension] = [line]
            else:
                files.append(line)
        return files, extensions


def main():
    '''Main function'''
    files, extensions = file_extensions("filenames.txt")
    print(f"{len(files)} files with no extension")
    for extension in extensions:
        print(f"{extension} {len(extensions[extension])}")    

if __name__ == "__main__":
    main()
