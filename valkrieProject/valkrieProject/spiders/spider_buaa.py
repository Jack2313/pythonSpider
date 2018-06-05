import scrapy
import re
from valkrieProject.items import ValkrieprojectItem

class buaaSpider(scrapy.Spider):
    name = "buaa"

    def start_requests(self):
        urls = [
            'http://shi.buaa.edu.cn/Leo_Tam/zh_CN/index.htm',
            'http://shi.buaa.edu.cn/liuzhiqi/zh_CN/index.htm',
            'http://shi.buaa.edu.cn/xingyufeng/zh_CN/index.htm'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-3]
        filename = 'info-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

        people=ValkrieprojectItem()
        people['name']=''
        people['degree']=''
        people['insitution']=''
        people['contact']=''
        people['field']=''
        people['name']=response.xpath('//div[@class="name"]/h1/text()').extract()
        basicInfo=response.xpath('//div[@class="jbqk"]/p/text()').extract()

        for i in basicInfo :
            #print (i)
            str=''.join(i)

            if re.match('学位',i):
                people['degree']=i.split("：")[-1]
                #print(people['degree'])
                continue
            if re.match('学历',i):
                people['degree']=i.split("：")[-1]
                #print(people['degree'])
                continue
            if re.match('所在单位',i):
                people['insitution']=i.split("：")[-1]
                #print(people['insitution'])
                continue
            if re.match('联系方式',i):
                people['contact']=i.split("：")[-1]
                #print(people['contact'])
                continue

        #moreInfo=response.xpath('//div[@class="con_bload"]/test()').extract()
        #for i in moreInfo:
        #    if re.match('<h2>研究方向</h2>',i):
        #        people['field']=i.split("：")[-1]
        #        #print(people['degree'])
        #        continue
        people['field']=response.xpath('//div[@class="con_bload" and h2="研究方向"]/li/p/text()').extract()
        people['description'] = response.xpath('//div[@class="con_bload" and h2="个人简历"]/p/text()').extract()
        #print (people['field'])
        urlhead='http://shi.buaa.edu.cn/xingyufeng'
        paperurl=response.xpath('//div[@id="rightside"]/div[@class="nav"]/div[@class="menu"]/div/ul/li[a=" 论文"]/a/@href').extract()
        if not paperurl:
            people['papers']=''
        else :
            paperurl=urlhead+''.join(paperurl)
            #print ('------------'+paperurl+'------------')


        yield people

    def parse_url(self, response):
