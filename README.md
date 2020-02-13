# SimpleLoginPrg
<다음과 같은 조건들을 참고하여 회원 가입 및 로그인 프로그램을 작성하시오>

1) 프로그램 시작 후 다음과 같은 메시지가 출력되어 1, 2, 3 중 하나의 값을 입력 받도록 한다.

2) 1을 선택하면 ID, Password, Name, School의 4가지 정보를 입력받아 파일에 저장하는 프로그램을 작성한다.

    2-1) 입력된 내용은 access.txt 라는 이름의 텍스트 파일 내에 저장된다.

    2-2) access.txt 파일의 각 라인에는 가입된 회원 각각의 정보가 "[id]: [password], [name], [school]" 형태로 저장된다.

    2-3) 즉, 가입 회원이 10명이면 access.txt 파일 내에 라인 수도 정확히 10개이다.

    2-4) 암호화 방식은 sha 모듈을 활용한다. sha 모듈 활용 방법은 본 문제의 마지막에 제시된 sha 활용 예를 참고한다. 즉, access.txt 파일 내에     password 정보는 암호화 되어 저장되어야 한다.

    2-5) 회원 정보를 입력 받을 때 id를 입력 받은 직후 access.txt를 확인하여 이미 존재하는 id가 입력되었다면 다음 메시지를 출력하고 id 정보를 다시 입력받는다. Sorry, the entered ID is already used.

3) 2를 선택하면 ID, Password의 2가지 정보를 입력받는 프로그램을 작성한다.

    3-1) 입력된 ID 정보가 access.txt에 존재하지 않으면 다음과 같은 메시지를 출력하고 다시 입력받는다.

    Sorry, you are not a registered member.

    3-2) 입력된 ID가 올바르게 존재하지만 Password 정보가 access.txt 파일에 있는 정보와 불일치하면 다음과 같은 메시지를 출력하고 Password를 다시 입력받는다.

    Sorry, the entered password is not correct.

    이 때에도 사용자가 입력한 Password 정보와 함께 sha 모듈이 활용되어야 한다.

    3-3) 입력된 ID와 Password가 모두 올바르면 다음과 같은 메시지를 출력한다.

    Hello [name]!

    위 [name]에는 access.txt에 기록되어 있는 name 정보를 출력한다.

4) 3을 선택하면 프로그램이 끝난다.
