import fastapi as FAST_API
import Analyzer
import pandas as pd
app = FAST_API.FastAPI()

@app.get("/")
def basicGet():
    return {"message":"kaam krle poora"}

@app.get("/predict")
def whatTocarry():
    op1Analysis = Analyzer.analyze_payments("12","das")
    data = pd.DataFrame({
    'Service Provider': ['Airtel'],
    'LSA': ['Delhi'],
    'Technology': ['4G'],
    'Test_type': ['Download']
})
    if(op1Analysis=="Digital Payments"):
        op2Analysis = Analyzer.predict_speed(data)
        if(op2Analysis>4):
            return {"response":"Can rely on Digital Payments"}
        else:
            return {"response":"Digital Payments are accepted, but your mobile network network signals are poor!"}
    else:
        return {"response":"Use Cash!"}

    


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8002)