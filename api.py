from fastapi import FastAPI, File, UploadFile, HTTPException
import pandas as pd
import json

app = FastAPI()



@app.post("/top_product")
async def top_product(file: UploadFile = File(...), name_column: str ='', rating_column: str = ''):
    if file.content_type not in ["text/csv", "application/vnd.ms-excel"]:
        raise HTTPException(400, detail="Invalid data type")
    try:
        data = pd.read_csv(file.file)
        if (name_column not in data.columns or rating_column not in data.columns):
            raise HTTPException(404, detail="Entered columns are not found in the data")
        if (data.empty):
            raise HTTPException(404, detail="Empty file - There is no data")
        data = data.sort_values(by=[rating_column], ascending=False, kind='quicksort')
        data = data.to_json(orient = "records")
        products = json.loads(data)
        top_product_list = []
        for p in products:
            if(products[0][rating_column] != p[rating_column] and products[1]==p):
                break
            top_product_list.append({"top_product": p[name_column], "product_rating": p[rating_column]})
        top_product = json.dumps(top_product_list)
        top_product = json.loads(top_product)
        return top_product
    except pd.errors.EmptyDataError:
        raise HTTPException(404, detail="Invalid data")
