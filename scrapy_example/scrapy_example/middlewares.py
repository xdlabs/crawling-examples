

class CustomSpiderMiddleware:

    def process_spider_input(self, response, spider):
        print "\n\n response.url : ", response.url
