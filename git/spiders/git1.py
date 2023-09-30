import scrapy


class Git1Spider(scrapy.Spider):
    name = "git1"
    allowed_domains = ["github.com"]
    start_urls = ["https://github.com/heiyukuaidou23"]

    def start_requests(self):
        url = self.start_urls[0]

        temp = '_octo=GH1.1.1004902652.1694050183; _device_id=a4c3930fdf92cadab64ea634a436059a; user_session=SkFkjC40ucKDxoLbNmtJx72YHTKCrT9um6N_9vv0y3xJDLdW; __Host-user_session_same_site=SkFkjC40ucKDxoLbNmtJx72YHTKCrT9um6N_9vv0y3xJDLdW; logged_in=yes; dotcom_user=heiyukuaidou23; fileTreeExpanded=false; has_recent_activity=1; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%7D; preferred_color_mode=light; tz=Asia%2FShanghai; _gh_sess=980OzoQO%2Bh1FfDGx%2FaPIEtpE2mP%2BgYukiOXJEwrVLo6pz%2BRrf8hT9gQthbDRmJK60G321ykBhn1cXugDoSoIzWs9Yp3CER1ynEqln1JF7%2BuNKPrp85IVUcXO4fc0x9tqZw7DWmAmFdf1H%2FSfKav9atIHL1EMEPSA3ZaAD78QarUcMzwbDVVLwYbuIShXArcv72lLjVIuY%2BvWAotVxY4mJEN9Q%2B5bq1cE5Y3LMchHpjgYE3Vm%2Bf%2F%2FX9%2B6ld3DKYXrcbpidRcvMXPsPQsgiLGSm%2BVqZBmNlrDrxAs3AzUSMPTU7TvUiiZU9vyNDcI5rW3FGxsfDQ%3D%3D--BJ%2FayB7FUURu%2FdRd--'
        cookies = {data.split('=')[0]: data.split('=')[-1]for data in temp.split(';')}
        yield scrapy.Request(
            url=url,
            callback=self.parse,
            cookies=cookies
        )


    def parse(self, response):
        print(response.xpath('/html/body/div[1]/div[1]/header/div[1]/div[1]/div/div[2]/nav/ul/li/a/span/text()').extract_first())
