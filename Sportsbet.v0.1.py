import csv
from selenium import webdriver
from bs4 import BeautifulSoup


file_soccer = 'SportsBet_Soccer'
base_url = "https://www.sportsbet.com.au"

#load browser driver
sb_driver = webdriver.Chrome()
sb_driver.get(base_url)

#parse page
new_soup = BeautifulSoup(sb_driver.page_source, 'lxml')
menu_soup = new_soup.find("a", text="Soccer")

soccer_url = menu_soup.get('href')

sb_driver.get(soccer_url)
sb_driver.refresh()

# league_soup = BeautifulSoup(sb_driver.page_source, 'lxml')
# leagues_soccer = league_soup.find("li", class_="on").find_all("a")
# test_league_soccer = leagues_soccer[0]
# for league_soccer in test_league_soccer:
#     league_url = league_soccer.a.get('href')
#     sb_driver.get(league_url)
#     sb_driver.refresh()




# sb_driver.close()
# #search for soccer link and load page
# data_soccer = menu_soup.find_all("a",onclick="return ewt.trackLink({name: 'Soccer', type:'click', link:this});")
# urls_soccer = data_soccer.find_all('a', class_="text")

# for i in urls_soccer:
#     i.text.strip() 

# # #load each soccer game
# for url_soccer in urls_soccer:
#     #load url
#     file_name_socc = (file_soccer +" " +url_soccer.text.strip() + ".csv").replace("/","-")
#     with open(file_name_socc, 'w') as f:
#         f.write("Section,Selection,Odds\n")
#     url_soccer_href = base_url+url_soccer.get('href')
#     print(url_soccer_href)
#     driver.get(url_soccer_href)
#     driver.refresh()
#     soup2 = BeautifulSoup(driver.page_source, 'lxml')
#     body_soup = soup2.find('body',class_="sport")
#     soup=body_soup.find('div',class_="main-outer").find('div',class_="main").find('div',id="game-page")   
#     #Parse betting page and extract all bets
#     # # Get Game Name
#     match_soccer = soup.find('h3', class_="name").text
#     #Find all Sections
#     sec_soccer = soup.find_all('div', class_="option option_fpw")
#     for i in sec_soccer:
#         # Get Section Name
#         sec_soccer_name = i.find('a', class_="js-state description").text
#         # #selection - 'td', class=c2 cnorder-selection
#         lines_socc = i.find_all('td', class_="c2 cnorder-selection")
#         odds_socc = i.find_all('td', class_="odds-fpw c3 cnorder-odds")
#         for x in range(len(lines_socc) -1):
#             with open(file_name_socc, 'a') as f:
#                 f.write(sec_soccer_name+","+lines_socc[x].text.strip()+","+odds_socc[x].span.text+"\n")

#pin_driver.close()
