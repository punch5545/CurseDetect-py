from crawler import Crawler

class IlbeParser():
    def __init__(self):
        self.url = "https://www.ilbe.com"
        self.postList = []

    def getBS(self, url):
        return Crawler(self.url+url).getHtml()
        

    def getIlbePosts(self, page): # Get Posts from Ilbe - Daily Best
        param = str.format("?page={0}&listStyle=list", page)
        url = str.format("/list/ilbe{0}", param)
        bs = self.getBS(url)
        posts = bs.find('div', class_='board-list').select('li span a.subject')
        postList = []
        for post in posts:
            postList.append(post['href'].replace(param, "").replace("/view/", ""))

        return postList

    def getIlbePostsCount(self, pageCount): # for loop getIlbePosts function in range.
        for c in range(1, pageCount):
            posts = self.getIlbePosts(c)
            print (str.format("Getting Posts from '/list/ilbe?page={0}'", c), end="\r")
            self.postList.extend(posts)
    
    def getReplyFromUrl(self, postNum): # Get reply from post
        url = str.format("/commentlist/{0}", postNum) 
        print (str.format("Getting replys from '/commentlist/{0}'       ", postNum), end="\r")
        bs = self.getBS(url)
        comments = bs.find_all('div', class_='comment-item')
        commentList = []
        for cmt in comments:
            if cmt.find('span', class_='cmt') is not None:
                commentList.append(cmt.find('span', class_='cmt').get_text())
        return commentList


class Parser():
    def __init__(self):
        pass

    def getIlbeReplys(self, count):
        ilbe = IlbeParser()
        ilbe.getIlbePostsCount(count)

        replys = []

        for post in ilbe.postList:
            replys.extend(ilbe.getReplyFromUrl(post))

        import datetime
        f = open(str.format("../dist/ilbe-{0}.txt", datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')), 'w')
        for reply in replys:
            f.write(str.format("{0}\n", reply))
        f.close()
    
    def GetAllReplys(self, count):
        ilbe = IlbeParser()
        ilbe.getIlbePostsCount(100)

        replys = []

        for post in ilbe.postList:
            replys.extend(ilbe.getReplyFromUrl(post))

        import datetime
        f = open(str.format("../dist/{0}.txt", datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')), 'w')
        for reply in replys:
            f.write(str.format("{0}\n", reply))
        f.close()