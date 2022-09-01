import json

def save_list(input_list:list, filename:str) -> None:
    """saves @input_list as new lines to file
        file = open(filename, 'w')
    file.writelines('\n'.join(input_list))
    file.writelines('\n')
    file.close()
    """
    file = open(filename, 'w')
    file.writelines('\n'.join(input_list))
    file.writelines('\n')
    file.close()

def save_str(input_string:str, filename:str) -> None:
    """saves @input_string as new lines to file"""
    file = open(filename, 'w')
    file.write(input_string)
    file.close()

def save_to_dir(input_string:str, filename:str) -> None:
    """Gets and prints the spreadsheet's header columns

    @type file_loc: str
    @param file_loc: The file location of the spreadsheet
    @type print_cols: bool
    @param print_cols: A flag used to print the columns to the console
        (default is False)
    @rtype: list
    @returns: a list of strings representing the header columns
    """

    file = open(filename, 'w')
    file.write(input_string)
    file.close()

def load_file(filename:str) -> str:
    file = open(filename, 'r')
    loaded = file.read()
    file.close()
    return loaded

def save_json(content:any, filename:str) -> None:
    file = open(filename + '.json', 'w')
    json.dump(content, file, indent=2)
    file.close()

def load_json(filename:str) -> any:
    file = open(filename + '.json', 'r')
    load = json.load(file)
    file.close()
    return load
