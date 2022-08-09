import subprocess

def save_list_2_filename(list2save, filename):
    file = open(filename, 'w')
    file.writelines('\n'.join(list2save))
    file.writelines('\n')
    file.close()

def save_str_2_filename(str2save, filename):
    file = open(filename, 'w')
    file.write(str2save)
    file.close()

def load_from_filename(filename):
    file = open(filename, 'r')
    loaded = file.read()
    file.close()
    return loaded

def pbpaste():
    out=[]
    pbpaste = subprocess.run(
        ['pbpaste'],
        text=True,
        stdout=subprocess.PIPE,
        check=True)
    for line in pbpaste.stdout.split('\n'):
        out.append(line)
    return out

def pbcopy(str_2_pb):
    # txt_file_2_pb='/Users/stevo/Code/tools/figlet/out/temp.txt'
    # save_str_2_filename(str_2_pb, txt_file_2_pb)
    subprocess.run(
        # ['cat', txt_file_2_pb, '|', 'pbcopy'],
        # [f'cat {txt_file_2_pb} | pbcopy'],
        [f'echo {str_2_pb} | pbcopy'],
        # ['echo', str_2_pb, '|', 'pbcopy'],
        shell=True
        # text=True,
        # check=True
    )

def load_from_dir(filename):
    file = open(filename, 'r')
    loaded = file.read()
    file.close()
    return loaded


def save_to_dir(str2save, filename):
    file = open(filename, 'w')
    file.write(str2save)
    file.close()

