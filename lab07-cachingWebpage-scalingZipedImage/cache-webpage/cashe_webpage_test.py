import time
import cashe_webpage

if __name__ == '__main__':
    page = cashe_webpage.WebPage('https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BB%D1%8C%D0%B2%D1%96%D0%B2/10-%D0%B4%D0%BD%D1%96%D0%B2')
    
    content1 = page.content
    now = time.time()
    while True:
        if time.time() - now >= 7:
            break
    content2 = page.content
    while True:
        if time.time() - now >= 10:
            break
    content3 = page.content