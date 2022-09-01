# Commands list

### save_list_2_filename(list2save, filename):
    file = open(filename, 'w')
    file.writelines('\n'.join(list2save))
    file.writelines('\n')
    file.close()
### save_str_2_filename(str2save, filename):
    file = open(filename, 'w')
    file.write(str2save)
    file.close()
### save_to_dir(str2save, filename):
    file = open(filename, 'w')
    file.write(str2save)
    file.close()
### load_from_filename(filename):
    file = open(filename, 'r')
    loaded = file.read()
    file.close()
    return loaded
### load_from_dir(filename):
    file = open(filename, 'r')
    loaded = file.read()
    file.close()
    return loaded
### pbpaste():
    out=[]
    pbpaste = subprocess.run(
        ['pbpaste'],
        text=True,
        stdout=subprocess.PIPE,
        check=True)
    for line in pbpaste.stdout.split('\n'):
        out.append(line)
    return out
### pbcopy(str_2_pb):
    subprocess.run([f'echo {str_2_pb} | pbcopy'], shell=True)
### files_in_dir_ending(target_dir:str, ending:str) -> list:
    return [filename for filename in os.listdir(target_dir) if filename.endswith( '.' + ending)]
### files_in_dir(target_dir:str) -> list:
    return [filename for filename in os.listdir(target_dir) if not filename.startswith('.')]
### printl(list_2_print:list, n:int=0) -> print:
    if not n:
        n=len(list_2_print)
    for item in list_2_print[:n]: print(item)


