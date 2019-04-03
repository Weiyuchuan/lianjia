from lxml import etree
import requests

class lianjia:
    def __init__(self,base_url):
        self.html_tree = self.requestt_url(base_url)
        self.parse_html()
    def requestt_url(self,url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
        html = requests.get(url=url,headers=headers).content.decode('utf-8')
        # print(html)
        tree = etree.HTML(html)
        # print(tree)
        return tree
    def parse_html(self):
        area_1 = self.html_tree.xpath('//div[@class="position"]//div[@data-role="ershoufang"]//a/@href')
        name_1 = self.html_tree.xpath('//div[@class="position"]//div[@data-role="ershoufang"]//a/text()')
        for a1 ,n1 in zip(area_1,name_1):
            # print(a1,n1)
            for page in range(1,100):
                area_2 = 'https://zz.lianjia.com'+a1+'pg{}'.format(page)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`{}~~~~~~~~~~~~~~~~~~~~~~~~~".format(n1))
                # print(area_2,n1)
                area_2_html = self.requestt_url(area_2)
                # print(etree.tostring(area_2_html))
                # print(len(area_2_html))
                test = area_2_html.xpath('//li[@class="clear LOGCLICKDATA"]')
                for li  in test:
                    # print(etree.tostring(li))
                    info = li.xpath('./div[@class="info clear"]')[0]
                    name = info.xpath('./div[@class="title"]/a/text()')
                    dizhi = info.xpath('.//div[@class="houseInfo"]//text()')
                    positionInfo = info.xpath('.//div[@class="positionInfo"]//text()')
                    followInfo = info.xpath('.//div[@class="followInfo"]//text()')
                    totalPrice = info.xpath('.//div[@class="totalPrice"]//text()')
                    unitPrice = info.xpath('.//div[@class="unitPrice"]//text()')
                    a=name+dizhi+positionInfo+followInfo+totalPrice+unitPrice
                    b=':'.join(a)
                    print(b)
                    # print(unitPrice)
                    # print(followInfo)
                    # print(name[0])
                    # print(dizhi)
                    # print(type(li))
                    with open("链家网.txt",'a',encoding='utf-8')as fp:
                        # fp.write(n1+'第%页:')%page
                        fp.write('~~~~~~~~~~~~~~~{}~~~~~~~~~~~~~~~~~~~~~~~~'.format(n1)+'\n')
                        fp.write('~~~~~~~~~~~~~~~第{}页~~~~~~~~~~~~~~~~~~~~~~~~~'.format(page)+'\n')
                        fp.write('名字：' + name[0]+':'+'\n')
                        fp.write('地址：' + dizhi[0] + ':' + '\n')
                        fp.write('定位：' + positionInfo[0] + ':' + '\n')
                        fp.write('信息：' + followInfo[0] + ':' + '\n')
                        fp.write('总价：' + totalPrice[0] + ':' +'万'+ '\n')
                        fp.write('单价：' + unitPrice[0] +':'+'\n'+'\n')

if __name__ == '__main__':
    base_url = 'https://zz.lianjia.com/ershoufang/'
    lianjia(base_url)



