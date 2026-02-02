import pandas as pd
import matplotlib.pyplot as plt

def plot(filename):
    df = pd.read_csv(filename, encoding='utf-8')
    df.columns = ['Title', 'Price', 'Availability', 'Rating', 'Description', 'Category', 'URL']
    df['Price'] = df['Price'].str.replace('Â£', '').astype(float)
    df['DescriptionLength'] = df['Description'].str.len()
    df['TitleLength'] = df['Title'].str.len()
    while True:

        choice = int(input('''
                1. Average Price per Category
                2. Number of Books by Rating
                3. Books in Stock vs Out of Stock
                4. Top 10 Most Expensive Books
                5. Book Count by Category (Top 10)
                6. Distribution of Book Prices (Histogram)
                7. Title Length Distribution
                8. Boxplot of Prices by Rating
                9. Number of Books Over Price Thresholds
                10. Top Categories with Most 5-Star Books
                11. Top 10 Longest Book Descriptions
                12. Category Count in Pie Chart (Top 6)
                13. Books per Rating as Line Chart
                14. Price Comparison by Rating (Bar)
                15. Exit
                Enter your choice -> '''))

        # 1️)Average Price per Category
        if choice == 1:
            avg_price_cat = df.groupby('Category')['Price'].mean().sort_values(ascending=False)
            avg_price_cat.plot(kind='bar', title='Average Price per Category',edgecolor='black', figsize=(10, 5))
            plt.ylabel('Average Price (£)')
            plt.grid()
            plt.tight_layout()
            plt.tight_layout()
            plt.show()

        # 2️)Number of Books by Rating
        elif choice == 2:
            df['Rating'].value_counts().sort_index().plot(kind='bar', edgecolor='black',title='Number of Books by Rating')
            plt.grid()
            plt.xlabel('Rating')
            plt.ylabel('Count')
            plt.tight_layout()
            plt.show()

        # 3️)Books in Stock vs Out of Stock
        elif choice == 3:
            stock_counts = df['Availability'].str.contains('In stock').value_counts()
            stock_counts = stock_counts.rename({True: 'In Stock', False: 'Out of Stock'})
            stock_counts.plot(kind='bar', title='Stock Status',edgecolor='black')
            plt.grid()
            plt.ylabel('Number of Books')
            plt.tight_layout()
            plt.show()

        # 4️)Top 10 Most Expensive Books
        elif choice == 4:
            top10_expensive = df.nlargest(10, 'Price')
            top10_expensive.plot(x='Title', y='Price', kind='barh',color= "mediumseagreen", title='Top 10 Most Expensive Books', figsize=(8, 6), edgecolor='black')
            plt.grid()
            plt.xlabel('Price (£)')
            plt.tight_layout()
            plt.show()

        # 5️)Book Count by Category (Top 10)
        elif choice == 5:
            df['Category'].value_counts().head(10).plot(kind='bar', edgecolor='black',title='Top 10 Categories by Book Count')
            plt.grid()
            plt.ylabel('Number of Books')
            plt.tight_layout()
            plt.show()

        # 6️)Distribution of Book Prices (Histogram)
        elif choice == 6:
            df['Price'].plot(kind='hist', bins=20,edgecolor='black', title='Distribution of Book Prices')
            plt.grid()
            plt.xlabel('Price (£)')
            plt.tight_layout()
            plt.show()
            
        # 7️)Title Length Distribution
        elif choice == 7:
            df['TitleLength'].plot(kind='hist', bins=20,edgecolor='black', title='Title Length Distribution')
            plt.grid()
            plt.xlabel('Title Length (characters)')
            plt.tight_layout()
            plt.show()

        # 8️)Boxplot of Prices by Rating
        elif choice == 8:
            df.boxplot(column='Price', by='Rating', grid=False)
            plt.title('Price Distribution by Rating')
            plt.suptitle('')
            plt.xlabel('Rating')
            plt.ylabel('Price (£)')
            plt.tight_layout()
            plt.show()

        # 9️)Number of Books Over Price Thresholds
        elif choice == 9:
            thresholds = [10, 20, 30, 40, 50]
            counts = [df[df['Price'] > t].shape[0] for t in thresholds]
            plt.plot(thresholds, counts, marker='o')
            plt.title('Books Over Price Thresholds')
            plt.xlabel('Price Threshold (£)')
            plt.ylabel('Number of Books')
            plt.grid(True)
            plt.tight_layout()
            plt.show()

        # )Top Categories with Most 5-Star Books
        elif choice == 10:
            top_5star = df[df['Rating'] == 'Five'].groupby('Category').size().sort_values(ascending=False).head(10)
            top_5star.plot(kind='bar', title='Top Categories with Most 5-Star Books')
            plt.ylabel('5-Star Book Count')
            plt.tight_layout()
            plt.show()

        # 1️2️)Top 10 Longest Book Descriptions
        elif choice == 11:
            longest_desc = df.nlargest(10, 'DescriptionLength')
            longest_desc.plot(x='Title', y='DescriptionLength', kind='barh', title='Top 10 Longest Descriptions', figsize=(8, 6))
            plt.xlabel('Description Length')
            plt.tight_layout()
            plt.show()

        # 1️3️)Category Count in Pie Chart (Top 6)
        elif choice == 12:
            top_categories = df['Category'].value_counts().head(6)
            top_categories.plot(kind='pie', autopct='%1.1f%%', title='Top 6 Categories')
            plt.ylabel('')
            plt.tight_layout()
            plt.show()

        # 1️4) Books per Rating as Line Chart
        elif choice == 13:
            rating_counts = df['Rating'].value_counts().sort_index()
            rating_counts.plot(kind='line', marker='o', title='Books per Rating')
            plt.xlabel('Rating')
            plt.ylabel('Number of Books')
            plt.grid(True)
            plt.tight_layout()
            plt.show()

        # 1️5 Price Comparison by Rating (Bar)
        elif choice == 14:
            avg_price_rating = df.groupby('Rating')['Price'].mean().sort_index()
            avg_price_rating.plot(kind='bar', title='Average Price by Rating')
            plt.ylabel('Average Price (£)')
            plt.tight_layout()
            plt.show()
        elif choice == 15:
            break
        else:
            print("invlad")