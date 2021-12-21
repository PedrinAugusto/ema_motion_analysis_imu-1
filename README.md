# Análise Automática do Movimento Humano de Sentar e Levantar

Projeto em desenvolvimento utilizando dados de IMUs do banco de dados [MoVi: A Large Multipurpose Motion and Video Dataset](https://dataverse.scholarsportal.info/dataset.xhtml?persistentId=doi:10.5683/SP2/JRHDRN) para realizar a análise e classificação do movimento de sentar e levantar utilizando dados de aceleração das IMUs. Para a separação dos dados de aceleração referentes apenas ao movimento de sentar e levantar, utilizou-se os dados de vídeo como referência visual para os dados das IMUs que foram sincronizados. A imagem a seguir demonstra alguns exemplos de voluntários sentados, utilizando diferentes assentos. 


<p align="center">
  <img src="https://github.com/lara-unb/ema_motion_analysis_imu/blob/master/images/Tipos%20de%20cadeiras.png?raw=true" alt="Tipos de cadeiras"/>
</p>


Os dados de aceleração foram convertidos em dados de ângulos, de forma que a figura a seguir apresenta os dados de inclinação do tronco em relação à fase do movimento. 


<p align="center">
  <img src="https://github.com/lara-unb/ema_motion_analysis_imu/blob/master/images/Fases_movimento_com_desenhos.png?raw=true" alt="Grafico e fase do movimento"/>
</p>


Este trabalho está situado em um projeto maior, [Project EMA website](http://projectema.com), onde a análise de movimento é usada para avaliar os parâmetros de controle do movimento de eletroestimulação em atletas com lesão medular.

O projeto foi realizado de duas maneiras, fazendo a análise do movimento após a aquisição dos dados (offline) e fazendo a análise do movimento durante a aquisição de dados (online). Para o método offline utilizou-se o algoritmo DTW e para o método online utilizou-se o algoritmo IMM, que realiza o chaveamento de modelos de filtros de Kalman por Cadeia de Markov. 

# Dependências 

Uma opção de rápida instalação das dependências é utilizando o arquivo requiriments.txt com o seguinta comando: 

~~~Python

pip install -r requiriments.txt

~~~

Outra possibilidade é criando um [ambiente virtual](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/), para utilizar as importações sem interferir nas do sistema. Dessa forma é criado um ambiente novo onde é instaladas as bibliotecas para esse projeto

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

