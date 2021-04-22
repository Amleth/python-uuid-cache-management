from cachemanagement import Cache

mon_cache = Cache("fichier-cache.yaml")

uuid_chanson_1 = mon_cache.get_uuid(["chansons", "chanson_0001"], True)
uuid_compositeur_1 = mon_cache.get_uuid(["compositeurs", "compositeur_01"], True)

mon_cache.bye()