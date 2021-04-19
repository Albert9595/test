from celery import shared_task
from .models import JobVacancy
import requests


@shared_task
def parser_hh_city_api(city):
    area = "https://api.hh.ru/areas/113"
    response = requests.get(area)
    hh_area = response.json()
    for country in hh_area['areas']:
        if country['name'] == city:
            return country['id']


@shared_task
def parser_hh_vacans_api(vacans, city):
    area = parser_hh_city_api(city)
    for page in range(10):
        url = f"https://api.hh.ru/vacancies?text={vacans}&page={page}&area={area}"
        headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:74.0) Gecko/20100101 Firefox/74.0'}
        hh_vacansy =requests.request("GET", url, headers=headers).json()
        for vacansy in hh_vacansy['items']:
            name_vacancy = vacansy['name']
            if vacansy['salary'] == None:
                wage = "Нету"
            else:
                if vacansy['salary']['from'] == None:
                    wage = vacansy['salary']['to']
                else:
                    wage = vacansy['salary']['from']
            if vacansy['address'] == None:
                adress = vacansy['area']['name']
            elif vacansy['address']['raw'] == None:
                adress = vacansy['address']['metro']['station_name']
            else:
                adress = vacansy['address']['raw']
            url = vacansy['alternate_url']
            name_job = vacansy['employer']['name']
            description = (vacansy['snippet']['responsibility'], vacansy['snippet']['requirement'])
            skills = "Нету"
            JobVacancy.objects.create(name_vacancy=name_vacancy, wage = wage, 
                                    adress=adress, url=url, name_job=name_job, description=description, skills=skills)
        


