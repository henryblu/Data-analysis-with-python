#!/usr/bin/env python3

import re
# Write function red_green_blue that reads the file rgb.txt from the folder src. Remove the irrelevant first line of the file. The function should return a list of strings. Clean-up the file so that the strings in the returned list have four fields separated by a single tab character (\t). Use regular expressions to do this. The first field should be the name of the color, the second field should be the red value, the third field should be the green value, and the fourth field should be the blue value. The returned list should not contain any empty strings.

def red_green_blue(filename="src/rgb.txt"):
    ret=[]
    with open(filename, 'r') as f:
        for line in f:
            if line.startswith('!'):
                continue
            else:
                name = re.findall(r"[a-zA-Z].+\n$", line)
                srt_name = ' '.join(name).lower().strip()
                rgb = re.findall(r"\d+", line)
                ret.append( rgb[0] + '\t'  + rgb[1] + '\t'  + rgb[2] + '\t'  + srt_name)
    return ret
                    

def main():
    print(red_green_blue('rgb.txt'))

if __name__ == "__main__":
    main()
