from requests import get
from bs4 import BeautifulSoup as Soup

def research_gate():
    profiles = ["https://www.researchgate.net/profile/Ike_Mowete", "https://www.researchgate.net/profile/Hisham_Muhammed", "https://www.researchgate.net/profile/Aa_Ayorinde"]
    research = []
    for profile in profiles:
        r = get(profile).text
        try:
            soup = Soup(r, features="html5lib")
        except:
            soup = Soup(r)
        try:
            research_section = soup.find("div", {"id": "research-items"}).find("div", {"class": "nova-o-stack"})
            ttype = False
        except:
            ttype = True
            research_section = soup.find("div", {"id": "research"}).find("div", {"class": "nova-o-stack"})
        if ttype:
            author = soup.find("div", {"class": "nova-l-flex--direction-row@s-up"}).find("span").text
            start = 1
        else:
            start = 0
            author = soup.find("div", {"class": "nova-o-pack--vertical-align-middle"}).find("div", {"class": "nova-e-text--spacing-xxs"}).text
        for research_item in research_section.find_all("div", {"class": "nova-o-stack__item"})[start:]:
            research_link_section = research_item.find("a", {"class": "nova-e-link"})
            research_link = research_link_section["href"]
            research_title = research_link_section.text
            try:
                abstract = research_item.find("div", {"class": "nova-v-publication-item__description"}).text
            except:
                abstract = ""
            research.append({"author": author, "research_link": research_link, "research_title": research_title, "abstract": abstract})
        print(research)
    return research
