# BMI 計算公式
#__name__== '__main__'----> 主要執行檔 ，__
def get_ststus(bmi:float)->str:  #(bmi:float) 為參數 ，->str 為return 出type ，可省略
    if bmi < 18.5:
        status = "體重過輕"
    elif bmi < 24:
        status = "正常"
    elif bmi < 27:
        status = "過重"
    elif bmi < 30:
        status = "輕度肥胖"
    elif bmi <35:
        status = "中度肥胖"
    else:
        status = "重度肥胖"
    #print(f"狀態:{status}") #不要在FUNCTION 列印，表結果傳出來用return
    return status 

def get_bmi(w:int,h:int)->float:
    return round(w/pow(h/100,2),1)

def main():
    height:int = int(input("請輸入身高公分"))
    weight:int = int(input("請輸入體重公斤"))
   # BMI:float = round(weight/pow(height/100,2),1)
    BMI:float =get_bmi(weight,height)

    print(f"身高:{height}""cm")
    print(f"體重:{weight}""kg")
    print(f"BMI:{BMI}")
    #get_ststus(BMI)  #(BMI)引數值(真正的值)
    status:str=get_ststus(BMI)  #(BMI)引數值(真正的值)，改寫return 要有接收
    print(f"狀態:{status}")
    
if __name__== '__main__':
    main()

    