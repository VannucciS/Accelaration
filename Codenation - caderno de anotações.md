# Tipos de aprendizado
* reforço 
* sempre supervisionado
* aprendizado supervisionado - objetivo é aprender a entrada para mostrar as saídas;
	* algoritmo aprenda caracteristicas  dos dados classificados e na saída ele pegue 
		dados não classificados e os classifique.
* aprendizado não supervisionado - o algoritmo descobre padrões nos dados, sem a classificação 
	inicial dos dados.
	
# Papéis dentro de um projeto de dados:

* Gerente de dados - falta no mercado;
* Arquiteto de dados - desenha o projeto de ciência de dados (infra e tecnologia);
* Engenheiro de dados - foco no processo de gestão de dados (etl, manipular massas de dados,
* Decision scientist - ligado a àrea de negócios ( quais projetos vão gerar mais valor);
* Engenheiro de machine learning - 

4 tipos de analise de dados
* solucao descritita - descreve o que existe (olha pra o passado);
* solucao diagnostica - descreve o por quê (olha o passado para explicar o agora);
* solucao preditiva - descreve o que vai acontecer (olha o passado para explicar o futuro);
		* previsão - ancorada no tempo;
		* prediçao - forma genérica de prever;
* solucao prescritiva - recomenda tomada de decisão (recomenda uma ação);

# Tipos de problemas
* classificação binário (uma ou duas classes):
	* regressão logística;
	* Spam ou não?
	
* classificação multiclasse:
	* permitem gerar previsões para várias classes (prever um entre mais de dois resultados)
	* regressão logística multinomial;
	* Isto é um livro, filme ou roupa?
	
* Regressão
	* prever um valor numérico;
	* regressão linear;
	* Qual será o valor de venda de uma casa? Qual a temperatura em Posse?

* Agrupamento / clusterização
	* Modelo aprende grupos / divisão dos dados;
	* retornar um grupo;
	* Kmeans;
	* Quantos perfis de clientes a empresa tem? Quantos grupos de alunos tem na classe?
	
* Sistemas de recomendação
	* modelo sugere / recomenda algo ao usuário;
	* retorna sugestão;
	* Collaborative filtering / Content based;
	* Qual filme recomenda a um usuário de acordo com o seu gosto? E no gosto de pessoas similares?

# Maturidade com analytics

* Maturidade com os dados (como a empresa trabalha os dados)
	* Dados crus - não geram valor s
	* geram informação - mas não de forma automatizada (disperso e não padronizado)
	* BI - clara visão do passado (paineis - etl - data lakes - governança dos dados)
	* Advanced analytics - já trabalha com prediçao