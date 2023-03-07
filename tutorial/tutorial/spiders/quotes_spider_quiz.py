from pathlib import Path

import scrapy
import datetime


class QuotesSpider(scrapy.Spider):
    name = "quiz"
    start_urls = [
        "https://www.proprofs.com/quiz-school/story.php?title=advanced-world-war-ii-quiz"
    ]

    def parse(self, response):
        yield {
            'title': response.css('title::text').get(),
            'tags': response.css('#breadcrumb span:nth-child(2) a span::text').getall(),
            'description': [option.replace('\n', '').strip() for option in response.css('p.question_text::text').getall()][0],
            'user': {
                "$oid": "640757ea067d6a30d72679e5"
            },
            'createdAt': datetime.datetime.now(),

        }
