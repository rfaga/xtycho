# -*- coding: utf-8 -*-
import scrapy
import urlparse
from xtycho.items import LattesItem

class TychoSpider(scrapy.Spider):
    name = "tycho"
    allowed_domains = ["uspdigital.usp.br"]
    start_urls = (
        'https://uspdigital.usp.br/tycho/curriculoLattesListarUnidades?vinculo=DOCENTE',
    )

    def parse(self, response):
        for url in response.css('#layout_conteudo table.table_list a::attr("href")'):
            yield scrapy.Request(response.urljoin(url.extract()) + '&formato=xml', self.parse_unidade)

    def parse_unidade(self, response):
        d = urlparse.parse_qs(response.url)
        for sel in response.css('objeto'):
            item = LattesItem()
            item['idLattes'] = sel.css('idLattes::text').extract_first()
            item['nome'] = sel.css('nome::text').extract_first()
            item['dataAtualizacao'] = sel.css('dataAtualizacao::text').extract_first()
            item['tipoVinculo'] = d['tipoVinculo'][0]
            item['nomeUnidade'] = d['nomeUnidade'][0]
            yield item
