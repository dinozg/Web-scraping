# Define your item pipelines here

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

class FirstscrapingPipeline:
    def process_item(self, item, spider):
        return item
