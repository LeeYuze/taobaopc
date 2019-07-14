import requests
import json

def parse_dsr(id,shop_id,isTmall):
    '''分析某宝的动态评论系统'''
    if isTmall == 'True':
        #天猫dsr
        url = 'https://dsr-rate.tmall.com/list_dsr_info.htm?itemId='+id
        headers = {
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
            'cookie':'cookie:cna=TeuoFQZkxm0CAXjvQS/Oxr/F; _m_h5_tk=aaf383c3e43685540409ddbe7d0f4766_1563008510809; _m_h5_tk_enc=45b12bae877808a9584f19c5beb87ce2; sm4=440100; hng=CN%7Czh-CN%7CCNY%7C156; uc1=cookie14=UoTaG7%2FZKHzsQg%3D%3D; t=96b35e785ef112719c0d2437fd22b0c9; uc3=vt3=F8dBy3%2F8amw5Pbmdqec%3D&id2=UNaE8t%2F7FLgNOA%3D%3D&nk2=0%2B5q0jMPD%2FVvgVvzV0Y%3D&lg2=UIHiLt3xD8xYTw%3D%3D; tracknick=%5Cu7231%5Cu542C%5Cu97F3%5Cu4E50%5Cu7684%5Cu6D69%5Cu53D4; lid=%E7%88%B1%E5%90%AC%E9%9F%B3%E4%B9%90%E7%9A%84%E6%B5%A9%E5%8F%94; lgc=%5Cu7231%5Cu542C%5Cu97F3%5Cu4E50%5Cu7684%5Cu6D69%5Cu53D4; enc=acGvv0%2BaO2uEt4LbGDltpBIEW3unTirFZBVRbv8yrsQJhQY8%2B53u9uwWzDO8Mr4mPj5adQVajtRD6Yu6liA0Pg%3D%3D; _tb_token_=5e311b53661e; cookie2=5f476051068f3d00306f15e91b0e4c4e; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; isg=BP39hIjUfDVd79jYMwnFis7ZAlk3MjGJlz6fZ79CSdSW9h8ohOjvvDvnoGoV7Umk; l=cBQUKym4qaxJ1Ui0BOCwZuI8aPbOkBd0YuPRwNcXi_5IJ_YaAg_Okc9npEv6cjWFTITe4KijACeThFHzJyTaXMJA-9cdvdC..',
            'referer':'https://detail.tmall.com/',
        }
        r = requests.get(url,headers=headers)
        r = json.loads(r.text.replace('jsonp128(','').replace(')',''))
        score = r['dsr']['gradeAvg']
        rateTotal = r['dsr']['rateTotal']
        return {
            'score':score,
            'rateTotal':rateTotal
        }
    else:
        #淘宝dsr
        url = 'https://rate.taobao.com/detailCommon.htm?auctionNumId=' + id + '&userNumId='+ shop_id +'&callback=json_tbc_rate_summary'
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
            'cookie': 'cookie:cna=TeuoFQZkxm0CAXjvQS/Oxr/F; _m_h5_tk=aaf383c3e43685540409ddbe7d0f4766_1563008510809; _m_h5_tk_enc=45b12bae877808a9584f19c5beb87ce2; sm4=440100; hng=CN%7Czh-CN%7CCNY%7C156; uc1=cookie14=UoTaG7%2FZKHzsQg%3D%3D; t=96b35e785ef112719c0d2437fd22b0c9; uc3=vt3=F8dBy3%2F8amw5Pbmdqec%3D&id2=UNaE8t%2F7FLgNOA%3D%3D&nk2=0%2B5q0jMPD%2FVvgVvzV0Y%3D&lg2=UIHiLt3xD8xYTw%3D%3D; tracknick=%5Cu7231%5Cu542C%5Cu97F3%5Cu4E50%5Cu7684%5Cu6D69%5Cu53D4; lid=%E7%88%B1%E5%90%AC%E9%9F%B3%E4%B9%90%E7%9A%84%E6%B5%A9%E5%8F%94; lgc=%5Cu7231%5Cu542C%5Cu97F3%5Cu4E50%5Cu7684%5Cu6D69%5Cu53D4; enc=acGvv0%2BaO2uEt4LbGDltpBIEW3unTirFZBVRbv8yrsQJhQY8%2B53u9uwWzDO8Mr4mPj5adQVajtRD6Yu6liA0Pg%3D%3D; _tb_token_=5e311b53661e; cookie2=5f476051068f3d00306f15e91b0e4c4e; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; isg=BP39hIjUfDVd79jYMwnFis7ZAlk3MjGJlz6fZ79CSdSW9h8ohOjvvDvnoGoV7Umk; l=cBQUKym4qaxJ1Ui0BOCwZuI8aPbOkBd0YuPRwNcXi_5IJ_YaAg_Okc9npEv6cjWFTITe4KijACeThFHzJyTaXMJA-9cdvdC..',
            'referer': 'https://detail.tmall.com/',
        }
        r = requests.get(url, headers=headers)
        r = json.loads(r.text.replace('json_tbc_rate_summary(','').replace(')',''))
        score = r['data']['correspond']
        rateTotal = r['data']['count']['total']
        return {
            'score': score,
            'rateTotal': rateTotal
        }

def parse_index(wordkey,count,if_price_min,if_price_max,if_rate_total,if_score):
    global suc_count,start_page
    print('正在采集第'+ str(start_page + 1) +'页')
    url = 'https://s.taobao.com/search?ie=utf8&q='+ wordkey + '&s=' + str(start_page * 44)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
        'cookie': 'cookie:cna=TeuoFQZkxm0CAXjvQS/Oxr/F; _m_h5_tk=aaf383c3e43685540409ddbe7d0f4766_1563008510809; _m_h5_tk_enc=45b12bae877808a9584f19c5beb87ce2; sm4=440100; hng=CN%7Czh-CN%7CCNY%7C156; uc1=cookie14=UoTaG7%2FZKHzsQg%3D%3D; t=96b35e785ef112719c0d2437fd22b0c9; uc3=vt3=F8dBy3%2F8amw5Pbmdqec%3D&id2=UNaE8t%2F7FLgNOA%3D%3D&nk2=0%2B5q0jMPD%2FVvgVvzV0Y%3D&lg2=UIHiLt3xD8xYTw%3D%3D; tracknick=%5Cu7231%5Cu542C%5Cu97F3%5Cu4E50%5Cu7684%5Cu6D69%5Cu53D4; lid=%E7%88%B1%E5%90%AC%E9%9F%B3%E4%B9%90%E7%9A%84%E6%B5%A9%E5%8F%94; lgc=%5Cu7231%5Cu542C%5Cu97F3%5Cu4E50%5Cu7684%5Cu6D69%5Cu53D4; enc=acGvv0%2BaO2uEt4LbGDltpBIEW3unTirFZBVRbv8yrsQJhQY8%2B53u9uwWzDO8Mr4mPj5adQVajtRD6Yu6liA0Pg%3D%3D; _tb_token_=5e311b53661e; cookie2=5f476051068f3d00306f15e91b0e4c4e; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; isg=BP39hIjUfDVd79jYMwnFis7ZAlk3MjGJlz6fZ79CSdSW9h8ohOjvvDvnoGoV7Umk; l=cBQUKym4qaxJ1Ui0BOCwZuI8aPbOkBd0YuPRwNcXi_5IJ_YaAg_Okc9npEv6cjWFTITe4KijACeThFHzJyTaXMJA-9cdvdC..',
        'referer': 'https://detail.tmall.com/',
    }
    r = requests.get(url, headers=headers)
    r = r.text
    start = r.find('g_page_config = ')+len('g_page_config = ')
    end = r.find('shopcardOff":true}}')+len('shopcardOff":true}}')
    js = json.loads(r[start:end])
    for i in js['mods']['itemlist']['data']['auctions']:
        #商品id
        goods_id = i['nid']
        #商品标题
        goods_title = str(i['title']).replace('<span class=H>','').replace('</span>','')
        #商品价格
        goods_price = i['view_price']
        #商品链接
        goods_url = i['detail_url']
        if goods_url[0] == '/':
            goods_url = 'https:'+ goods_url
        #店铺名称
        shop_title = i['nick']
        #是否天猫店铺
        isTmall = i['shopcard']['isTmall']
        #店铺id
        shop_id = i['user_id']

        dsr = parse_dsr(goods_id,shop_id,isTmall)
        #商品平均分
        score = dsr['score']
        #商品评论总数
        rate_total = dsr['rateTotal']

        if suc_count >= count:
            break
        else:
            if float(goods_price) >= if_price_min and float(goods_price) <= if_price_max:
                if int(rate_total) >= if_rate_total:
                    if float(score) >= if_score:
                        suc_count +=1
                        print(suc_count,goods_title,goods_price,score,rate_total,isTmall,goods_url)

    if suc_count >= count:
        print('采集完毕')
    else:
        start_page += 1
        parse_index(wordkey, count, if_price_min, if_price_max, if_rate_total, if_score)


def main():
    global suc_count,start_page
    start_page = 0
    suc_count = 0

    关键词 = '壁挂'
    采集数量 = 200
    最低价格 = 20
    最高价格 = 200
    最少评论数 = 100
    最低平均分 = 4.9

    parse_index(关键词,采集数量,最低价格,最高价格,最少评论数,最低平均分)

if __name__ == '__main__':
     main()
