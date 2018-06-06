# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ValkrieprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    #name

    degree = scrapy.Field()
    #master/doctor

    field =scrapy.Field()
    #field that he/she research

    institution =scrapy.Field()
    #where he/she work

    contact=scrapy.Field()
    email=scrapy.Field()
    description=scrapy.Field()

    photo=scrapy.Field()

    number=scrapy.Field()
    papers=scrapy.Field()
    pass
