# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
class ValkrieprojectPipeline(object):
    number=0
    def __init__(self):
        self.file = open("info.txt",'a')

    def process_item(self, item, spider):
        self.number=self.number+1
        self.file.write('number:' + str(self.number) + '\n')
        self.file.write('name:'+''.join(item['name']) + '\n')
        self.file.write('degree:' + ''.join(item['degree']) + '\n')
        self.file.write('institution:' + ''.join(item['institution']) + '\n')
        self.file.write('contact:' + ''.join(item['contact']) + '\n')
        self.file.write('field:' + ''.join(item['field']) + '\n')
        self.file.write('description:' + ''.join(item['description']) + '\n')
        self.file.write('papers:\n' + ''.join(item['papers']) + '\n')
        self.file.write('\n')