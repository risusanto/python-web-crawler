import os

#setiap crawling website, buat folder project

def create_new_dir(directory):
    if not os.path.exists(directory):
        print('Creating new directory')
        os.makedirs(directory)

#membuat file yang berisi antrian dan antrian crawling dan antrian yang sudah selesai di crawling
def create_data_files(project_name,base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue,base_url)
    if not os.path.isfile(crawled):
        write_file(crawled,'')

#menambahkan isi file
def write_file(path,data):
    f = open(path,'w')
    f.write(data)
    f.close()

#tambah data ke file
def append_file_content(path,data):
    with open(path,'a') as file:
        file.write(data + '\n')

#hapus data di file
def delete_file_contents(path):
    with open(path,'w'):
        pass

#read a file and convert each line to set items
def file_to_set(file_name):
    results = set()
    with open(file_name,'rt') as f:
        for line in f:
            results.add(line.replace('\n',''))
    return results

#iterate through a set, each item will be a new line in the file

def set_to_file(links,file):
    delete_file_contents(file)
    for link in sorted(links):
        append_file_content(file,link)


