# -*- coding: utf-8 -*-
import scrapy
import re


class YncSpider(scrapy.Spider):
    name = 'ync'
    allowed_domains = ['theync.com']
    start_urls = ['http://theync.com/most-recent/']

    def parse(self, response):
        blocks = response.xpath('//main[@id="content"]//div[@class="content-block"]/div[contains(@class, "item-normal")]')
        if blocks:
            for block in blocks:
                if block.xpath('.//span[@class="border-gold"]/text()').extract_first() != 'UNDERGROUND' and block.xpath('.//span[@class="user"]/a/@target').extract_first() != '_blank':
                    url = block.xpath('.//div[@class="inner-block"]/a/@href').extract_first()
                    yield scrapy.Request(response.urljoin(url), callback=self.parse_page)

        next_page = response.xpath('//div[@id="pagination"]//a[contains(text(), "NEXT")]/@href').extract_first()
        if next_page is not None:
            yield scrapy.Request(response.urljoin(next_page))

    @staticmethod
    def parse_page(response):

        item = {}

        main_block = response.xpath('//div[@id="main-item"]')

        title = main_block.xpath('//div[contains(@class, "title-video")]/h2/text()[normalize-space()]').extract_first()
        date = main_block.xpath('//span[@class="date"]/text()').extract_first()
        id = main_block.xpath('//div[@class="ratingStars"]/@data-id').extract_first()
        rating = main_block.xpath('//div[@class="rated"]//span[@class="count"]/text()').extract_first()
        views = main_block.xpath('//div[@class="views-block"]//span[@class="count"]/text()').extract_first()
        category = main_block.xpath('//div[@class="path-item"]/a[@class="path-link"]/text()').extract_first()

        video_block = main_block.xpath('//div[contains(@class, "stage-video")]//script[contains(text(), "thisPlayer.setup")]').extract_first()

        image_block = main_block.xpath('//div[contains(@class, "stage-video")]/div[@id="galleryImages"]').extract_first()

        if image_block:
            return
        else:
            file_src = re.search('file: "(.*?)"', video_block).groups()
            if file_src[0]:
                item['file_src'] = file_src[0]
            image_src = re.search('image: "(.*?)"', video_block).groups()
            if image_src[0]:
                item['image_src'] = image_src[0]

            if title:
                item['title'] = title.strip()
            if date:
                item['date'] = date.strip()
            if id:
                item['id'] = id.strip()
            if rating:
                item['rating'] = rating.strip()
            if views:
                item['views'] = views.strip()
            if category:
                item['category'] = category.strip()

            ync_url = response.url
            item['url'] = ync_url

            yield item
