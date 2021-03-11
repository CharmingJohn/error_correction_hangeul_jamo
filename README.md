# error_correction_hangeul_jamo
### 한글 자모를 이용한 오류 교정. 검색어 교정
***

입력된 단어를 아스키코드값으로 한글 자모로 나눈 후 difflib 으로 교정.



error_correction.py
~~~python
def correction(call):
  #단어 세트 추가 및 변경
  target = [] #set 원하는 word set 설정
~~~


test.py --word 사삼
