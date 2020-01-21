# Electoral Zone Scraping

## Language used

For this project I used Python 3.7.4 64b, running under W10. I also used the following libraries:
-bs4
-re
-pandas
-urllib.request    

## Project overview

During my vacation, I decided to discover if there was any relationship between the average earnings and the candidate chosen for president in the past elections in my city (Porto Alegre, RS, Brazil). To complete that work I needed the specific addresses of the electoral zones, but this information was shown only in HTML. So I built a scraping script to convert the HTML information into tabular information. This project covers the scraping code I used to achieve that result.

## Source of the data

The source of the data is the website of the regional elections office (TRE-RS). Although this office covers only the state of Rio Grande do Sul, I believe the code can be used to scrap zones from cities of other states as well

## How to use

The code is set to scrap one city at a time. 

1) Got to http://capa.tre-rs.jus.br/apps/locais/ and chose the city you want to scrap from the dropdown menu
2) Copy the URL that is generated after you chose the city
3) Set this URL as the URL string in the beginning of the code
4) Run the code
5) The results will be saved in a CSV file called 'zonas_scraped.csv'

## Limitations and error handling

Since some addresses had no number, I had to hard-code some corrections (lines 41-46). These corrections works only for the city of Porto Alegre. If you are executing this code for other cities, you cand either delete the 4 lines after "## SPLIT THE NUMBER FROM THE FULL ADDRESS", or you can run the code, that will spill an error in the addresses with no number (case they do exist), and you will need to add the corrections manually.
