from pathlib import Path

import scrapy
import datetime


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://www.proprofs.com/quiz-school/story.php?title=advanced-world-war-ii-quiz"
    ]

    def parse(self, response):
        for quote in response.css('li.ques_marg'):
            yield {
                'type': 'multiple-choice',
                'answer': 'C',
                'createdAt': datetime.datetime.now(),
                'question': quote.css('div.question-text::text').get(),
                'options': [option.replace('\n', '').strip() for option in quote.css('ul.answers-list li div.opt_text p::text').getall()]
            }
