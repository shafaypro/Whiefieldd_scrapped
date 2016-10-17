from bs4 import BeautifulSoup
import urllib.request
import json


# The below is the inner link scrapping , where we are going to scrap the inner link of the File

def Create_file():
    file_writer = open("Output.csv", "a")
    file_writer.write(
        "Name,Id,City,Zipcode,Address,Website,Email,Phone,Company Type,Postal Address, description,Twitter, Linkedin, Lognitude,Latitude")
    file_writer.close()


def Write_Data(name, id, city, zipcode, address, website, email, phone, company_type, postal_address, description,
               twitter, Linkedin, lognitude, latitude):
    name = str(name).replace(',', '')
    id = str(id).replace(',', '')
    zipcode = str(zipcode).replace(',', '')
    address = str(address).replace(',', '')
    company_type = str(company_type).replace(',', '')
    postal_address = str(postal_address).replace(',', '')
    description = str(description).encode('utf-8', errors='replace')
    description = str(description).replace("<p>", "")
    description = str(description).replace("</p>", "")
    description = str(description).replace("<div>", "")
    description = str(description).replace("</div>", "")
    description = str(description).replace("<br>", "")
    description = str(description).replace(',', '')
    file_writer = open("Output.csv", "a")
    row_insert = str(name) + "," + str(id) + "," + str(city) + "," + str(zipcode) + "," + str(address) + "," + str(website) + "," + str(email) + "," +str(phone) + "," + str(company_type) + "," + str(postal_address) + "," + str(description) + "," + str(twitter) + "," + str(Linkedin) + "," + str(lognitude) + "," + str(latitude)
    file_writer.writelines(row_insert)
    file_writer.write("\n")
    file_writer.close()


def scrap_the_website(link):
    link = link.strip()  # stripping the inner link for the extra spaces
    #print("Scrapping the inner link: ", link)
    inner_data = urllib.request.urlopen(link).read()  # opening the specified link
    inner_soup = BeautifulSoup(inner_data, "html.parser")
    contact_info = inner_soup.find('div', {'id': 'result'})  # Findin the respectable id of the program.
    json_scrapped_data = contact_info.get('data-company')
    data_load = json.loads(str(json_scrapped_data))  # This is the Json Data which has been scrapped.!
    #print("Name :", data_load["name"])
    #print("ID :", data_load["id"])
    #print("City :", data_load["city"])
    #print("ZipCode :", data_load["zipcode"])
    #print("Address :", data_load["address"])
    #print("website :", data_load["website"])
    #print("Email :", data_load["email"])
    #print("Phone  :", data_load["phone"])
    #print("Company type:", data_load["company_type"])
    #print("Postal Address :", data_load["postal_address"])
    #print("Description :", data_load["description"])
    #print("Twitter :", data_load["twitter"])
    #print("linkedin :", data_load["linkedin"])
    #print("longitude :", data_load["longitude"])
    #print("latitude :", data_load["latitude"])
    Write_Data(data_load["name"], data_load["id"], data_load["city"], data_load["zipcode"], data_load["address"], data_load["website"], data_load["email"], data_load["phone"], data_load["company_type"], data_load["postal_address"], data_load["description"], data_load["twitter"], data_load["linkedin"], data_load["longitude"], data_load["latitude"])


def scrap_test(link_to_scrap):
    data_html = urllib.request.urlopen(link_to_scrap).read()
    soup = BeautifulSoup(data_html, "html.parser")  # parsing the data in the Beautiful soup
    for link_check in soup.find_all('div', {'class', 'search-contents'}):
        print('Name :', link_check.h2.a.string)
        # print('phone_number',link_check)
        # print('City :', str(link_check.div.text).strip())
        address = BeautifulSoup(str(link_check), "html.parser")
        check = 0
        for single in address.findAll('div', {'class': 'marker'}):
            if check == 0:
                #print('city', single.text)
                check += 1
            elif check == 1:
                #print("address", single.text)
                check += 1
            elif check == 2:
                try:
                    inner_link = "https://whitfieldd.com" + single.a.get('href')
                    print("innerlink", inner_link)
                    scrap_the_website(inner_link)  # passed the inner link so that we can extract all the things.!
                    check = 0
                    print("_______________________________________________")

                except:
                    check = 0
                    continue
        check = 0
        # break  # just for the debugging purpose check if we successfully scrap the one website.


def main():
    pages = range(0, 622)
    for page in pages:
        link_to_scrap = "https://whitfieldd.com/kantoren/search?city=&page=" + str(page + 1) + "&utf8=%E2%9C%93#"  # this is the link to scrap
        print("Search link", link_to_scrap)
        # Create_file()
        scrap_test(link_to_scrap)  # calling the function and then providing the results.
        #break


if __name__ == '__main__':
    main()  # calling the main furnction.!
