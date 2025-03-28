from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse,FileResponse
from typing import List
import utils.controver as converter
import os
import yaml
import uuid
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
import io

app = FastAPI()

def load_config():
    config_path = "JMService/utils/config.yml"
    with open(config_path, "r", encoding="utf8") as f:
        return yaml.load(f, Loader=yaml.FullLoader)

def generate_multipart_response(files):
    msg = MIMEMultipart('mixed')
    
    for file_name, file_data in files:
        part = MIMEApplication(
            file_data,
            Name=file_name
        )
        part['Content-Disposition'] = f'attachment; filename="{file_name}"'
        msg.attach(part)
    
    return StreamingResponse(
        iter([msg.as_bytes()]),
        media_type=msg.get_content_type(),
        headers={'Content-Disposition': 'attachment; filename=documents'}
    )

@app.post("/generate-pdfs/")
async def generate_pdfs(jmIds: List[str]):
    config = load_config()
    base_dir = config["dir_rule"]["base_dir"]
    
    try:
        converter.jmIds2PDF(jmIds)
        
        files = []
        for album_id in jmIds:
            pdf_path = os.path.join(base_dir, f"{album_id}.pdf")
            if os.path.exists(pdf_path):
                with open(pdf_path, "rb") as f:
                    files.append((f"{album_id}.pdf", f.read()))
            else:
                print(f"警告:ID {album_id} 转换失败")
        
        return {"status": "completed", "pdf_files": files}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate-pdf/")
async def generate_pdf(jmId: str):
    config = load_config()
    base_dir = config["dir_rule"]["base_dir"]
    
    try:
        converter.jmId2PDF(jmId)
        
        pdf_path = os.path.join(config["dir_rule"]["base_dir"], f"{jmId}.pdf")
        
        return FileResponse(
            pdf_path,
            media_type="application/pdf",
            headers={"Content-Disposition": f"attachment; filename={jmId}.pdf"}
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
