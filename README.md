# 마크 모드 언어 번역기

### 주의! 번역기 성능 구림
마크 모드 한국어 번역기  
마크 모드 말고 json value도 번역해줌.  
구글 코랩에서 테스트 함.  
코드가 참 똥 같기에 고인물 유저에게 심심한 사과의 말씀을 드립니다.  
코드만이 아니라 국어 실력도 똥같기에 README.md 가 이해가 안되시면,  
discord: `MakerZip#7772`  
e-mail: <makerzip@hanmail.net>  
로 연락주시면 감사하겠습니다!

## 간단 설명
colab.py => 구글 코랩에 붙여넣기 한 후 사용.  
main.py => 그냥 사용가능  
차이점은 pip 설치랑 파일 경로.  
colab 버전은 파일 경로가 루트(/)경로  
main 버전은 파일 경로가 main.py 파일이 있는 경로  

## 필수 pip
```sh
pip3 install googletrans==3.1.0a0  
```
코랩버전에선 입력할 필요 없이 코드 그대로 복붙하면, 전부 OK

## 실행법
colab 버전은 코랩에서 리눅스 루트경로에 en_us.json 파일을 업로드.  
그 후 코랩에서 실행 후 드라이브를 리로드 하면 ko_kr.json 파일이 뜸.

main 버전은 다운 받은 후 main.py 파일이 있는 경로에 en_us.json 파일을 업로드.  
그 후 
```sh
python3 main.py
```
를 입력하면 코드가 알아서 실행되고, ko_kr.json 파일이 나타남.
