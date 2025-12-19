from pydantic import BaseModel, Field
from typing import List

class EmbroideryStats(BaseModel):

    total_stitches: int = Field(..., alias="totalStitches")
    est_time: str = Field(..., alias="estTime")
    density: float
    thread_colors: List[str] = Field(..., alias="threadColors")
    dimensions: str

    model_config = {
        "populate_by_name": True,        # allows both alias and field name
        "alias_generator": None,
        "json_encoders": {}
    }
