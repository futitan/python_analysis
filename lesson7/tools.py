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