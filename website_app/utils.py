import pandas as pd
from rank_bm25 import BM25Okapi
from .models import MovieData

_maindata_df = None # Use underscore to indicate internal module variable
_bm25_model = None  # Use underscore to indicate internal module variable

def get_loaded_data():
    global _maindata_df, _bm25_model
    if _maindata_df is None or _bm25_model is None:
        print("[website_app/utils.py] Attempting to load movie data and BM25 model...")
        if MovieData.objects.exists():
            _maindata_df = pd.DataFrame(list(MovieData.objects.all().values()))
            _bm25_model = BM25Okapi(_maindata_df['tags'].apply(lambda x: x.lower().split()))
            print("[website_app/utils.py] Movie data and BM25 model loaded successfully.")
            print(f"[website_app/utils.py] _maindata_df shape after load: {_maindata_df.shape if _maindata_df is not None else 'N/A'}")
            print(f"[website_app/utils.py] _bm25_model type after load: {type(_bm25_model)}")
            print("[website_app/utils.py] First 5 rows of _maindata_df:\n", _maindata_df.head())
        else:
            print("[website_app/utils.py] No movie data found in DB, BM25 model not initialized.")
    else:
        print("[website_app/utils.py] Movie data and BM25 model already loaded (from previous request in this process).")
    return _maindata_df, _bm25_model 