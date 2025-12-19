from fastapi import FastAPI
from router.upload_process import router as upload_router
from router.export_files import router as export_router

app = FastAPI(
    title="Embroidery API",
    version="1.0.0"
)

app.include_router(upload_router)
app.include_router(export_router)
    