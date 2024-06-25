# function
- 어떤 일을 수행하는 코드의 덩어리
- 반복적인 수행을 1회만 작성 후 호출
- 코드를 논리적 단위로 분리
- 캡슐화: 인터페이스만 알면 타인의 코드 활용
- 사용 예시

```
def 함수 이름 (parameter #1, ... , ):
	statements #1
	statements #2
	return return_value
```

- 수학의 함수와 프로그래밍의 함수는 유사함
- parameter : 입력 값 인터페이스
- argument : 실제 파라미터에 입력되는 값


# Console IO
- console 입력 : input()
	- 입력받은 값은 string을 기본으로 받음
- console 출력 : print()
	- print formatting
		- % string
			- "%datatype" % (variable) 형태로 표현
				- %d number, %s String, %f float
		- format 함수
			- "\~~{datatype}~~".format(variable) 형태로 표현
			- \< : 왼쪽 정렬
            - \> : 오른쪽 정렬
            - {}.{} : padding, 표시할 자릿수
		- fstring
			- *< : * 기호로 채우면서 왼쪽 정렬
			- *^ : * 기호로 채우면서 가운데 정렬

