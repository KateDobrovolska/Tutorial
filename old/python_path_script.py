from pathlib import Path
str = r"C:\Users\Kateryna_Dobrovolska"
path = Path(str)

def parse_folder(path):
    files = []
    folders = []
    for item in path.iterdir():
        if item.is_dir():
            print(f'folder - {item.name}')
            folders.append(item.name)
        elif item.is_file():
            print(f'file - {item.name}')
            files.append(item.name)
            
    return files, folders

parse_folder(path)