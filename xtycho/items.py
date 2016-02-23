# -*- coding: utf-8 -*-

import scrapy


class LattesItem(scrapy.Item):
    nome = scrapy.Field()
    idLattes = scrapy.Field()
    dataAtualizacao = scrapy.Field()
    tipoVinculo = scrapy.Field()
    nomeUnidade = scrapy.Field()
