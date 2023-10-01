import scrapy


class Git2Spider(scrapy.Spider):
    name = "git2"
    allowed_domains = ["github.com"]
    start_urls = ["https://github.com/login"]

    def parse(self, response):
        # 1.从登录页面的响应数据解析出post数据
        token = response.xpath('//input[@name="authenticity_token"]/@value').extract_first()

        post_data = {
            'commit': 'Sign in',
            'authenticity_token': token,
            'login': 'heiyukuaidou23',
            'password': '*******',
            'webauthn-conditional': 'undefined',
            'javascript - support': 'true',
            'webauthn-support': 'supported'
        }
        # print(post_data)
        # 2.针对登录url发送post请求
        yield scrapy.FormRequest(
            url='https://github.com/session',
            callback=self.after_login,
            formdata=post_data
        )

    def after_login(self, response):
        yield scrapy.Request('https://github.com/heiyukuaidou23', callback=self.check_login)

    def check_login(self, response):
        print(response.xpath(
            '/html/body/div[1]/div[1]/header/div[1]/div[1]/div/div[2]/nav/ul/li/a/span/text()').extract_first())
