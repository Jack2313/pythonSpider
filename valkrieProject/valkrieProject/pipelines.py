# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
class ValkrieprojectPipeline(object):
    def __init__(self):
        self.file = open("info.txt",'a')

    def process_item(self, item, spider):
        if item is None:
            print ('-------------------in if\n')
            return
        else :
            self.file.write('name:'+''.join(item['name']) + '\n')
            self.file.write('degree:' + ''.join(item['degree']) + '\n')
            self.file.write('insitution:' + ''.join(item['insitution']) + '\n')
            self.file.write('contact:' + ''.join(item['contact']) + '\n')
            self.file.write('field:' + ''.join(item['field']) + '\n')