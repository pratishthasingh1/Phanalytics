#import dependencies
import bs4, requests

#using requests library, we can get the URL
url = 'https://questionnaire-148920.appspot.com/swe/data.html'
res = requests.get(url) 


# using html.parser we can now look for the class of 'player-salary' to use the relevant data
soup = bs4.BeautifulSoup(res.text, 'html.parser')
salaries = soup.find_all('td', class_='player-salary')


# clean up the salary data by removing $ and ,
salaries = [ salary.get_text().replace('$', '').replace(',', '') for salary in salaries]

# filter out text entries
salaries = [num for num in salaries if num.isdigit()] 

# filter out entries with missing salary data
salaries = list(filter(None, salaries)) 

# convert data to integers
salaries = [int(salary) for salary in salaries] 

# sort descending
salaries.sort(reverse=True)

# select the highest 125 salaries then find the average of the 125 highest salaries
topSalaries = salaries[:125] 
qualifyingOffer = sum(topSalaries) / 125

# documentation for formatting: 
# https://www.kite.com/python/answers/how-to-format-a-float-as-currency-in-python
qualifyingOffer = '${:,.2f}'.format(qualifyingOffer) 

print(qualifyingOffer)