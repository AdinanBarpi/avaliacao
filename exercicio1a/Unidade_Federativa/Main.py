from Uf import UnidadeFederativa

sigla_estado = input("Escolha uma sigla para descobrir o nome do estado")

if sigla_estado != " ":
    uf = UnidadeFederativa.get_listas_ufs(sigla_estado)
    print("Para a UF {} o nome do estado é {}" .format(sigla_estado , uf))
