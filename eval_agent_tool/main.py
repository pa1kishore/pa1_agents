from fastapi import FastAPI, UploadFile, Form, HTTPException
from fastapi.responses import JSONResponse
import pandas as pd
from io import BytesIO

app = FastAPI()

@app.post("/upload-excel/")
async def upload_excel(file: UploadFile, user_id: str = Form(...), description: str = Form(...)):
    """
    Accepts an Excel file and additional form data (user_id and description).
    """
    if file.content_type not in ["application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", "application/vnd.ms-excel"]:
        raise HTTPException(status_code=400, detail="Invalid file type. Only Excel files are allowed.")

    try:
        # Read the file content into a BytesIO buffer
        file_bytes = await file.read()
        excel_data = BytesIO(file_bytes)
        
        # Process the Excel file using pandas
        df = pd.read_excel(excel_data)
        
        # Example of processing: get column names and first few rows
        columns = list(df.columns)
        preview = df.head().to_dict(orient="records")

        # Log or use the additional request body data
        print(f"Received data for user_id: {user_id}, description: {description}")

        return JSONResponse(
            status_code=200,
            content={
                "message": f"Successfully processed file: {file.filename}",
                "user_id": user_id,
                "description": description,
                "columns": columns,
                "preview": preview
            }
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {e}")
