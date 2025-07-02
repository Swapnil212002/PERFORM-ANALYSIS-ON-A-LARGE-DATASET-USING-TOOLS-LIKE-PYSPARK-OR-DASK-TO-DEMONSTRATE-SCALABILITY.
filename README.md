# PERFORM-ANALYSIS-ON-A-LARGE-DATASET-USING-TOOLS-LIKE-PYSPARK-OR-DASK-TO-DEMONSTRATE-SCALABILITY.

COMPANY : CODTECH IT SOLUTIONS

NAME : SWAPNIL SOMNATH JAGDALE

INTERN ID : CT04DF1586

DURATION : 4 WEEKS

MENTOR : NEELA SANTOSH

## Description : 

This project demonstrates the use of Dask, a parallel computing library in Python, to analyze a large dataset from Netflix. The dataset includes metadata about TV shows and movies available on Netflix, such as titles, genres, release years, countries, and the date they were added to the platform. The analysis not only showcases how to process large datasets efficiently using Dask, but also derives meaningful business insights and visualizations from the content data.

Tools and Technologies Used
Dask: Used for scalable, parallel computation on large datasets. Unlike Pandas, Dask handles out-of-core computation and works efficiently on datasets larger than memory.

Matplotlib & Seaborn: Libraries used to create visualizations like bar charts and line graphs.

Jupyter Notebook / Python Script: Used for interactive analysis and reproducibility.

Data Loading and Cleaning
The dataset was in CSV format with semicolon (;) delimiters and quoted fields. It was read using Dask’s read_csv function with appropriate parameters (sep=';' and quotechar='"').

Before performing any analysis, missing values in key columns like type (Movie/TV Show) were removed. Dask’s lazy evaluation model delayed computation until explicitly requested via .compute().

1. Null Values Analysis
The first step was identifying missing values in each column. This helped understand the data quality and determine which columns needed cleaning or could be used reliably in further analysis.

2. Content Type Distribution
The dataset was grouped by type to compare how many entries were classified as Movies and how many as TV Shows. The result was visualized using a bar chart, revealing that movies made up a significantly larger portion of Netflix's content catalog compared to TV shows.

3. Top Content-Producing Countries
Netflix content was further analyzed based on the country field. By using Dask's value_counts() and selecting the top 10 results, we identified the most frequent countries contributing to Netflix's content library. Countries like the United States, India, and United Kingdom appeared as major content producers. A horizontal bar chart made the comparison clear and easy to interpret.

4. Content Added per Year
The date_added column, which represents when a show or movie was added to Netflix, was converted to datetime format. From this, the year was extracted, and the number of shows/movies added each year was calculated. This was visualized using a line plot, showing trends in Netflix's content growth over the years. Peaks in specific years may correspond to strategic content expansion or global events like the COVID-19 pandemic that boosted digital viewership.

5. Genre Frequency Analysis
Netflix titles are associated with multiple genres in a single string. These were split and “exploded” into separate rows for accurate genre counting. The most common genres such as Dramas, Comedies, International TV Shows, and Documentaries were identified. A bar chart was used to visualize the top 10 genres, giving insight into the platform’s content strategy and audience preferences.

Scalability and Dask’s Role
Unlike Pandas, Dask enables processing in chunks, which is ideal for large files or low-memory environments. Each .compute() operation executes the graph of tasks in parallel, providing high efficiency. This scalability makes Dask a preferred tool in big data analysis and industry pipelines.

Conclusion
This project effectively demonstrates how to use Dask for scalable data analysis and derive insights from a real-world dataset. It provides visual summaries that can assist stakeholders in understanding Netflix’s content distribution and strategy. The project is modular and can be extended with further analyses such as actor frequency, duration analysis, or time-to-market trends.


## OUTPUT : 



![Image](https://github.com/user-attachments/assets/0143491b-14dd-4c23-86cd-9e5b8367885a)
![Image](https://github.com/user-attachments/assets/20f983b8-c629-495f-ac53-e0c031c32da7)
![Image](https://github.com/user-attachments/assets/9241dab0-733d-4870-8306-0c86be767ac4)
![Image](https://github.com/user-attachments/assets/59a16472-1375-4345-bb34-a8b2e5aa318a)
