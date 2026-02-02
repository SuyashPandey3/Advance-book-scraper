import pandas as pd
import time

def run_queries(filename):
    try:
        df = pd.read_csv(filename, encoding='utf-8')
        df.columns = ['Title', 'Price', 'Availability', 'Rating', 'Description', 'Category', 'URL']
        df['Price'] = df['Price'].str.replace('Â£', '').astype(float)
        df['is_expensive'] = df['Price'] > 40
        df['DescriptionLength'] = df['Description'].str.len()
        
        decide = int(input('''
                       1. Do you want onw quary at a time
                       2. Do you want all at a time
                       Enter your choice -> '''))
        if decide == 1:
                while True:
                        choice = int(input('''
                                1.  Convert Price from string to float
                                2. Top 5 most expensive books
                                3. Average price of all books
                                4. Count of books by star rating
                                5. Number of books in each category
                                6. Books with "Python" in the title
                                7. Books currently in stock
                                8. Out-of-stock books
                                9. Count of books missing a description
                                10. Most common book rating
                                11. Number of unique categories
                                12. List all unique categories
                                13. Sort all books alphabetically by title
                                14. Books with the longest descriptions
                                15.  Cheapest book in each category
                                16. Top 3 most expensive books per category
                                17. Books with title length > 50 characters
                                18. Add a column for "is_expensive" (price > £40)
                                19. Count of expensive books by category
                                20.  Save filtered DataFrame of in-stock & expensive books
                                21. Exit
                                Enter your choice: '''))

                        if choice == 1:
                                # df['Price'] = df['Price'].str.replace('Â£', '').astype(float)
                                print("Converted successfully")
                        elif choice == 2:
                                time.sleep(0.5)
                                print("\nTop 5 Expensive Books:")
                                print(df.nlargest(5, 'Price')[['Title', 'Price']])
                                time.sleep(0.5)
                        elif choice == 3:
                                time.sleep(0.5)
                                print("\nAverage Price of All Books:")
                                print(round(df['Price'].mean(), 2))
                                time.sleep(0.5)
                        elif choice == 4:
                                time.sleep(0.5)
                                print("\nRating Counts:")
                                print(df['Rating'].value_counts())
                                time.sleep(0.5)
                        elif choice == 5:
                                time.sleep(0.5)
                                print("\nCategory Counts:")
                                print(df['Category'].value_counts())
                                time.sleep(0.5)
                        elif choice == 6:
                                time.sleep(0.5)
                                print("\nBooks with 'Python' in Title:")
                                print(df[df['Title'].str.contains('Python', case=False)]['Title'])
                                time.sleep(0.5)
                        elif choice == 7:
                                time.sleep(0.5)
                                print("\nIn-Stock Books Count:")
                                print(df[df['Availability'].str.contains('In stock')].shape[0])
                                time.sleep(0.5)
                        elif choice == 8:
                                time.sleep(0.5)
                                print("\nOut-of-Stock Books Count:")
                                print(df[~df['Availability'].str.contains('In stock')].shape[0])
                                time.sleep(0.5)

                        elif choice == 9: 
                                time.sleep(0.5)
                                print("\nMissing Descriptions Count:")
                                missing_desc = df['Description'].isna().sum() + (df['Description'].str.strip() == '').sum()
                                print(missing_desc)
                                time.sleep(0.5)
                        elif choice == 10:
                                time.sleep(0.5)
                                print("\nMost Common Rating:")
                                print(df['Rating'].mode()[0])
                                time.sleep(0.5)
                        elif choice == 11:
                                time.sleep(0.5)
                                print("\nUnique Categories Count:")
                                print(df['Category'].nunique())
                                time.sleep(0.5)
                        elif choice == 12:
                                time.sleep(0.5)
                                print("\nList of Unique Categories:")
                                print(df['Category'].unique())
                                time.sleep(0.5)
                        elif choice == 13:
                                time.sleep(0.5)
                                print("\nBooks Sorted Alphabetically by Title:")
                                print(df.sort_values('Title')[['Title']])
                                time.sleep(0.5)
                        elif choice == 14:
                                time.sleep(0.5)
                                df['DescriptionLength'] = df['Description'].str.len()
                                longest_descriptions = df.nlargest(5, 'DescriptionLength')[['Title', 'DescriptionLength']]
                                print("\n` Top 5 Books with the Longest Descriptions:")
                                print(longest_descriptions)
                                time.sleep(0.5)
                        elif choice == 15:
                                time.sleep(0.5)
                                print("\nCheapest Book in Each Category:")
                                cheapest = df.loc[df.groupby('Category')['Price'].idxmin()]
                                print(cheapest[['Category', 'Title', 'Price']])
                                time.sleep(0.5)
                        elif choice == 16:
                                time.sleep(0.5)
                                print("\nTop 3 Expensive Books per Category:")
                                top3 = df.sort_values('Price', ascending=False).groupby('Category').head(3)
                                print(top3[['Category', 'Title', 'Price']])
                                time.sleep(0.5)
                        elif choice == 17:
                                time.sleep(0.5)
                                print("\nBooks with Title Length > 50 Characters:")
                                print(df[df['Title'].str.len() > 50][['Title']])
                                time.sleep(0.5)
                        elif choice == 18:
                                time.sleep(0.5)
                                df['is_expensive'] = df['Price'] > 40
                                print("\n 'is_expensive' Column Added:")
                                print(df[['Title', 'Price', 'is_expensive']].head())
                                time.sleep(0.5)
                        elif choice == 19:
                                time.sleep(0.5)
                                print("\nExpensive Books Count by Category:")
                                print(df[df['is_expensive']].groupby('Category').size())
                                time.sleep(0.5)
                        elif choice == 20:
                                time.sleep(0.5)
                                print("\nSaving Filtered DataFrame...")
                                filtered = df[df['is_expensive'] & df['Availability'].str.contains('In stock')]
                                filtered.to_csv('filtered_books.csv', index=False)
                                print(" Filtered DataFrame saved as 'filtered_books.csv'")
                                time.sleep(0.5)

                        else:
                             break
                         
                         
        elif decide == 2:
                
                        
                                # df['Price'] = df['Price'].str.replace('Â£', '').astype(float)
                        
                                print("\nTop 5 Expensive Books:")
                                print(df.nlargest(5, 'Price')[['Title', 'Price']])
                                print('-'*30)
                        
                                print("\nAverage Price of All Books:")
                                print(round(df['Price'].mean(), 2))
                                print('-'*30)
                        
                                print("\nRating Counts:")
                                print(df['Rating'].value_counts())
                                print('-'*30)
                        
                                print("\nCategory Counts:")
                                print(df['Category'].value_counts())
                                print('-'*30)
                        
                                print("\nBooks with 'Python' in Title:")
                                print(df[df['Title'].str.contains('Python', case=False)]['Title'])
                                print('-'*30)
                       
                                print("\nIn-Stock Books Count:")
                                print(df[df['Availability'].str.contains('In stock')].shape[0])
                                print('-'*30)
                        
                                print("\nOut-of-Stock Books Count:")
                                print(df[~df['Availability'].str.contains('In stock')].shape[0])
                                print('-'*30)

                        
                                print("\nMissing Descriptions Count:")
                                missing_desc = df['Description'].isna().sum() + (df['Description'].str.strip() == '').sum()
                                print(missing_desc)
                                print('-'*30)
                        
                                print("\nMost Common Rating:")
                                print(df['Rating'].mode()[0])
                                print('-'*30)
                        
                                print("\nUnique Categories Count:")
                                print(df['Category'].nunique())
                                print('-'*30)
                        
                                print("\nList of Unique Categories:")
                                print(df['Category'].unique())
                                print('-'*30)
                        
                                print("\nBooks Sorted Alphabetically by Title:")
                                print(df.sort_values('Title')[['Title']])
                                print('-'*30)
                        
                                print("\nBooks with Longest Descriptions:")
                                print(df.nlargest(5, 'DescriptionLength')[['Title', 'DescriptionLength']])
                                print('-'*30)
                                
                                df['DescriptionLength'] = df['Description'].str.len()
                                longest_descriptions = df.nlargest(5, 'DescriptionLength')[['Title', 'DescriptionLength']]
                                print("\nTop 5 Books with the Longest Descriptions:")
                                print(longest_descriptions)
                                print('-'*30)
                        
                                print("\nCheapest Book in Each Category:")
                                cheapest = df.loc[df.groupby('Category')['Price'].idxmin()]
                                print(cheapest[['Category', 'Title', 'Price']])
                                print('-'*30)
                        
                                print("\nTop 3 Expensive Books per Category:")
                                top3 = df.sort_values('Price', ascending=False).groupby('Category').head(3)
                                print(top3[['Category', 'Title', 'Price']])
                                print('-'*30)
                        
                                print("\nBooks with Title Length > 50 Characters:")
                                print(df[df['Title'].str.len() > 50][['Title']])
                                print('-'*30)
                        
                                df['is_expensive'] = df['Price'] > 40
                                print("\n 'is_expensive' Column Added:")
                                print(df[['Title', 'Price', 'is_expensive']].head())
                                print('-'*30)
                        
                                print("\nExpensive Books Count by Category:")
                                print(df[df['is_expensive']].groupby('Category').size())
                                print('-'*30)
                                
                                ask = input("Do your want filtered datafram y/n: ").lower()
                                if ask == "y":       
                                        print("\nSaving Filtered DataFrame...")
                                        filtered = df[df['is_expensive'] & df['Availability'].str.contains('In stock')]
                                        filtered.to_csv('filtered_books.csv', index=False)
                                        print(" Filtered DataFrame saved as 'filtered_books")
                                else:
                                        print("NO filtered CSV file created")
                                     
                        
    except FileNotFoundError:
        print(f" File '{filename}' not found. Please check the name and try again.")
    except Exception as e:
        print(f" Error occurred: {e}")
        
        