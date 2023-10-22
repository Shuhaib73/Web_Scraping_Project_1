
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import pandas as pd


def Scraper(url, pages):

    web = "https://www.indcareer.com"

    # Configuring the Chrome webdriver with options
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    # Locate the web element(State_Button) using XPath and store it in the 'check_State' variable
    check_State = driver.find_element(By.XPATH, '//a[@id="hrefstateMaharashtra"]')
    check_State.click()
    sleep(3)
    # Locate the web element(City_Button) using XPath and store it in the 'check_State' variable
    check_City = driver.find_element(By.XPATH, "//a[@id='hrefcityAurangabad']")
    check_City.click()

    # Initializing an empty list to store scraped data
    data_list = []

    try:
        for page in range(pages):       # Looping through specified number of pages for data scraping

            # Extracting the HTML source code of the current page
            page_source = driver.page_source
            soup = BeautifulSoup(page_source, 'html.parser')

            # Locating the list of colleges on the page
            list_col = soup.find('ul', class_='list-group')
            colleges = list_col.find_all('li', class_='list-group-item')

            i = 1
            for college in colleges:

                if i == 4:
                    i += 1
                    continue
                
                # Initializing the Dictionary to store college data
                College_dataset = {
                    'College_name' : [],
                    'Courses_Available' : [],
                    'Established' : [],
                    'Address' : [],
                    'City' : [],
                    'Locality' : [],
                    'Phone' : [],
                    'Fax' : [],
                    'Email' : [],
                    'Affiliations' : [],
                    'College_Web_Site' : [],
                    'indcareer_college_link' : []
                }

                # Extract relevant information from the current college element
                name = college.find('a')
                name = name.text if name else ''

                courses = college.find('ul', class_='list-unstyled')
                courses = courses.text.strip() if courses else ''
                course_names = courses.split(')')

                col_link = college.find('a')['href'] if college.find('a')['href'] else ''
                link = web + col_link if col_link else ''

                # Visit the individual college page
                driver.get(link)
                sleep(2)

                sub_page = driver.page_source
                sub_soup = BeautifulSoup(sub_page, 'html.parser')

                details = sub_soup.find('div', class_='col-sm-4 pull-right')
                details_tr = details.find_all('tr')
                
                # Extract the college's website link if available
                try:
                    college_web = driver.find_element(By.XPATH, "//a[@rel='nofollow']") 
                    college_link = college_web.get_attribute('href') 
                except NoSuchElementException:
                    college_link = 'N/A'


                lst = []

                data_dict = {
                    'Established' : '',
                    'Address' : '',
                    'City' : '',
                    'Locality' : '',
                    'Phone' : '',
                    'Fax' : '',
                    'Email' : '',
                    'Affiliations / Important Links:' : ''
                }

                for ele in details_tr:
                    lst.append(ele.text.strip())
    
                clst = [ele.replace('\n', '') for ele in lst]
                clst = clst[1:]


                for item in clst:
                    if '  ' in item:
                        key, value = item.split('  ',1)
                    else:
                        key = 'N/A'
                        value = 'N/A'

                    data_dict[key] = value

                    College_dataset['College_name'] = name
                    College_dataset['Courses_Available'] = course_names
                    College_dataset['Established'] = data_dict['Established'] if data_dict['Established'] else 'N/A'
                    College_dataset['Address'] = data_dict['Address'] if data_dict['Address'] else 'N/A'
                    College_dataset['City'] = data_dict['City'] if data_dict['City'] else 'N/A'
                    College_dataset['Locality'] = data_dict['Locality'] if data_dict['Locality'] else 'N/A'
                    College_dataset['Phone'] = data_dict['Phone'] if data_dict['Phone'] else 'N/A'
                    College_dataset['Fax'] = data_dict['Fax'] if data_dict['Fax'] else 'N/A'
                    College_dataset['Email'] = data_dict['Email'] if data_dict['Email'] else ' N/A'
                    College_dataset['Affiliations'] = data_dict['Affiliations / Important Links:'] if data_dict['Affiliations / Important Links:'] else 'N/A'
                    College_dataset['College_Web_Site'] = college_link
                    College_dataset['indcareer_college_link'] = link
                
                data_list.append(College_dataset)   # Append the college details to the data list

                i += 1
                driver.back()
                sleep(2)

            try:
                driver.find_element(By.XPATH, "//li[@class='pager-next']//a").click()   # Navigating to the next page if available
                sleep(2)
            except Exception as e:
                print(f'The page Status : {e}')


    except Exception as e:
        print(e)
    
    finally:
        df = pd.DataFrame(data_list)        # Creating a DataFrame for the collected data and save it to an Excel file
        df.to_excel('Top_Colleges_Aurangabad.xlsx', index=False)


if __name__=='__main__':
    url = "https://www.indcareer.com/find/all-colleges"
    Scraper(url, pages=12)
    

