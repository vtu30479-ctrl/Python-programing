def copy_files(file_path):
    for file_path in file_path:
        if os.path.exists(file_path):
            with open(file_path,'r')as original_file:
                original_content=original_file.read()
                copy_file_path=file_path.split('.')[0]+'_copy'+file_path.split('.')[1]
                with open(copy_file_path,'w')as copy_file:
                    copy_file.write(original_content)
            print(f"Contents copied from{file_path} to { copy_file_path} successfullty")
        else:
            print(f'Error:file{file_path} not found')
import os
file_list=['file.txt']
copy_files(file_list)
