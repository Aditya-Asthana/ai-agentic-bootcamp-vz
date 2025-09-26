from datetime import datetime
import json
from ibm_watsonx_orchestrate.agent_builder.tools import tool, ToolPermission
import requests


# get data from openapi

GET_DATA_API_URL = (
    "https://vzbootcampnj-bootcamp.apps.68d14ea9ba8368133c0b353a.am1.techzone.ibm.com"
)


@tool(
    name="get_data_tool",
    description="Fetches data from the /data endpoint of the FastAPI server.",
    permission=ToolPermission.ADMIN,
)
def get_data_tool() -> str:
    """
    Calls the /data endpoint and returns the response as a string.
    """
    try:
        response = requests.get(f"{GET_DATA_API_URL}/data", timeout=5)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return f"API call failed: {str(e)}"
