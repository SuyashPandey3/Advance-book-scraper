import requests
from bs4 import BeautifulSoup
import  csv
import  sqlite3 as db
import  time

from  urllib.parse import urljoin

BASE_URL="https://books.toscrape.com/catalogue/"

def get_soup(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"html.parser")
    return  soup

def get_book_links(page_url):
    soup = get_soup(page_url)
    book_links=[]
    link=soup.select('article.product_pod h3 a')
    for article in link:
         rel_url= article.get('href')
         full_url = urljoin(BASE_URL,rel_url)
         book_links.append(full_url)
    return book_links

def parse_book_page(book_url) :
    soup = get_soup(book_url)
    title=soup.h1.text.strip()
    price =soup.select_one("p.price_color").text.strip()
    availability = soup.select_one("p.instock.availability").text.strip()
    description = soup.select_one("div#product_description")
    description_text=""
    if(description):
      description_text= description.find_next_sibling("p").text.strip()
    else:
        description_text="No Descreption"

    category = soup.select("ul.breadcrumb li")[-2].text.strip()
    raiting  = soup.select_one("p.star-rating")["class"][1]
    return {
        'Title':title,
        'Price':price,
        'Availability':availability,
        'Raiting':raiting,
        'Description':description_text,
        'Category':category,
        'URL':book_url
    }


def scrap_all_books():
    all_books_dict=[]
    limit = int(input("books form how may pages u want to scrap: "))
    print("Scrapping in progress")
    for i in range(1,limit+1):
        page_url=f"{BASE_URL}page-{i}.html"
        book_links = get_book_links(page_url)
        for desc_link in book_links:
            book_detail = parse_book_page(desc_link)
            all_books_dict.append(book_detail)
            time.sleep(0.5)
    return all_books_dict

def save_to_db(books,dbname="books.db"):
    conn= db.connect(dbname)
    cur=conn.cursor()
    qry='''create table if not exists books(
    title Text,
    price Text,
    availability Text,
    raiting Text,
    description Text,
    category Text,
    url Text
    )'''
    cur.execute(qry)
    cur.execute("delete from books")
    conn.commit()
    for book in books:
        cur.execute('''insert into books values(?,?,?,?,?,?,?)''',
                    (book['Title'],book['Price'],book['Availability'],book['Raiting'],book['Description'],book['Category'],book['URL']))
        conn.commit()
        
def csvconvertor():
    conn = db.connect('books.db') 
    cursor = conn.cursor()

   
    cursor.execute("SELECT * FROM books") 
    rows = cursor.fetchall()

    
    column_names = [description[0] for description in cursor.description]

    print(" Do not include .csv in the end, It may cause error")
    user = input("Enter your file name: ")
    with open(f'{user}.csv', 'w', newline='', encoding='utf-8') as csvfile:
        time.sleep(0.5)
        writer = csv.writer(csvfile)
        writer.writerow(column_names)  
        writer.writerows(rows)      
        time.sleep(1.5)   
        print("CSV file created successfully")

    conn.close()



    
def bookscraper():
    books=scrap_all_books()
    print("scraping done saving data in db..")
    save_to_db(books)
    print("data saved successfully...")
    
    

            






