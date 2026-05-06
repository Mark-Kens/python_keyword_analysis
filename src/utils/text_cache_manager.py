from pathlib import Path
def cache_file_exists(cache_file_path):
    return Path(cache_file_path).exists()
def read_cached_text(cache_file_path):
    return Path(cache_file_path).read_text(encoding="utf-8")
def write_cached_text(cache_file_path, text):
    cache_file_path = Path(cache_file_path)
    cache_file_path.parent.mkdir(parents=True, exist_ok=True)
    cache_file_path.write_text(text, encoding="utf-8")