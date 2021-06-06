from crawler import Crawler
import requests

class IlbeParser():
    def __init__(self):
        self.url = "https://www.ilbe.com"
        self.postList = []

    def getBS(self, url):
        return Crawler(self.url+url).getHtml()
        

    def getPosts(self, page): # Get Posts from Ilbe - Daily Best
        param = str.format("?page={0}&listStyle=list", page)
        url = str.format("/list/ilbe{0}", param)
        bs = self.getBS(url)
        posts = bs.find('div', class_='board-list').select('li span a.subject')
        postList = []
        for post in posts:
            postList.append(post['href'].replace(param, "").replace("/view/", ""))

        return postList

    def getPostsCount(self, pageCount): # for loop getIlbePosts function in range.
        for c in range(1, pageCount):
            posts = self.getPosts(c)
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



##### Request POST 로 요청해야하나, same-origin 정책때문에 사용할 수 없음.
##### Selenium 등의 Rendered page crawler 사용 필요

class DCParser():
    def __init__(self, gallery):
        self.url = "https://gall.dcinside.com/board/lists/"
        self.e_s_n_o = "3eabc219ebdd65f23d"
        self.gallery = gallery
        self.postList = []

    def getPosts(self, page): # Get Posts from Ilbe - Daily Best
        param = str.format("?id={0}&page={1}", self.gallery, page)
        bs = self.getBS(url)
        posts = bs.find('table', class_='gall_list').select('tbody.us-post')
        postList = []
        for post in posts:
            postList.append(post['data-no'])

        return postList

    def getPostsCount(self, pageCount): # for loop getIlbePosts function in range.
        for c in range(1, pageCount):
            posts = self.getPosts(c)
            print (str.format("Getting Posts from '/board/view/?id={0}&no={1}'", self.gallery, c), end="\r")
            self.postList.extend(posts)
    
    def getReplyFromUrl(self, postNum): # Get reply from post
        print (str.format("Getting replys from '/board/comment/?id={0}&no={1}'       ", postNum), end="\r")

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
        ilbe.getPostsCount(count)

        replys = []

        for post in ilbe.postList:
            replys.extend(ilbe.getReplyFromUrl(post))

        import datetime
        f = open(str.format("../dataset/unlabeled/ilbe-{0}.txt", datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')), 'w')
        for reply in replys:
            f.write(str.format("{0}\n", reply.replace("\r\n", "\t")))
        f.close()