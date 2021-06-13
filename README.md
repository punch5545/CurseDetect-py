# 한국어 욕설 감지 프로젝트 CurseDetect-py
* 한국어 욕설을 감지하는 프로젝트입니다.
* 개발 진행중인 프로젝트로, 데이터셋과 모델이 포함될 예정입니다.
* 진행이 완료되는대로 아래 Readme에 설명란이 순차적으로 추가될 예정입니다.
* Reference Project - [욕설감지기](https://github.com/2runo/Curse-detection),  [TFJS Models - Toxicity](https://github.com/tensorflow/tfjs-models/tree/master/toxicity)

## 목차

* 댓글 목록 불러오기
* Data labeling
* 모델 생성하기

## 댓글 목록 불러오기

`getIlbeReplys()` 함수로 일간베스트저장소의 댓글을 불러올 수 있습니다.

```py
from parser import Parser

count = 10
# 일간베스트저장소 - 일간베스트 게시판의 1~10페이지에 있는 모든 게시물의 댓글리스트를 불러온다.
Parser().getIlbeReplys(count)

```
* `dataset/unlabeled/ilbe-{timestamp}.txt` 파일로 저장되며, 파일 저장 시 `개행문자(\r\n)`는 `탭문자(\t)`로 치환됩니다. 
* `DC인사이드` 커뮤니티의 댓글목록은 Request POST 로 요청해야하며 same-origin 정책때문에 `requests`를 사용할 수 없어 제외하였습니다.

## Data labeling
* 일간베스트에 업로드된 약 8만개의 댓글을 분류중입니다. (2,000개 완료.. 진행중)
* 각 구분의 기준에 부합하는 경우 `1`, 부합하지 않거나 애매한 경우 `0`으로 분류했습니다.
* 모델은 [욕설감지기 데이터셋](https://github.com/2runo/Curse-detection-data)과 직접 분류한 댓글 데이터셋으로 학습하였습니다.
* [욕설감지기 데이터셋](https://github.com/2runo/Curse-detection-data)과 같은 기준으로 판단하였습니다.

### Labeling 기준
구분|기준
-|-
욕설|사회통념상 욕설 또는 성적인 단어를 포함하거나 타인에게 모욕적인 언사를 행했을 시
혐오표현|지역감정을 조장하거나 불쾌감을 주는 단어 또는 사회통념상의 혐오표현 사용시
젠더|젠더갈등을 조장하는 문장일 경우


## 모델 생성하기
