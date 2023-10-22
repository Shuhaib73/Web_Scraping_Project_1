# College Data Scraper and Analysis

### Project Overview

#### Description
The College Data Scraper and Analysis project is a web scraping and data analysis tool designed to gather information about colleges in the Maharashtra's Aurangabad City and provide valuable insights and data-driven analysis. It is a versatile solution that simplifies the process of collecting, analyzing, and visualizing data related to educational institutions in Maharashtra.

##### 1. Web Scraping:

        The project begins with web scraping using Python, BeautifulSoup, and Selenium to extract detailed college data from https://indcareer.com/.
        * Dynamic Web Content: Selenium was employed to navigate and interact with websites that contain dynamic content loaded through JavaScript. and it replicates user interactions with the website, such as clicking buttons, filling forms, and scrolling.
        * BeautifulSoup for Parsing: BeautifulSoup is utilized for parsing the HTML content once Selenium fetches the pages. It provides a convenient way to extract and structure data from the HTML source.

##### 2. Data Cleaning Process:

        Data cleaning is a crucial step in preparing dataset for analysis. It involves identifying and addressing various issues within the data to ensure its quality and reliability. This process includes the following steps:

        - Handling Missing Values: The first step is to identify and address missing values. Missing data can impact the accuracy of the analysis, so i decide to impute missing values with appropriate data and also i have removed few rows having missing information.
        - Formatting Inconsistencies: After conducting the web scraping process on the indcareer platform, it became evident that the dataset exhibits inconsistency in its data formatting.
        to solve this issue, I have performed few steps like - Replacing Symbols, Using Regular Expressions (Regex) for : 
        * Extracting structured information like phone numbers or email addresses.
        * Remove unwanted characters, such as punctuation or special symbols.
        * Standardize data with consistent patterns.

###### 3. Data Analysis:

        Pandas and numpy are used for data analysis, which includes exploring the cleaned data, conducting statistical analysis, and generating visualizations.

###### 4. Data Visualization:

        The project incorporates libraries like Matplotlib and Seaborn for data visualization, creating informative charts and graphs to convey insights in a clear and visual manner.

#### In conclusion, this project provided a comprehensive understanding of the higher education landscape in Maharashtra's Aurangabad through the following analyses:

       - We highlighted the top localities with the highest concentration of colleges.
       - Explored establishment years, revealing historical trends and patterns.
       - Examined affiliations, showcasing the diversity of academic networks.
       - Identified the most popular courses, aiding student and program decisions.
###### These insights serve as a valuable resource for students, policymakers, and educational stakeholders, contributing to informed decision-making and also this approach supports students in making informed decisions about their educational journeys in Aurangabad.
