from sunpy.net import hek2vso
h2v = hek2vso.H2VClient()
vso_results = h2v.translate_and_query(result[0])
h2v.vso_client.get(vso_results[0]).wait()