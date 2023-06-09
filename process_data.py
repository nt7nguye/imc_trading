import sys 
import os

# Avoid weird poermission issues that I'm too lazy to fix in Windows
os.umask(0)
def opener(path, flags):
    return os.open(path, flags, 0o777)

if __name__ == '__main__':
    print("Parsing data")
    folder_name = sys.argv[1]
    in_file_name = sys.argv[2]
    out_file_name = sys.argv[3]
    keyword = sys.argv[4]
    with open(f'./{folder_name}/{in_file_name}', 'r', opener=opener) as in_f:
        with open(f'./{folder_name}/{out_file_name}', 'w', opener=opener) as out_f:
            for line in in_f: 
                if len(line) < 6:
                    continue
                start = line.find(f"{keyword}: ")
                if start == -1: 
                    continue
                out_f.write(line[start+len(keyword) + 2:])

