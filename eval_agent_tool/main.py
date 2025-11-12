from fastapi import FastAPI, UploadFile, Form, HTTPException
from fastapi.responses import JSONResponse
import pandas as pd
from io import BytesIO
from datetime import datetime, timezone

from file_handling import upload_file_to_gcs

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
         # Reset the cursor to 0 before pandas reads it
        # excel_data.seek(0) 
        # Process the Excel file using pandas
        df = pd.read_excel(excel_data)
        
        # Example of processing: get column names and first few rows
        columns = list(df.columns)
        preview = df.head().to_dict(orient="records")

        # Log or use the additional request body data
        print(f"Received data for user_id: {user_id}, description: {description}")

        job_id = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
        print(f"Generated job ID: {job_id}")
        destination_blob_name = f"{job_id}/input_{file.filename}"
        excel_data_gcs = BytesIO(file_bytes)
        await upload_file_to_gcs(file, excel_data_gcs, destination_blob_name)

        return JSONResponse(
            status_code=200,
            content={
                "message": f"Successfully processed file: {file.filename}",
                "user_id": user_id,
                "description": description,
                "columns": columns,
                "preview": preview,
                "job_id": job_id,
                "gcs_path": destination_blob_name
            }
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {e}")
