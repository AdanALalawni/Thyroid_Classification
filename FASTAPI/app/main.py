from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# load model
model=joblib.load('app/classifer.pkl')
 # creat an intace of Fastapi
app=FastAPI()
# create body of requset 
class InputData(BaseModel):
     age:int  
     sex:int  
     on_1hyroxine:int  
     query_on_1hyroxin:int  
     on_an1i1hyroid_medica1ion:int  
     sick:int  
     pregnan1:int 
     col_1hyroid_surgery:int  
     I131_1rea1men1:int 
     query_hypo1hyroid:int  
     query_hyper1hyroid:int 
     li1hium:int  
     goi1re:int  
     col_1umor:int 
     hypopi1ui1ary:int  
     psych:int  
     col_1SH_measured:int  
     TSH:float
     col_13_measured :int  
     T3:float
     col_114_measured:int 
     TT4:float
     col_14U_measured :int 
     T4U:float
     col_01I_measured:int  
     FTI:float
@app.get("/")
def root():
     return{"welcome!"}
@app.post('/predict')
def predict(requst:InputData):
     data=np.array([[requst.age,
                     requst.sex,
                     requst.on_1hyroxine,
                     requst.query_on_1hyroxin,
                     requst.on_an1i1hyroid_medica1ion,
                     requst.sick,
                     requst.pregnan1,
                     requst.col_1hyroid_surgery,
                     requst.I131_1rea1men1,
                     requst.query_hypo1hyroid,
                     requst.query_hyper1hyroid,
                     requst.li1hium,
                     requst.goi1re,
                     requst.col_1umor,
                     requst.hypopi1ui1ary,
                     requst.psych,
                     requst.col_1SH_measured,
                     requst.TSH,
                     requst.col_13_measured,
                     requst.T3,
                     requst.col_114_measured,
                     requst.TT4,
                     requst.col_14U_measured,
                     requst.T4U,
                     requst.col_01I_measured,
                     requst.FTI]])
     pred=model.predict(data)
     spices_map={0:'Normal',1:'Sick'}
     return {"predictions":spices_map[int(pred[0])]}
