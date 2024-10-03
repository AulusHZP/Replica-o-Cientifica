# Replicação Científica
Este repositório contém os códigos utilizados para a replicação científica da análise CDF dos tamanhos de commits em repositórios GitHub, com base no artigo original sobre o tamanho de arquivos de sites BitTorrent.

## Artigo-base da replicação e análise replicada


O artigo [BitTorrent Traffic from a Caching Perspective](https://doi.org/10.1007/s13173-013-0112-z) apresenta uma análise sobre a distribuição de tamanhos de arquivos em redes peer-to-peer, revelando um padrão de cauda longa, no qual uma minoria de arquivos grandes representa a maior parte do tráfego.

O objetivo da oficina de replicação é replicar essa análise no contexto de um repositório de software, analisando os tamanhos dos commits feitos no repositório de controle de versão tensorflow. Busca-se responder à seguinte pergunta: No repositório tensorflow, uma pequena fração dos commits é responsável pela maior parte do código modificado, seguindo um comportamento de cauda longa semelhante ao observado no tráfego de arquivos em redes BitTorrent?

## Fases da replicação e códigos associados
1.Coletar dados de cada commit feito no repositório. Código analise_commits.py
2.Gerar o gráfico CDF com a mesma lógica (eixos X e Y) do artigo-base. cdf_commits_tensorflow.png

## Dados usados coletados e gerados na replicação
Os resultados da replicação foram materializados na forma de um gráfico CDF que demonstra a distribuição dos tamanhos dos commits no repositório analisado. O gráfico pode ser visualizado no arquivo cdf_commits_tensorflow.png

---
_Áulus Arcanjo Alves Batista_
_Henrique Leite Najar_
_Leonardo de Freitas Viana_
