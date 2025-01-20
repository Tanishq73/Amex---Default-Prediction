from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import rasterio
from rasterio.io import MemoryFile
from fastapi.responses import StreamingResponse
import requests
from io import BytesIO

import pandas

app = FastAPI()

# Define request parameters model
class COGRequest(BaseModel):
    url: str
    bbox: list[float]  # [minX, minY, maxX, maxY]

@app.post("/fetch-cog-tile")
async def fetch_cog_tile(request: COGRequest):
    """
    Fetches the requested tile from the COG using REST API.
    """
    try:
        # Extract parameters
        cog_url = request.url
        bbox = request.bbox

        if len(bbox) != 4:
            raise HTTPException(status_code=400, detail="Invalid bounding box format. Provide [minX, minY, maxX, maxY].")

        # Fetch the COG file via HTTP
        response = requests.get(cog_url, stream=True)
        if response.status_code != 200:
            raise HTTPException(status_code=404, detail=f"Unable to fetch the COG from the provided URL: {cog_url}")

        # Load the COG into a Rasterio MemoryFile
        with MemoryFile(response.content) as memfile:
            with memfile.open() as src:
                # Ensure the bbox is within the image bounds
                window = rasterio.windows.from_bounds(*bbox, src.transform)
                data = src.read(window=window)

                # Serialize the data to bytes
                output = BytesIO()
                with rasterio.open(
                    output,
                    "w",
                    driver="GTiff",
                    height=data.shape[1],
                    width=data.shape[2],
                    count=src.count,
                    dtype=data.dtype,
                    crs=src.crs,
                    transform=rasterio.windows.transform(window, src.transform),
                ) as dst:
                    dst.write(data)

                output.seek(0)
                return StreamingResponse(output, media_type="image/tiff")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing COG: {str(e)}")
