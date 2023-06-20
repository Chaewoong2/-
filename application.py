from flask import Flask, jsonify, request
import sys
from index import index_df1
from index import index_df2
from index import index_df3
import pprint
from datetime import datetime
from exceptions import NotMatchDormError, NotMatchDateError, NotMatchTimeError

application = Flask(__name__)


# 동의어 사전
dorm_syn = {"본관":{"본관", "개성재"},
      "양성재":{"양성재"},
      "양진재":{"양진재"},}
date_syn = {"오늘":{"오늘"},
      "어제":{"어제"},
      "내일":{"내일"},}
date_to_day = {0:"월요일",
              1:"화요일",
              2:"수요일",
              3:"목요일",
              4:"금요일",
              5:"토요일",
              6:"일요일"}
time_syn = {"아침":{"아침"},
      "점심":{"점심"},
      "저녁":{"저녁"},}

@application.route("/menu1",methods=['POST'])
def Get_function1():
    text = "???"
    try:
        # 카카오톡 오픈빌더에서 전송한 json받기
        param = request.get_json()
        pprint.pprint(param)
        # 받은 json에서 엔티티로 추출해놓은 값들 변수로 받기
        # 1. 건물 (동의어 처리)
        dorm_value = param["action"]["detailParams"]["dorm_name"]["value"]
        print(dorm_value)
        if dorm_value in dorm_syn["본관"]:
            dorm_value = "본관"
        elif dorm_value in dorm_syn["양성재"]:
            dorm_value = "양성재"
        elif dorm_value in dorm_syn["양진재"]:
            dorm_value = "양진재"
        else:
            raise NotMatchDormError
        
        # 2. 날짜 (동의어 처리, 오늘/내일/어제 해당 날짜변환)
        date_value = param["action"]["detailParams"]["sys_date"]["origin"]
        today_value = datetime.today().weekday()
        if date_value in date_syn["오늘"]:
            date_value = date_to_day[today_value]
        elif date_value in date_syn["내일"]:
            date_value = date_to_day[(today_value+1)%7]
        elif date_value in date_syn["어제"]:
            date_value = date_to_day[((today_value-1)+7)%7]
        elif date_value in ["월요일","화요일","수요일","목요일","금요일","토요일","일요일"]:
            date_value = date_value
        else:
            raise NotMatchDateError

        # 3. 시간
        time_value = param["action"]["detailParams"]["time"]["value"]
        if time_value in time_syn["아침"]:
            time_value = "아침"
        elif time_value in time_syn["점심"]:
            time_value = "점심"
        elif time_value in time_syn["저녁"]:
            time_value = "저녁"
        else:
            raise NotMatchTimeError
        
        # 전송할 답변 내용 작성
        if dorm_value == "본관":
            text = index_df1(date_value, time_value)
        elif dorm_value == "양성재":
            text = index_df2(date_value, time_value)
        elif dorm_value == "양진재":
            text = index_df3(date_value, time_value)
        
        
    
    except NotMatchDormError as e:
        print("NotMatchDormError : ", e)
        text = "건물 정보를 입력해 주셔야 합니다"
    except NotMatchDateError as e:
        print("NotMatchDateError : ", e)
        text = "오늘,내일,어제같은 날짜 정보를 입력해 주셔야 합니다"
    except NotMatchTimeError as e:
        print("NotMatchTimeError : ", e)
        text = "아침,점심,저녁같은 시간 정보를 입력해 주셔야 합니다"
    except KeyError as e:
        print("KeyError발생 : 해당 조건에 맞는 식단 정보를 없습니다")
        text = "해당 조건에 맞는 식단 정보를 없습니다"
    
    print(text)
    print(type(text))
    res = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": text
                        }
                    }
                ]
            }
        }
    # 답변 전송
    return jsonify(res)


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=80, debug = True)