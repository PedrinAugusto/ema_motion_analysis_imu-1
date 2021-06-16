# Análise Automática do Movimento Humano de Sentar e Levantar

Projeto em desenvolvimento utilizando dados de IMUs do banco de dados [MoVi: A Large Multipurpose Motion and Video Dataset](https://dataverse.scholarsportal.info/dataset.xhtml?persistentId=doi:10.5683/SP2/JRHDRN) para realizar a análise e classificação do movimento de sentar e levantar utilizando dados de aceleração das IMUs. Para a separação dos dados de aceleração referentes apenas ao movimento de sentar e levantar, utilizou-se os dados de vídeo como referência visual para os dados das IMUs que foram sincronizados.

Este trabalho está situado em um projeto maior, [Project EMA website](http://projectema.com), onde a análise de movimento é usada para avaliar os parâmetros de controle do movimento de eletroestimulação em atletas com lesão medular.

O projeto foi realizado de duas maneiras, fazendo a análise do movimento após a aquisição dos dados (offline) e fazendo a análise do movimento durante a aquisição de dados (online). Para o método offline utilizou-se o algoritmo DTW e para o método online utilizou-se o algoritmo IMM. 

# Dependências 

- Numpy (pip install numpy)
- Pandas (pip install pandas)
- Matplotlib (pip install matplotlib)
- Opencv (pip install opencv-python)
- Pykalman (pip install pykalman)
- Math (pip install math)
- Scipy (pip install scipy)
- Pathlib (pip install pathlib)
- Os (pip install os)
- Sys (pip install sys)
- Collections (pip install collections)
- Re (pip install re)
- Fastdtw (pip install fastdtw)
- Dtw (pip install dtw)

