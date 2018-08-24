# -*- coding: utf-8 -*-
import scrapy


class SotruSpider(scrapy.Spider):
    name = 'sotru'
    allowed_domains = ['pravda-sotrudnikov.ru']
    start_urls = [
        'http://pravda-sotrudnikov.ru/catalog/uslugi-naseleniju/it-kompanii-razrabotka-hosting',
        'http://pravda-sotrudnikov.ru/catalog/uslugi-naseleniju/avtoservisy-i-avtoshkoly',
        'http://pravda-sotrudnikov.ru/catalog/uslugi-naseleniju/gosudarstvennaya-sluzhba',
        'http://pravda-sotrudnikov.ru/catalog/uslugi-naseleniju/dizajn-i-kreativnaja-reklama',
        'http://pravda-sotrudnikov.ru/catalog/uslugi-naseleniju/izdatelstva-pressa-internet-portaly',
        'http://pravda-sotrudnikov.ru/catalog/uslugi-naseleniju/inzhenernoe-obsluzhivanie',
        'http://pravda-sotrudnikov.ru/catalog/uslugi-naseleniju/kadrovye-agentstva',
        'http://pravda-sotrudnikov.ru/catalog/uslugi-naseleniju/kafe-i-restorany',
        'http://pravda-sotrudnikov.ru/catalog/uslugi-naseleniju/kluby-gostinicy-kinoteatry',
        'http://pravda-sotrudnikov.ru/catalog/uslugi-naseleniju/krasota-i-zdorovie',
        'http://pravda-sotrudnikov.ru/catalog/uslugi-naseleniju/kultura-i-iskusstvo',
        'http://pravda-sotrudnikov.ru/catalog/uslugi-naseleniju/logistika-i-transport',
        'http://pravda-sotrudnikov.ru/catalog/uslugi-naseleniju/marketing-i-reklama',
        'http://pravda-sotrudnikov.ru/catalog/uslugi-naseleniju/medicinskie-uslugi-i-ozdorovlenie',
        'http://pravda-sotrudnikov.ru/catalog/uslugi-naseleniju/melkie-bytovye-uslugi-i-zhkh',
        'http://pravda-sotrudnikov.ru/catalog/uslugi-naseleniju/nauka-i-fizika',
        'http://pravda-sotrudnikov.ru/catalog/uslugi-naseleniju/obschestvennye-organizacii',
        'http://pravda-sotrudnikov.ru/catalog/uslugi-naseleniju/ohrana-i-bezopasnost',
        'http://pravda-sotrudnikov.ru/catalog/uslugi-naseleniju/provajdery-i-svjaz',
        'http://pravda-sotrudnikov.ru/catalog/uslugi-naseleniju/prodazha-zemel-i-nedvizhimosti',
        'http://pravda-sotrudnikov.ru/catalog/uslugi-naseleniju/salony-optiki',
        'http://pravda-sotrudnikov.ru/catalog/uslugi-naseleniju/stroitelstvo-i-remont',
        'http://pravda-sotrudnikov.ru/catalog/uslugi-naseleniju/tele-i-radiokompanii',
        'http://pravda-sotrudnikov.ru/catalog/uslugi-naseleniju/treningi-i-obrazovanie',
        'http://pravda-sotrudnikov.ru/catalog/uslugi-naseleniju/turisticheskie-i-aviakompanii',
        'http://pravda-sotrudnikov.ru/catalog/uslugi-naseleniju/uslugi-dlya-biznesa',
        'http://pravda-sotrudnikov.ru/catalog/uslugi-naseleniju/uslugi-dlya-naseleniya',
        'http://pravda-sotrudnikov.ru/catalog/uslugi-naseleniju/finansy-banki-strahovanie',
        'http://pravda-sotrudnikov.ru/catalog/uslugi-naseleniju/jekologija-i-utilizacija',
        'http://pravda-sotrudnikov.ru/catalog/uslugi-naseleniju/juridicheskie-uslugi-i-advokaty',
        'http://pravda-sotrudnikov.ru/catalog/optovaja-i-roznichnaja-torgovlja/avtomobili-i-zapchasti',
        'http://pravda-sotrudnikov.ru/catalog/optovaja-i-roznichnaja-torgovlja/bytovaja-tehnika-i-mobilnaja-svjaz',
        'http://pravda-sotrudnikov.ru/catalog/optovaja-i-roznichnaja-torgovlja/igrushki-i-podarki',
        'http://pravda-sotrudnikov.ru/catalog/optovaja-i-roznichnaja-torgovlja/internet-magaziny',
        'http://pravda-sotrudnikov.ru/catalog/optovaja-i-roznichnaja-torgovlja/kanceljarskie-tovary',
        'http://pravda-sotrudnikov.ru/catalog/optovaja-i-roznichnaja-torgovlja/knigi-cd',
        'http://pravda-sotrudnikov.ru/catalog/optovaja-i-roznichnaja-torgovlja/komputery-po',
        'http://pravda-sotrudnikov.ru/catalog/optovaja-i-roznichnaja-torgovlja/kosmetika-i-parfumeriya',
        'http://pravda-sotrudnikov.ru/catalog/optovaja-i-roznichnaja-torgovlja/mebel-i-predmety-interera',
        'http://pravda-sotrudnikov.ru/catalog/optovaja-i-roznichnaja-torgovlja/nedvizhimost-prodazha-i-arenda',
        'http://pravda-sotrudnikov.ru/catalog/optovaja-i-roznichnaja-torgovlja/oborudovanie-dlya-predpriyatiy',
        'http://pravda-sotrudnikov.ru/catalog/optovaja-i-roznichnaja-torgovlja/sportivnie-tovary',
        'http://pravda-sotrudnikov.ru/catalog/optovaja-i-roznichnaja-torgovlja/supermarkety-i-riteil',
        'http://pravda-sotrudnikov.ru/catalog/optovaja-i-roznichnaja-torgovlja/floristika',
        'http://pravda-sotrudnikov.ru/catalog/optovaja-i-roznichnaja-torgovlja/hozjajstvennye-i-strojmaterialy',
        'http://pravda-sotrudnikov.ru/catalog/optovaja-i-roznichnaja-torgovlja/uvelirnye-izdeliya',
        'http://pravda-sotrudnikov.ru/catalog/proizvoditeli-i-postavshhiki/bytovaja-tehnika-i-jelektronika',
        'http://pravda-sotrudnikov.ru/catalog/proizvoditeli-i-postavshhiki/lesnaja-promyshlennost',
        'http://pravda-sotrudnikov.ru/catalog/proizvoditeli-i-postavshhiki/mashinostroenie-i-oborudovanie',
        'http://pravda-sotrudnikov.ru/catalog/proizvoditeli-i-postavshhiki/metallurgicheskie-kompanii',
        'http://pravda-sotrudnikov.ru/catalog/proizvoditeli-i-postavshhiki/neftegazovyj-kompleks',
        'http://pravda-sotrudnikov.ru/catalog/proizvoditeli-i-postavshhiki/odezhda-i-obuv',
        'http://pravda-sotrudnikov.ru/catalog/proizvoditeli-i-postavshhiki/produkty-pitaniya',
        'http://pravda-sotrudnikov.ru/catalog/proizvoditeli-i-postavshhiki/proizvodstvo-upakovki',
        'http://pravda-sotrudnikov.ru/catalog/proizvoditeli-i-postavshhiki/selskoe-hozyaystvo',
        'http://pravda-sotrudnikov.ru/catalog/proizvoditeli-i-postavshhiki/stroitelnye-materialy',
        'http://pravda-sotrudnikov.ru/catalog/proizvoditeli-i-postavshhiki/tabachnye-kompanii',
        'http://pravda-sotrudnikov.ru/catalog/proizvoditeli-i-postavshhiki/farmacevticheskie-kompanii',
        'http://pravda-sotrudnikov.ru/catalog/proizvoditeli-i-postavshhiki/himicheskaja-promyshlennos',
        'http://pravda-sotrudnikov.ru/catalog/proizvoditeli-i-postavshhiki/energeticheskie-kompanii'
    ]

    def parse(self, response):
        pages = response.xpath('//div[@class="mdc-companies-item-title"]/span/a/@href').extract()
        if pages:
            for url in pages:
                yield scrapy.Request(response.urljoin(url), callback=self.parse_page)

        next_page = response.xpath('//ul//li[@class="next"]/a/@href').extract_first()
        if next_page is not None:
            yield scrapy.Request(response.urljoin(next_page))

    @staticmethod
    def parse_page(response):

        item = {}
        name = response.xpath(
            '//div[@class="company-info-title"]//text()[normalize-space()]'
        ).extract_first()
        descr = response.xpath(
            '//div[@class="company-info-description"][normalize-space()]'
        ).extract_first()
        other_name = response.xpath(
            '//div[@class="company-info-contacts-row"][contains(./div/text(), "Другие названия")]/div[@class="company-info-contacts-row-value"]//text()[normalize-space()]'
        ).extract_first()
        phone = response.xpath(
            '//div[@class="company-info-contacts-row"][contains(./div/text(), "Телефоны")]/div[@class="company-info-contacts-row-value"]//text()[normalize-space()]'
        ).extract()
        email = response.xpath(
            '//div[@class="company-info-contacts-row"][contains(./span/text(), "Email")]/span[@class="company-info-contacts-row-value"]//text()[normalize-space()]'
        ).extract_first()
        site = response.xpath(
            '//div[@class="company-info-contacts-row"][contains(./span/text(), "Сайт")]/span[@class="company-info-contacts-row-value"]/a/@href'
        ).extract_first()
        category = response.xpath(
            '//div[@class="company-info-contacts-row"][contains(./div/text(), "Сфера деятельности")]/div[@class="company-info-contacts-row-value"]//text()[normalize-space()]'
        ).extract_first()
        regions = response.xpath(
            '//div[contains(@class, "company-info-localitys")]/div/a/text()'
        ).extract()
        views = response.xpath(
            '//span[@class="company-info-views-count"]/text()'
        ).re(r'[0-9]+')
        company_id = response.xpath(
            '//div[contains(@class, "company-info-logo")]/img/@src'
        ).re(r'company-([0-9]+).png')
        company_url = response.url

        if name:
            item['name'] = name.strip()
        if descr:
            item['description'] = descr.strip()
        if other_name:
            item['other_name'] = other_name.strip()
        if phone:
            item['phone'] = phone
        if email:
            item['email'] = email.strip()
        if category:
            item['category'] = category.strip()
        if site:
            item['site'] = site.strip()
        if regions:
            item['regions'] = regions
        if views:
            item['views'] = views[0]
        if company_id:
            item['company_id'] = company_id[0]
        item['url'] = company_url

        yield item
