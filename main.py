import twint
import pandas as pd


class FindTweet:

    def __init__(self, keyword:str, save_dir:str, limit:int):
        self.keyword = keyword
        self.save_dir = save_dir
        self.limit = limit
        self.config = None
        self.init_config()

    def init_config(self):
        self.config = twint.Config()
        self.config.Search = self.keyword
        self.config.Store_json = True
        self.config.Limit = self.limit
        self.config.Output = self.save_dir

    def run(self):
        twint.run.Search(self.config)
        data = pd.read_json(path, lines=True)
        selection = data[['date', 'time', 'username',
                          'name', 'tweet', 'retweets_count',
                          'likes_count', 'link']]
        html = selection.to_html()
        text_file = open("index.html", "w")
        text_file.write(html)
        text_file.close()


if __name__ == '__main__':
    path = 'data.json'
    keyword = 'request for startup'
    limit = 40
    tw = FindTweet(keyword, path, limit)
    tw.run()
