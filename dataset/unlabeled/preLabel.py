# curseList = ["갈보", "개년","개새","개쓰레기","거렁뱅이","걸레","개새끼","그지","급식충","김치년","김치녀","구더기","구데기","ㄴㄷㅆ","느개비","느금마","느검마","느개미","느그애비","너검마","느금","니미","나가뒤져","등신","따까리","딸딸이","또라이","똘마니","미친놈","미친년","ㅁㅊㄴ","미친ㄴ","ㅁㅊ년","ㅁㅊ놈","미친새끼","병신","븅신","빙신","ㅄ","ㅂㅅ","벌레새끼","보지","뷰지","ㅂㅈ","빡대가리","병신새끼","븅신새끼","빙신새끼","ㅄ새끼","ㅂㅅ새끼","씨발","ㅆㅂ","시발","ㅅㅂ","시팔","씨팔","십팔","씹","쌍년","썅년","썅놈","쌍놈","ㅆㄴ","아가리","에미","애미","애비","애새끼","앰흑","엠창","엄창","앰창","염병","운지","자지","존나","쥬지","젖","좆","좃","좋까","줫나","줫까","줬까","줬나","종나","지랄","창녀","창년","창놈","챙녀","챙년","챙놈","피싸개","후장","후빨",]
# hateList = ["틀딱", "틀니", "네다틀", "ㄴㄷㅌ", "장애", "정신병", "정박아", "찐따", "찌질이", "전라도", "쌍도", "라도", "5시", "7시", "초졸", "문재앙"]
# genderList = ["한남","한녀","메갈","페미","폐미"]

# # f = open("./ilbe-20210606215622449555.txt", "r")
# f2 = open("./라벨링3.csv", "r")
# f3 = open("./라벨링4.csv", "w")
# lines = f2.readlines()

# for line in lines:
#     line = line.rstrip()
#     if line == ".\t,0\t,0\t,0" or line == "\t,0\t,0\t,0" :
#         pass
#     else: 
#         f3.write(line+"\n")

# f3.close()
# #     if line == "" or line == " " or not line or line == "." or line is None:
# #         pass
# #     c=0
# #     h=0
# #     g=0
# #     for curse in curseList:
# #         if curse in line:
# #             c=1
# #     for hate in hateList:
# #         if hate in line:
# #             h=1
# #     for gender in genderList:
# #         if gender in line:
# #             g=1
# #     f2.write(str.format("{0}|{1}|{2}|{3}\n",line.rstrip(),c,h,g))

# # f.close()
# f2.close()


# curseList = ["갈보", "개년","개새","개쓰레기","거렁뱅이","걸레","개새끼","그지","급식충","김치년","김치녀","구더기","구데기","ㄴㄷㅆ","느개비","느금마","느검마","느개미","느그애비","너검마","느금","니미","나가뒤져","등신","따까리","딸딸이","또라이","똘마니","미친놈","미친년","ㅁㅊㄴ","미친ㄴ","ㅁㅊ년","ㅁㅊ놈","미친새끼","병신","븅신","빙신","ㅄ","ㅂㅅ","벌레새끼","보지","뷰지","ㅂㅈ","빡대가리","병신새끼","븅신새끼","빙신새끼","ㅄ새끼","ㅂㅅ새끼","씨발","ㅆㅂ","시발","ㅅㅂ","시팔","씨팔","십팔","씹","쌍년","썅년","썅놈","쌍놈","ㅆㄴ","아가리","에미","애미","애비","애새끼","앰흑","엠창","엄창","앰창","염병","운지","자지","존나","쥬지","젖","좆","좃","좋까","줫나","줫까","줬까","줬나","종나","지랄","창녀","창년","창놈","챙녀","챙년","챙놈","피싸개","후장","후빨",]
# hateList = ["틀딱", "틀니", "네다틀", "ㄴㄷㅌ", "장애", "정신병", "정박아", "찐따", "찌질이", "전라도", "쌍도", "라도", "5시", "7시", "초졸", "문재앙"]
# genderList = ["한남","한녀","메갈","페미","폐미"]

# f = open("./ilbe-20210606215622449555.txt", "r")
# f2 = open("./라벨링3.csv", "w")
# lines = f.readlines()
# for line in lines:
#     if line == "" or line == " " or not line or line == "." or line is None:
#         pass
#     c=0
#     h=0
#     g=0
#     for curse in curseList:
#         if curse in line:
#             c=1
#     for hate in hateList:
#         if hate in line:
#             h=1
#     for gender in genderList:
#         if gender in line:
#             g=1
#     if "\"" in line:
#         line.replace("\"", "\"\"")

#     if "," in line:    
#         f2.write(str.format("\"{0}\t\",{1}\t,{2}\t,{3}\n",line.rstrip(),c,h,g))
#     else:
#         f2.write(str.format("{0}\t,{1}\t,{2}\t,{3}\n",line.rstrip(),c,h,g))

# f.close()
# f2.close()


f = open("./asdasd.csv", "r")
f2 = open("../labeled/Labeled-2100.txt", "w")

lines = f.readlines()
for line in lines:
    line = line.replace("\"\"", "\"")
    line = line.replace("\t\",", "|")
    line = line.replace("\t,", "|")

    f2.write(line)

f.close()
f2.close()