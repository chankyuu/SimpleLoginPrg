import hashlib
import string

def signUp() :                                                        # 회원가입 함수
    s = []                                                            # 최종적으로 파일에 쓰여질 리스트
    i = 0
    while(True) :                                                     # 입력받은 ID를 검사하는 반복문
        f = open("access.txt", 'r+')                                  # access.txt 파일을 읽고 쓰기 가능한 모드로 오픈한다.
        check_id = 0                                                  # 이미 존재하는 id가 있는지 체크하기 위한 변수
        id = input("Press your ID : ")
        for line in f :                                               # 파일 f에서 한 줄씩 읽은 후, ':'로 나누면 첫 번째 원소가 ID이기 때문에
            check = line.split(":")[0]
            if(id in check) :                                         # 같은 ID가 존재하는지 확인한다.
                print("Sorry, the entered ID is already used.")
                check_id = 1
                break;
        if(check_id == 0) :                                           # 같은 ID가 존재하지 않으면 빈 리스트 s에 추가한다.
            s.append(id)
            break;
    while(True) :                                                     # 패스워드를 입력하는 반복문
        password = input("Press your Password : ")
        if(password != '') :                                          # 패스워드가 공백문자가 아니면 리스트 s에 추가한다.
            s.append(password)
            break
        else :
            print("Sorry, the entered Password is wrong.")
    name = input("Press your Name : ")                                # 이름과 학교를 리스트 s에 추가한다.
    s.append(name)
    school = input("Press your School : ")
    s.append(school)

    for i in range(len(s)) :                                          # 모든 정보가 입력되어있는 리스트 s를 문제에서 주어진대로 file에 입력한다.
        f.write('[')
        if(i == 1) :
            password_encrypted = hashlib.sha1(s[1].encode('utf-8')).hexdigest() # 패스워드는 hashlib 모듈을 이용하여 암호화한 후 파일에 저장한다.
            f.write(password_encrypted)
        else :
            f.write(s[i])
        f.write(']')
        if(i == 0) :
            f.write(':')
        else :
            if(i != 3) :
                f.write(',')
    f.write("\n")
    f.close()

def loginPrg() :                                                       # 로그인 함수
    f = open("access.txt", "r+")                                       # "access.txt" 를 읽고 쓰기 가능한 모드로 오픈한다.
    info = f.readlines()
    for i in range(len(info)) :                                        # 파일을 한 줄씩 읽어와 구두문자를 없앤 후 순수 정보들만으로 구성된 리스트 생성
        info[i] = info[i].replace("\n","")                             # 과제3 10번 문제를 응용하였다.
        for j in range(len(string.punctuation)) :
            info[i] = info[i].replace(string.punctuation[j]," ")
    for i in range(len(info)) :
        info[i] = info[i].split()
    while(True) :                                                      # 올바른 회원정보인지 판단하는 반복문
        s = input("Press your ID : ")
        for i in range(len(info)) :                                    # 입력받은 ID가 회원정보로 등록되어 있으면
            if(s in info[i][0]) :                                      # 그 ID에 맞는 비밀번호를 확인한다.
                while(True) :                                          # 그렇지 않다면 등록되어 있지 않은 회원정보임을 알린다.
                    s = input("Press your Password : ")                # 비밀번호가 맞을 때까지 입력받는다.
                    s = hashlib.sha1(s.encode('utf-8')).hexdigest()    # 입력받은 비밀번호를 역시 암호화하여 비교한다.
                    if (s not in info[i][1]):
                     print("Sorry, the entered password is not correct.")
                    else:
                        print("Hello {0}!".format(info[i][2]))
                        return 0
        print("Sorry, you are not a registered member.")
    f.close()

while(True) :                                                           # 기본 출력 반복문
    print("Welcom to Our Service")
    print("1. Sign Up")
    print("2. Sign In")
    print("3. Quit")

    n = input()
    if(n == "1") :
        signUp()
    elif(n == "2") :
        loginPrg()
    elif(n == "3") :
        break;