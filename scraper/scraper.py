import logging
import time
import requests
from bs4 import BeautifulSoup

from utils.helper import Helper


class Scraper:

    def __init__(self):
        self.url = 'https://helloworld.rs/iskustva?page='

    @staticmethod
    def scrape(page_url):
        try:
            res = requests.get(page_url)
            res.raise_for_status()

            interview = []

            soup = BeautifulSoup(res.content, 'html.parser')
            sections = soup.find_all('div', class_="p-6")

            for section in sections:

                interview_info, questions = Scraper.get_interview_data(section)

                if questions:
                    interview.append(interview_info)

            return interview
        except requests.RequestException as e:
            logging.error(f"❌Could not scrape page: {page_url}\n{e}")

    @staticmethod
    def get_interview_data(section):
        company_text = Scraper.get_company(section)
        position_text = Scraper.get_position(section)
        questions, questions_text = Scraper.get_questions(section)

        interview_info = {
            'company': company_text,
            'position': position_text,
            'questions': questions_text
        }
        return interview_info, questions

    @staticmethod
    def get_questions(section):
        questions = section.find_all('li')
        questions_text = [question.get_text(strip=True) for question in questions]

        return questions, questions_text

    @staticmethod
    def get_position(section):
        position = section.find('h3', class_="font-semibold text-xl !leading-none")
        position_text = position.get_text(strip=True) if position else None
        return position_text

    @staticmethod
    def get_company(section):
        company = section.find('a', class_="inline-block link __impression-company-link-interview pt-2")
        company_text = company.get_text(strip=True) if company else None
        return company_text

    def scrape_pages(self, start_page, end_page):

        if start_page < 0 or start_page > end_page:
            print("❌Invalid start or end page. Exiting...")
            return None

        all_interviews = []
        for page in range(start_page, (end_page * 10) + 10, 10):
            page_url = f'{self.url}{page}'

            print("⏳Scraping page: " + page_url)

            interviews_on_page = self.scrape(page_url)
            all_interviews.extend(interviews_on_page)

            time.sleep(1)

        print(f"\n📋Total questions fetched: {len(all_interviews)}")
        helper = Helper()
        helper.format_and_save(all_interviews)

        print("\n✅Data successfully saved to data/interview_data.csv\n🍀Good luck!")
