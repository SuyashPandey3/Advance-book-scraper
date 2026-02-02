import  sqlite3 as db
import pandas as pd
import matplotlib.pyplot as plt
import BookScraper as bs
import pan as p
import matplot as plt
import time

print("Welcome to book scraping")

def main():
    while True:
        choice = int(input('''
                        1. Book scraping
                        2. CSV file creation
                        3. Run pandas quaries
                        4. Run matplotlib quaries
                        5. Exit
                        Enter your chooice ->  '''))
        if choice == 1:
            print("Make sure you are conncected with lan or wifi")
            bs.bookscraper()
        elif choice == 2:
            bs.csvconvertor() 
        elif choice == 3:
            filename = input("Enter CSV file name: ")
            p.run_queries(filename)
        elif choice == 4:
            filename = input("Enter CSV file name: ")
            plt.plot(filename)
        else: 
            break

if __name__=="__main__":
     main()
   

  

    
