def read_file_safety(filename):

    try:
        file=open(filename,"r")
        data=file.read()
        file.close()
        return data
    
    except FileNotFoundError:
        return "File not found."
    
print(read_file_safety("sample.txt"))    