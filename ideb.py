import basedosdados as bd
import matplotlib as plt

# Evolução do ideb no Brasil ano a ano
ideb_ano_brasil = '''
SELECT ano, avg(ideb)
FROM `basedosdados.br_inep_ideb.brasil`
GROUP BY ano
'''

# Evolução do ideb no Brasil ano a ano, comparando a rede pública com a privada
ideb_ano_rede = '''
SELECT ano, rede, avg(ideb) as ideb_medio
FROM `basedosdados.br_inep_ideb.brasil`
GROUP BY ano, rede
HAVING rede = 'publica' or rede = 'privada'
'''

# Evolução do ideb por região
ideb_ano_regiao = '''
SELECT ano, regiao, avg(ideb) as ideb_medio
FROM `basedosdados.br_inep_ideb.regiao`
GROUP BY ano, regiao
'''

evolucao_brasil = bd.read_sql(ideb_ano_brasil, billing_project_id="ps-analytica-a2-416401")
publico_privada_brasilDf = bd.read_sql(ideb_ano_rede, billing_project_id="ps-analytica-a2-416401")
evolucao_regiao = bd.read_sql(ideb_ano_regiao, billing_project_id="ps-analytica-a2-416401")


