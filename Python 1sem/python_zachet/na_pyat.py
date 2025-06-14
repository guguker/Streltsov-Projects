import os

def Pyaterka(pattern, extension):
    
    current_directory = os.getcwd()
    
    files_in_dir = os.listdir(current_directory)
    
    filtered_files = [f for f in files_in_dir if f.endswith(extension) and os.path.isfile(f)]
    

    for index, old_name in enumerate(filtered_files, start=1):

        file_name, file_ext = os.path.splitext(old_name)
        
        new_name = f"{pattern}_{index}{file_ext}"
        
        old_path = os.path.join(current_directory, old_name)
        new_path = os.path.join(current_directory, new_name)
        
        try:
            os.rename(old_path, new_path)
            print(f"Файл '{old_name}' переименован в '{new_name}'")

        except Exception as e:
            print(f"Ошибка при переименовании файла '{old_name}': {e}")


if __name__ == "__main__":

    pattern = input("Введите паттерн (как он будет называться?) для имени файла: ")
    extension = input("Введите расширение файлов (например, .txt или .jpg): ")
    
    if not extension.startswith('.'):
        extension = '.' + extension
    
    Pyaterka(pattern, extension)









































