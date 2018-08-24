# -*- coding: utf-8 -*-
import scrapy
import json
import logging


class DotasSpider(scrapy.Spider):
    name = 'dotas'
    api_key = 'aeba8e0b-3e44-4862-8dd0-475c564cf483'
    allowed_domains = ['api.opendota.com']
    start_urls = ['https://api.opendota.com/api/publicMatches?mmr_descending=3000'+'&api_key='+api_key]
    # &less_than_match_id=3870095902

    def parse(self, response):
        api_key = 'aeba8e0b-3e44-4862-8dd0-475c564cf483'
        matches = json.loads(response.body.decode('utf-8'))
        for match in matches[:50]:
            yield scrapy.Request('https://api.opendota.com/api/request/'+str(match['match_id'])+'?api_key='+api_key,
                                 callback=self.parse_jobs,
                                 method='POST')

    def parse_jobs(self, response):
        api_key = 'aeba8e0b-3e44-4862-8dd0-475c564cf483'
        jobs = json.loads(response.body.decode('utf-8'))
        yield scrapy.Request('https://api.opendota.com/api/request/'+str(jobs['job']['jobId'])+'?api_key='+api_key,
                             callback=self.run_jobs)

    def run_jobs(self, response):
        api_key = 'aeba8e0b-3e44-4862-8dd0-475c564cf483'
        jobs = json.loads(response.body.decode('utf-8'))
        yield scrapy.Request('https://api.opendota.com/api/matches/'+str(jobs['data']['match_id'])+'?api_key='+api_key,
                             callback=self.parse_match)

    @staticmethod
    def parse_match(response):
        item = {}
        messages = []
        match = json.loads(response.body.decode('utf-8'))
        item['match_id'] = match['match_id']
        for message in match['chat']:
            messages.append(message)

        item['messages'] = messages
        yield item


