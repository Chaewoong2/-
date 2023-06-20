class NotMatchDormError(Exception):
    # 카카오톡에서 넘어온 dorm_value값이 서버에 dorm_syn 딕셔너리 내에 값들과 매치되지 않을 경우
    def __init__(self):
        super().__init__("서버에 저장된 dorm_syn딕셔너리 안에 dorm_value와 매치되는 값이 없습니다. 카카오톡 오픈빌더 엔티티 동의어 설정과 서버 dorm_syn딕셔너리를 일치시켜 주십시오.")

class NotMatchDateError(Exception):
    # 카카오톡에서 넘어온 date_value값이 서버에 date_syn 딕셔너리 내에 값들과 매치되지 않을 경우
    def __init__(self):
        super().__init__("서버에 저장된 date_syn딕셔너리 안에 date_value와 매치되는 값이 없습니다. 카카오톡 오픈빌더 엔티티 동의어 설정과 서버 date_syn딕셔너리를 일치시켜 주십시오.")
        
class NotMatchTimeError(Exception):
    # 카카오톡에서 넘어온 time_value값이 서버에 time_syn 딕셔너리 내에 값들과 매치되지 않을 경우
    def __init__(self):
        super().__init__("서버에 저장된 time_syn딕셔너리 안에 time_value와 매치되는 값이 없습니다. 카카오톡 오픈빌더 엔티티 동의어 설정과 서버 time_syn딕셔너리를 일치시켜 주십시오.")