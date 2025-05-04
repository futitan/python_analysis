# BMI 計算公式
#__name__== '__main__'----> 主要執行檔
def get_ststus(bmi:float):  #(bmi:float) 為參數
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
    print(f"狀態:{status}")

def main():
    height:int = int(input("請輸入身高公分"))
    weight:int = int(input("請輸入體重公斤"))
    BMI = round(weight/pow(height/100,2),1)

    print(f"身高:{height}""cm")
    print(f"體重:{weight}""kg")
    print(f"BMI:{BMI}")
    get_ststus(BMI)  #(BMI)引數值(真正的值)

    
if __name__== '__main__':
    main()

    