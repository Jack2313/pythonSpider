import scrapy
import re
from valkrieProject.items import ValkrieprojectItem

class buaaSpider(scrapy.Spider):
    name = "buaa"
    number=0;
    def start_requests(self):
        with open('url.txt', 'r+') as f:
            for url in f.readlines():
                url=url.strip()
                #self.number=self.number+1
                yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        name=''
        degree=''
        institution=''
        contact=''
        field=''
        description=''
        name=response.xpath('//div[@class="name"]/h1/text()').extract()
        basicInfo=response.xpath('//div[@class="jbqk"]/p/text()').extract()

        for i in basicInfo :
            #print (i)
            #str=''.join(i)

            if re.match('学位',i):
                degree=i.split("：")[-1]
                #print(people['degree'])
                continue
            if re.match('学历',i):
                degree=i.split("：")[-1]
                #print(people['degree'])
                continue
            if re.match('所在单位',i):
                institution=i.split("：")[-1]
                #print(people['institution'])
                continue
            if re.match('联系方式',i):
                contact=i.split("：")[-1]
                #print(people['contact'])
                continue

        field=response.xpath('//div[@class="con_bload" and h2="研究方向"]/li/p/text()').extract()
        description = response.xpath('//div[@class="con_bload" and h2="个人简历"]/p/text()').extract()
        #print (people['field'])
        urlhead='http://shi.buaa.edu.cn/'
        paperurl=response.xpath('//div[@id="rightside"]/div[@class="nav"]/div[@class="menu"]/div/ul/li[a=" 论文"]/a/@href').extract()
        if not paperurl:
            people = ValkrieprojectItem()
            people['number'] =str(self.number)
            people['papers']=''
            people['name']=name
            people['degree'] = degree
            people['institution'] = institution
            people['contact']=contact
            people['field']=field
            people['description']=description
            yield people
        else :
            paperurl=urlhead+''.join(paperurl)
            print ('------------'+paperurl+'------------')
            yield scrapy.Request(url=paperurl,callback=self.parse_paper,meta={
                'name':name,
                'degree':degree,
                'institution':institution,
                'contact':contact,
                'field':field,
                'description':description
            })
            #yield people

    def parse_paper(self, response):
        #page = response.url.split("/")[-6]
        #filename = 'paper-%s.html' % page
        #with open(filename, 'wb') as f:
        #    f.write(response.body)
        #self.log('Saved file %s' % filename)

        people = ValkrieprojectItem()

        people['papers']=''
        people['name']=response.meta['name']
        people['degree'] = response.meta['degree']
        people['institution'] =response.meta['institution']
        people['contact']=response.meta['contact']
        people['field']=response.meta['field']
        people['description']=response.meta['description']

        paper=response.xpath('//div[@class="listnews"]/ul/li/a/text()').extract()
        paperstr='\n'.join(paper)
        people['papers']=paperstr
        people['number']=str(self.number)
        yield people
