import os

def get_from_dir(input_dir):
        for file in os.listdir(input_dir):
        file_name = file.split('.')
        
        yield file, file_name
