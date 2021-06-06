# 댓글 목록 불러오기

`getDCReplys()` 함수로 DC인사이드 갤러리의 댓글을 불러올 수 있습니다.

`getIlbeReplys()` 함수로 일간베스트저장소의 댓글을 불러올 수 있습니다.
사용 방법은 아래와 같습니다.

```py
from parser import Parser
# 일간베스트저장소 - 일간베스트 게시판의 1~10페이지에 있는 모든 게시물의 댓글리스트를 불러온다.
count = 10
Parser().getIlbeReplys(count)
```
`ReplyCrawler/dist/{community}-{timestamp}.txt` 파일로 저장됩니다.

# CurseDetect-py

