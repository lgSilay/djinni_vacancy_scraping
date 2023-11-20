import scrapy
from scrapy.http import Response

from djinni.config import PARSE_URL, STACK_LIST


class VacanciesSpider(scrapy.Spider):
    name = "vacancies"
    allowed_domains = ["djinni.co"]
    start_urls = [PARSE_URL]

    def parse(self, response: Response, **kwargs):
        for vacancy in response.css(".job-list-item"):
            vacancy_detail_url = vacancy.css(".job-list-item__link::attr(href)").get()
            yield scrapy.Request(
                url=response.urljoin(vacancy_detail_url), callback=self._parse_single_vacancy
            )

        next_page = response.css('li.page-item:last-child a.page-link::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    @staticmethod
    def _parse_single_vacancy(response: Response) -> dict:
        yield {
            "title": response.css("h1::text").get().strip(),
            "stack": VacanciesSpider._vacancy_stack(response),
            # "experience": response.css(".job-additional-info--item-text::text").get(),
            "url": response.url
        }

    @staticmethod
    def _vacancy_stack(response: Response) -> list:
        current_vacancy_stack = []

        for tech in STACK_LIST:
            if tech.lower() in response.css(".mb-4").get().lower():
                current_vacancy_stack.append(tech)

        return current_vacancy_stack
