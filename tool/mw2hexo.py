# coding:utf-8
import codecs

def convert_title(line):
    count = line.count('=') / 2
    line = '#' * count + ' ' + line.strip('=')
    return line


def convert_link(line):    
    try:
        idx = line.index('[')
        line = line[idx: ]
        space_idx = line.index(' ')
        if space_idx > 0:
            line = '* [' + line[space_idx + 1:] + '(' + line[1: space_idx - 1] + ')'
    except:
        pass
    
    return line


def convert(filename):
    fo = codecs.open('index.md', 'w', 'utf-8')
    f = codecs.open(filename, 'r', 'utf-8')    
    for line in f.readlines():
        line = line.strip()
        if not line:
            continue
        if line[0] == '=':
            line = convert_title(line)        
        elif line[0] in '*':
            line = convert_link(line)
        fo.write(line)
        fo.write('\n\n')


if __name__ == "__main__":
    convert('../source/favorite/index.md')    
