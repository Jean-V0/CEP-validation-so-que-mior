async def salvar_cache(cache: dict):
    return

async def ler_cache():
    return 

def carregar_cache() -> dict:
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            cache = json.load(f)
        print(f"Cache carregado: {len(cache):,} CEPs ja consultados.")
        return cache
    return {}


def salvar_cache(cache: dict):
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)