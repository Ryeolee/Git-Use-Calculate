
def div(a,b): # 나눗셈 원근 
    if(b!=0):
        return a/b

def mul(a,b):  #곱셈 승렬
    return a*b



def run():  
    while True:
        print("메뉴\n1.덧셈\n2.뺄셈\n3.나눗셈\n4.곱셈\n5.종료")  
        menu=int(input("메뉴 선택>>>"))
        
        if(menu==1):
            a,b=map(int,input("두 정수 입력:").split())
            print("%d + %d = %d"%(a,b,add(a,b)))  
            
        elif(menu==2):
            a,b=map(int,input("두 정수 입력:").split())
            print("%d - %d = %d"%(a,b,sub(a,b))) 
            
        elif(menu==3):
            a,b=map(int,input("두 정수 입력:").split())
            if(b==0):
                print("0으로 나눌 수 없습니다.")  
            else:
                print("%d / %d = %0.2f"%(a,b,div(a,b)))  
                
        elif(menu==4):
            a,b=map(int,input("두 정수 입력:").split())
            print("%d * %d = %d"%(a,b,mul(a,b))) 
    
            
        elif(menu==5):  
            print("종료")
            break
