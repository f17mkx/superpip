import subprocess

def paste():
    out=[]
    pbpaste = subprocess.run(
        ['pbpaste'],
        text=True,
        stdout=subprocess.PIPE,
        check=True)
    for line in pbpaste.stdout.split('\n'):
        out.append(line)
    return out

def copy(str_2_pb):
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
