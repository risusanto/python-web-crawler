import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

project_name = ''
homepage = ''
domain_name = ''
queue_file = ''
crawled_file = ''

NUMBER_OF_THREADS = 8
queue = Queue()

# buat threads
def create_worker():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

#do the next job
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name,url)
        queue.task_done()

#setiap queue adalah job baru
def create_jobs():
    for link in file_to_set((queue_file)):
        queue.put(link)
    queue.join()
    crawl()

#cek apakah ada item di queue
def crawl():
    queued_links = file_to_set(queue_file)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' Link in queue')
        create_jobs()

user_input = input('Input url to crawl: ')

project_name = get_domain_name(user_input)
homepage = user_input
domain_name = get_domain_name(homepage)
queue_file = project_name + '/queue.txt'
crawled_file = project_name + '/crawled.txt'

Spider(project_name, homepage, domain_name)

create_worker()
crawl()