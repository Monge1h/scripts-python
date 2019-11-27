import re
import sys
import os

def add_underscore(path):
    """
    Crea una copia de los archivos sustituyendo los espacios que se encuentren
    entre ` ` por _

    Parameters:
        path (str): string completo del path en el que se encuentran los archivos
    
    Example:
        $ python queryHelper.py C:/User/querys/
    """
    entreComillas = r"\s+(?=(?:(?:[^`]*`){2})*[^`]*`[^`]*$)"
    try:
        for filename in os.listdir(path):
            current_file = os.path.splitext(filename)[0]

            with open(f"{path}/{filename}",'r') as reader:
                texto = reader.readlines()
            with open(f'{path}/{current_file}-copy.sql','w') as writer:
                for text in texto:
                    newline = re.sub(entreComillas,'_',text).lower()
                    writer.writelines(newline)
    except expression as identifier:
        pass
   

if __name__ == '__main__':
    
    if len(sys.argv) == 1:
        print('Tienes que poner el path del folder donde estan los sql')
    else:
        path = sys.argv[1]
        add_underscore(path)