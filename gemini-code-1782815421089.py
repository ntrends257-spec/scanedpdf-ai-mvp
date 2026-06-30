from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from docling.document_converter import DocumentConverter
import os
import uuid

# Initialize FastAPI
app = FastAPI()

# Add CORS Middleware to allow your frontend to talk to this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the Docling converter
converter = DocumentConverter()

@app.post("/api/convert/structured")
async def convert_and_structure(file: UploadFile):
    # Create a unique ID for the file to prevent conflicts
    file_id = str(uuid.uuid4())
    temp_path = f"{file_id}.pdf"
    
    try:
        # Save uploaded file temporarily
        with open(temp_path, "wb") as f:
            f.write(await file.read())
        
        # Perform layout analysis and conversion
        result = converter.convert(temp_path)
        
        # Return the structured data in Markdown format
        return {"markdown": result.document.export_to_markdown()}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Conversion failed: {str(e)}")
    
    finally:
        # Clean up: delete the file after processing to save server space
        if os.path.exists(temp_path):
            os.remove(temp_path)

@app.get("/health")
def health_check():
    return {"status": "online"}