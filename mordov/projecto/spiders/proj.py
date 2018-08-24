# -*- coding: utf-8 -*-
import scrapy


class ProjSpider(scrapy.Spider):
    name = 'proj'
    allowed_domains = ['www.mordovmedia.ru']
    start_urls = [
        'http://www.mordovmedia.ru/company_category/364/', 'http://www.mordovmedia.ru/company_category/323/',
        'http://www.mordovmedia.ru/company_category/324/', 'http://www.mordovmedia.ru/company_category/245/',
        'http://www.mordovmedia.ru/company_category/406/', 'http://www.mordovmedia.ru/company_category/248/',
        'http://www.mordovmedia.ru/company_category/249/', 'http://www.mordovmedia.ru/company_category/250/',
        'http://www.mordovmedia.ru/company_category/252/', 'http://www.mordovmedia.ru/company_category/256/',
        'http://www.mordovmedia.ru/company_category/257/', 'http://www.mordovmedia.ru/company_category/258/',
        'http://www.mordovmedia.ru/company_category/260/', 'http://www.mordovmedia.ru/company_category/262/',
        'http://www.mordovmedia.ru/company_category/265/', 'http://www.mordovmedia.ru/company_category/266/',
        'http://www.mordovmedia.ru/company_category/349/', 'http://www.mordovmedia.ru/company_category/393/',
        'http://www.mordovmedia.ru/company_category/407/', 'http://www.mordovmedia.ru/company_category/271/',
        'http://www.mordovmedia.ru/company_category/272/', 'http://www.mordovmedia.ru/company_category/275/',
        'http://www.mordovmedia.ru/company_category/380/', 'http://www.mordovmedia.ru/company_category/379/',
        'http://www.mordovmedia.ru/company_category/351/', 'http://www.mordovmedia.ru/company_category/101/',
        'http://www.mordovmedia.ru/company_category/102/', 'http://www.mordovmedia.ru/company_category/103/',
        'http://www.mordovmedia.ru/company_category/106/', 'http://www.mordovmedia.ru/company_category/284/',
        'http://www.mordovmedia.ru/company_category/387/', 'http://www.mordovmedia.ru/company_category/404/',
        'http://www.mordovmedia.ru/company_category/386/', 'http://www.mordovmedia.ru/company_category/388/',
        'http://www.mordovmedia.ru/company_category/390/', 'http://www.mordovmedia.ru/company_category/385/',
        'http://www.mordovmedia.ru/company_category/391/', 'http://www.mordovmedia.ru/company_category/401/',
        'http://www.mordovmedia.ru/company_category/403/', 'http://www.mordovmedia.ru/company_category/405/',
        'http://www.mordovmedia.ru/company_category/86/', 'http://www.mordovmedia.ru/company_category/311/',
        'http://www.mordovmedia.ru/company_category/87/', 'http://www.mordovmedia.ru/company_category/88/',
        'http://www.mordovmedia.ru/company_category/89/', 'http://www.mordovmedia.ru/company_category/365/',
        'http://www.mordovmedia.ru/company_category/108/', 'http://www.mordovmedia.ru/company_category/110/',
        'http://www.mordovmedia.ru/company_category/111/', 'http://www.mordovmedia.ru/company_category/112/',
        'http://www.mordovmedia.ru/company_category/113/', 'http://www.mordovmedia.ru/company_category/114/',
        'http://www.mordovmedia.ru/company_category/411/', 'http://www.mordovmedia.ru/company_category/285/',
        'http://www.mordovmedia.ru/company_category/286/', 'http://www.mordovmedia.ru/company_category/288/',
        'http://www.mordovmedia.ru/company_category/289/', 'http://www.mordovmedia.ru/company_category/291/',
        'http://www.mordovmedia.ru/company_category/294/', 'http://www.mordovmedia.ru/company_category/352/',
        'http://www.mordovmedia.ru/company_category/117/', 'http://www.mordovmedia.ru/company_category/295/',
        'http://www.mordovmedia.ru/company_category/504/', 'http://www.mordovmedia.ru/company_category/505/',
        'http://www.mordovmedia.ru/company_category/52/', 'http://www.mordovmedia.ru/company_category/53/',
        'http://www.mordovmedia.ru/company_category/54/', 'http://www.mordovmedia.ru/company_category/55/',
        'http://www.mordovmedia.ru/company_category/502/', 'http://www.mordovmedia.ru/company_category/413/',
        'http://www.mordovmedia.ru/company_category/59/', 'http://www.mordovmedia.ru/company_category/500/',
        'http://www.mordovmedia.ru/company_category/62/', 'http://www.mordovmedia.ru/company_category/509/',
        'http://www.mordovmedia.ru/company_category/510/', 'http://www.mordovmedia.ru/company_category/419/',
        'http://www.mordovmedia.ru/company_category/381/', 'http://www.mordovmedia.ru/company_category/414/',
        'http://www.mordovmedia.ru/company_category/512/', 'http://www.mordovmedia.ru/company_category/513/',
        'http://www.mordovmedia.ru/company_category/416/', 'http://www.mordovmedia.ru/company_category/299/',
        'http://www.mordovmedia.ru/company_category/296/', 'http://www.mordovmedia.ru/company_category/297/',
        'http://www.mordovmedia.ru/company_category/518/', 'http://www.mordovmedia.ru/company_category/501/',
        'http://www.mordovmedia.ru/company_category/298/', 'http://www.mordovmedia.ru/company_category/503/',
        'http://www.mordovmedia.ru/company_category/516/', 'http://www.mordovmedia.ru/company_category/514/',
        'http://www.mordovmedia.ru/company_category/517/', 'http://www.mordovmedia.ru/company_category/119/',
        'http://www.mordovmedia.ru/company_category/120/', 'http://www.mordovmedia.ru/company_category/123/',
        'http://www.mordovmedia.ru/company_category/409/', 'http://www.mordovmedia.ru/company_category/121/',
        'http://www.mordovmedia.ru/company_category/127/', 'http://www.mordovmedia.ru/company_category/139/',
        'http://www.mordovmedia.ru/company_category/140/', 'http://www.mordovmedia.ru/company_category/142/',
        'http://www.mordovmedia.ru/company_category/143/', 'http://www.mordovmedia.ru/company_category/145/',
        'http://www.mordovmedia.ru/company_category/359/', 'http://www.mordovmedia.ru/company_category/354/',
        'http://www.mordovmedia.ru/company_category/358/', 'http://www.mordovmedia.ru/company_category/147/',
        'http://www.mordovmedia.ru/company_category/371/', 'http://www.mordovmedia.ru/company_category/150/',
        'http://www.mordovmedia.ru/company_category/357/', 'http://www.mordovmedia.ru/company_category/193/',
        'http://www.mordovmedia.ru/company_category/520/', 'http://www.mordovmedia.ru/company_category/400/',
        'http://www.mordovmedia.ru/company_category/153/', 'http://www.mordovmedia.ru/company_category/154/',
        'http://www.mordovmedia.ru/company_category/155/', 'http://www.mordovmedia.ru/company_category/356/',
        'http://www.mordovmedia.ru/company_category/303/', 'http://www.mordovmedia.ru/company_category/240/',
        'http://www.mordovmedia.ru/company_category/1/', 'http://www.mordovmedia.ru/company_category/362/',
        'http://www.mordovmedia.ru/company_category/2/', 'http://www.mordovmedia.ru/company_category/3/',
        'http://www.mordovmedia.ru/company_category/4/', 'http://www.mordovmedia.ru/company_category/5/',
        'http://www.mordovmedia.ru/company_category/7/', 'http://www.mordovmedia.ru/company_category/8/',
        'http://www.mordovmedia.ru/company_category/9/', 'http://www.mordovmedia.ru/company_category/395/',
        'http://www.mordovmedia.ru/company_category/10/', 'http://www.mordovmedia.ru/company_category/14/',
        'http://www.mordovmedia.ru/company_category/15/', 'http://www.mordovmedia.ru/company_category/16/',
        'http://www.mordovmedia.ru/company_category/363/', 'http://www.mordovmedia.ru/company_category/21/',
        'http://www.mordovmedia.ru/company_category/22/', 'http://www.mordovmedia.ru/company_category/130/',
        'http://www.mordovmedia.ru/company_category/131/', 'http://www.mordovmedia.ru/company_category/132/',
        'http://www.mordovmedia.ru/company_category/133/', 'http://www.mordovmedia.ru/company_category/134/',
        'http://www.mordovmedia.ru/company_category/135/', 'http://www.mordovmedia.ru/company_category/398/',
        'http://www.mordovmedia.ru/company_category/402/', 'http://www.mordovmedia.ru/company_category/137/',
        'http://www.mordovmedia.ru/company_category/27/', 'http://www.mordovmedia.ru/company_category/32/',
        'http://www.mordovmedia.ru/company_category/33/', 'http://www.mordovmedia.ru/company_category/397/',
        'http://www.mordovmedia.ru/company_category/28/', 'http://www.mordovmedia.ru/company_category/34/',
        'http://www.mordovmedia.ru/company_category/36/', 'http://www.mordovmedia.ru/company_category/366/',
        'http://www.mordovmedia.ru/company_category/369/', 'http://www.mordovmedia.ru/company_category/156/',
        'http://www.mordovmedia.ru/company_category/372/', 'http://www.mordovmedia.ru/company_category/157/',
        'http://www.mordovmedia.ru/company_category/158/', 'http://www.mordovmedia.ru/company_category/159/',
        'http://www.mordovmedia.ru/company_category/160/', 'http://www.mordovmedia.ru/company_category/161/',
        'http://www.mordovmedia.ru/company_category/162/', 'http://www.mordovmedia.ru/company_category/163/',
        'http://www.mordovmedia.ru/company_category/314/', 'http://www.mordovmedia.ru/company_category/164/',
        'http://www.mordovmedia.ru/company_category/373/', 'http://www.mordovmedia.ru/company_category/166/',
        'http://www.mordovmedia.ru/company_category/304/', 'http://www.mordovmedia.ru/company_category/39/',
        'http://www.mordovmedia.ru/company_category/167/', 'http://www.mordovmedia.ru/company_category/168/',
        'http://www.mordovmedia.ru/company_category/169/', 'http://www.mordovmedia.ru/company_category/315/',
        'http://www.mordovmedia.ru/company_category/172/', 'http://www.mordovmedia.ru/company_category/42/',
        'http://www.mordovmedia.ru/company_category/173/', 'http://www.mordovmedia.ru/company_category/174/',
        'http://www.mordovmedia.ru/company_category/175/', 'http://www.mordovmedia.ru/company_category/317/',
        'http://www.mordovmedia.ru/company_category/177/', 'http://www.mordovmedia.ru/company_category/178/',
        'http://www.mordovmedia.ru/company_category/180/', 'http://www.mordovmedia.ru/company_category/519/',
        'http://www.mordovmedia.ru/company_category/183/', 'http://www.mordovmedia.ru/company_category/396/',
        'http://www.mordovmedia.ru/company_category/186/', 'http://www.mordovmedia.ru/company_category/187/',
        'http://www.mordovmedia.ru/company_category/188/', 'http://www.mordovmedia.ru/company_category/189/',
        'http://www.mordovmedia.ru/company_category/190/', 'http://www.mordovmedia.ru/company_category/192/',
        'http://www.mordovmedia.ru/company_category/195/', 'http://www.mordovmedia.ru/company_category/197/',
        'http://www.mordovmedia.ru/company_category/198/', 'http://www.mordovmedia.ru/company_category/199/',
        'http://www.mordovmedia.ru/company_category/79/', 'http://www.mordovmedia.ru/company_category/78/',
        'http://www.mordovmedia.ru/company_category/81/', 'http://www.mordovmedia.ru/company_category/80/',
        'http://www.mordovmedia.ru/company_category/85/', 'http://www.mordovmedia.ru/company_category/202/',
        'http://www.mordovmedia.ru/company_category/399/', 'http://www.mordovmedia.ru/company_category/408/',
        'http://www.mordovmedia.ru/company_category/394/', 'http://www.mordovmedia.ru/company_category/374/',
        'http://www.mordovmedia.ru/company_category/318/', 'http://www.mordovmedia.ru/company_category/203/',
        'http://www.mordovmedia.ru/company_category/57/', 'http://www.mordovmedia.ru/company_category/375/',
        'http://www.mordovmedia.ru/company_category/60/', 'http://www.mordovmedia.ru/company_category/204/',
        'http://www.mordovmedia.ru/company_category/377/', 'http://www.mordovmedia.ru/company_category/206/',
        'http://www.mordovmedia.ru/company_category/63/', 'http://www.mordovmedia.ru/company_category/64/',
        'http://www.mordovmedia.ru/company_category/321/', 'http://www.mordovmedia.ru/company_category/410/',
        'http://www.mordovmedia.ru/company_category/209/', 'http://www.mordovmedia.ru/company_category/212/',
        'http://www.mordovmedia.ru/company_category/376/', 'http://www.mordovmedia.ru/company_category/68/',
        'http://www.mordovmedia.ru/company_category/213/', 'http://www.mordovmedia.ru/company_category/378/',
        'http://www.mordovmedia.ru/company_category/214/', 'http://www.mordovmedia.ru/company_category/215/',
        'http://www.mordovmedia.ru/company_category/383/', 'http://www.mordovmedia.ru/company_category/216/',
        'http://www.mordovmedia.ru/company_category/412/', 'http://www.mordovmedia.ru/company_category/219/',
        'http://www.mordovmedia.ru/company_category/320/', 'http://www.mordovmedia.ru/company_category/319/',
        'http://www.mordovmedia.ru/company_category/76/', 'http://www.mordovmedia.ru/company_category/77/',
        'http://www.mordovmedia.ru/company_category/220/', 'http://www.mordovmedia.ru/company_category/90/',
        'http://www.mordovmedia.ru/company_category/91/', 'http://www.mordovmedia.ru/company_category/92/',
        'http://www.mordovmedia.ru/company_category/93/', 'http://www.mordovmedia.ru/company_category/94/',
        'http://www.mordovmedia.ru/company_category/221/', 'http://www.mordovmedia.ru/company_category/222/',
        'http://www.mordovmedia.ru/company_category/223/', 'http://www.mordovmedia.ru/company_category/224/',
        'http://www.mordovmedia.ru/company_category/226/', 'http://www.mordovmedia.ru/company_category/227/',
        'http://www.mordovmedia.ru/company_category/228/', 'http://www.mordovmedia.ru/company_category/229/',
        'http://www.mordovmedia.ru/company_category/230/', 'http://www.mordovmedia.ru/company_category/231/',
        'http://www.mordovmedia.ru/company_category/234/', 'http://www.mordovmedia.ru/company_category/235/',
        'http://www.mordovmedia.ru/company_category/322/', 'http://www.mordovmedia.ru/company_category/237/'
    ]

    def parse(self, response):
        pages = response.xpath('//div[contains(@class, "company-item")]//a/@href').extract()
        for url in pages:
            yield scrapy.Request(response.urljoin(url), callback=self.parse_page)

        next_page = response.xpath('//a[@class="right-elem"]/a/@href').extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )

    def parse_page(self, response):
        yield {
            'name': response.xpath(
                '//h1[@class="company-name"]/text()'
            ).extract_first(),
            'phones': response.xpath(
                '//span[contains(@class, "phone-item")]/text()'
            ).extract(),
            'url': response.xpath(
                '//td[contains(@class, "contacts-icon url")]/following-sibling::td//text()'
            ).extract_first(),
            'vk': response.xpath(
                '//td[contains(@class, "contacts-icon vk")]/following-sibling::td//text()'
            ).extract_first(),
            'mail': response.xpath(
                '//td[contains(@class, "contacts-icon email")]/following-sibling::td//text()'
            ).extract_first()
        }
