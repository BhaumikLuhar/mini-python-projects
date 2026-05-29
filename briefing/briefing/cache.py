import json
from textwrap import indent
import time
from pathlib import Path
from typing import Any

from briefing.config import CACHE_DIR

def cache_path(name: str)-> Path:
    return CACHE_DIR / f"{name}.json"

def is_cache_fresh(timestamp:float, ttl_seconds:int)-> bool:
    age=time.time()-timestamp

    return age<ttl_seconds

def load_cache(name:str, ttl_seconds:int)->dict[str, Any] | None:
    
    path=cache_path(name)

    if not path.exists():
        return None
    
    try:
        with open(path,"r")as f:
            payload=json.load(f)

        timestamp=payload["timestamp"]

        if not is_cache_fresh(timestamp, ttl_seconds):
            return None
        
        return payload["data"]

    except (
        json.JSONDecodeError,
        KeyError,
        OSError,
    ):
        return None
    

def save_cache(name:str, data:dict[str, Any])->None:
    CACHE_DIR.mkdir(exist_ok=True)

    path=cache_path(name)

    payload={
        "timestamp": time.time(),
        "data":data,
    }

    with open(path,"w")as f:
        json.dump(payload,f,indent=4)


        