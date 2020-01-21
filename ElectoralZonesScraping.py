from bs4 import BeautifulSoup
import re
import pandas as pd
import urllib.request    

## DOWNLOAD HTML
URL = "http://capa.tre-rs.jus.br/apps/locais/index.php?acao=municipio&localidade=7994&nome=PORTO%20ALEGRE"
urllib.request.urlretrieve(URL, "Locais.html")
soup = BeautifulSoup(open('Locais.html'), "html.parser")

## START OF SCRAPING ## IMPORT REGIONS FROM HTML

# Define the header
columns = ['Zona', 'Local', 'Endereco', 'Secoes','Eleitores']

#Create the dataframe
df_zonas = pd.DataFrame(columns=columns)
i = 0
#Navigate through the table 
for table in soup.select('table'):
    i += 1
    # For each header cell (<th>) find the zone (region) number
    for th in table.find_all('th')[1:]:
        Zona = th.text
        Zona = re.findall('\d+', Zona)
        Zona = Zona[0]
        print('Region: '+str(Zona))
    # For each table row (<tr>) find all dividers (<td>)
    for tr in table.find_all('tr')[2:]:
        tds = tr.find_all('td')
        j = 0
        # The Local name information will be in the 1st one, 
        # the address will be in the 2nd, 
        # sections info in the 3rd and total number of voters in the 4th
        for td in tds:
            j += 1
            if j == 1:
                Local = td.text
            if j == 2:
                EnderecoFull = td.text
                ## CORRECT ADDRESS THAT ARE NOT COMPLYING WITH THE STANDARD
                EnderecoFull = EnderecoFull.replace("S/N", "1")
                EnderecoFull = EnderecoFull.replace("- ESQUINA", " ,1")
                EnderecoFull = EnderecoFull.replace("PARQUE LAVOURA", " ,1")
                EnderecoFull = EnderecoFull.replace("RUA FERNANDO PESSOAVILA NOVA", "RUA FERNANDO PESSOA ,1")
                EnderecoFull = EnderecoFull.replace("RUA PADRE HENRIQUE PAUQUETHÍPICA", "RUA PADRE HENRIQUE PAUQUET,1")
                ## SPLIT THE NUMBER FROM THE FULL ADDRESS
                NumEnd = re.findall('\d+', EnderecoFull)
                NumEnd = NumEnd[0]
                Logradouro, Num, Bairro = EnderecoFull.partition(',')
                Endereco = NumEnd+', '+Logradouro+' - Porto Alegre, RS'
            if j == 3:
                Secoes= td.text
            if j == 4:
                Eleitores = td.text
                
        # Append all the information as a line into the DataFrame
        df_zonas = df_zonas.append({'Zona' :Zona, 'Local' :Local, 'Endereco' :Endereco, 'Secoes' : Secoes, 'Eleitores' : Eleitores} , ignore_index=True)
## END OF SCRAPPING

df_zonas.to_csv('zonas_scraped.csv')
