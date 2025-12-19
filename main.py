from fastapi import FastAPI
from router.upload_process import router as upload_router
from router.export_files import router as export_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI(
    title="Embroidery API",
    version="1.0.0"
    
)



# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # allow all frontend origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload_router)
app.include_router(export_router)
    