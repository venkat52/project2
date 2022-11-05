import json , pickle
import numpy as np
# from sklearn.linear_model import _base


__data_column = None 
__locations= None
__model = None
def get_prediction(location , sqft,bath ,bhk):
    get_index()
    arr = np.zeros(len(__data_column))
    loc_index=-1
    for i in range(len(__data_column)):
        if __data_column[i]==location:
            loc_index=i
            break
    loc_indexs = np.where(__data_column==location)
    print(loc_indexs,loc_index,arr[loc_indexs])
    # return "FAS"
    
    arr[0]=sqft 
    arr[1]=bath 
    arr[2]=bhk 
    arr[loc_index]=1
    arr.reshape(1,-1)
    # print(loc_index,'asd',arr[loc_index],type(location),location)
    if loc_index==-1:
        # print(location,loc_index)
        # print(2)
        return "Enter a valid Address"
    # print(arr,len(arr),len(__data_column))
    return round(abs(__model.predict(arr.reshape(1,-1))[0]),2)
def get_index():
    global __data_column 
    global __locations
    global __model
    # C:\Users\VENKATESH\Desktop\ML_realstate_project\server\columns.json
    with open("columns.json","r") as f:
        __data_column = json.load(f)['data_columns']
        __locations = __data_column[3:]

    with open("bengaluru_home_price.pickle","rb") as f:
        # try:
        __model = pickle.load(f)
        

    
if __name__=='__main__':
    print("reading")
    

