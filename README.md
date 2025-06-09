## Sistema WEB de Registro com frontend, python e MySQL

📋 Sobre o Projeto

Este projeto é um Sistema Web de registro de cartório desenvolvido com o Framework Flask, Frontend HTML5, CSS3 e backend python e MySQL para armazenar os dados. Ele permite cadastrar usuarios, registros e visualizar o ultimo registro de forma intuitiva.

📌 Funcionalidades

 ✅Login de Administrador: Acesso ao painel de registro através de login com credenciais fixas.<br>
 ✅Cadastro de Usuários: Criptografia de senha com bcrypt e armazenamento seguro no banco.<br>
 ✅Registro de Nascimento: Entrada de dados como livro, folha, termo, data de nascimento, nome 
dos pais e etc.<br>
 ✅Exibição de Último Registro: Apresenta o último registro adicionado diretamente na interface.<br>
 ✅Mensagens de Validação: Utiliza flash() para fornecer feedback ao usuário.<br>

📌 Estrutura do Código

O projeto é voltada para a resolução de uma necessidade real, utilizando as tecnologias HTML, CSS, PYTHON, FLASK.

📂 PROJETO UNIFEOB _DESENVOLVIMENTO WEB/<br>
 ├── 📂 Banco de dados/<br>
 │    ├── banco de dados.sql<br>
 ├── 📂 static/<br>
 │    ├── imagens/<br>
 │    │    ├── Minimal Professional Lawyer Firm Justice & Law Logo.png<br>
 │    ├── box.css<br>
 │    ├── registro.css
 <br>├── 📂 templates/<br>
 │    ├── cadastro.html<br>
 │    ├── index.html<br>
 │    ├── registro.html
 <br>├── main.py/<br>
 ├── models.py<br>
 ├── routes.py

📌 Aplicação do Desenvolvimento Web<br>

1️⃣ Front-end (Desenvolvimento do Lado do Cliente)<br>
Definição: É a parte visível de um site ou aplicação, com a qual os usuários interagem diretamente.<br>


📌 Tecnologias: HTML, CSS, JavaScript<br>
📌 Frameworks/Bibliotecas: React, Vue.js, Angular<br>
📌 Responsividade e design são fundamentais.<br>

➡ Benefício: Criação de interfaces intuitivas e responsivas, melhoria da experiência do usuário (UX), permite que o site funcione bem em diferentes dispositivos (mobile, tablet, desktop).<br>

2️⃣ Back-end (Desenvolvimento do Lado do Servidor)<br>
Definição: Lida com a lógica, autenticação, armazenamento e manipulação de dados.<br>

📌 Linguagens: Python, Java, PHP, Node.js<br>
📌 Frameworks:  Flask, Django, Spring Boot, Express.js<br>

➡ Benefício: Garante o funcionamento interno da aplicação, mantém a segurança e o controle de acesso aos dados, possibilita integração com sistemas externos e APIs.<br>

3️⃣ Banco de Dados<br>
Definição: Armazena e organiza os dados da aplicação.<br>

📌 Relacionais: MySQL, PostgreSQL<br>
📌 Não-relacionais:  MongoDB, Firebase<br>

➡ Benefício: Permite o armazenamento estruturado e eficiente de informações, garante recuperação rápida e precisa dos dados, facilita análises e relatórios com base nas informações salvas<br>

📌 Como Executar o Projeto<br><br>
🔹 Pré-requisitos<br><br>
Python 3.13.3<br>
MySQL<br>
Framework Flask<br>
HTML5<br>
CSS3<br>

📋 Conceitos Aplicados

 🔒 Segurança<br>
 • As senhas dos usuários são criptografadas com bcrypt, garantindo a segurança dos dados 
 sensíveis.<br>

 🧠Lógica de Autenticação<br>
 • O login é simples e validado diretamente no back-end.<br>
 • Apenas usuários com a senha correta acessam a área de registros.<br>
 
 💾 Integração com Banco de Dados<br>
 • O sistema interage diretamente com o MySQL para inserir e recuperar dados.<br>
 • Utiliza cursor() e comandos SQL para manipulação das tabelas pessoa, registro e 
cadastro.<br>

🔹 Passo a passo<br>

1️⃣ Clone o repositório<br>
git clone https://github.com/ArthurLimaQz/SISTEMA_WEB_DO_CART-RIO.git<br> 

🧪 Instale as dependências<br>

Abra o terminal e dê o seguinte comando: **pip install -r requirements.txt**<br>

2️⃣ Configure o banco de dados no MySQL Workbench

Abra o MySQL Workbench<br>

Conecte ao seu servidor MySQL (usualmente chamado de “Local instance MySQL”)<br>

Clique em "create a new sql tab for executing queries” (ícone do SQL com um +)<br>

execute o código a seguir<br>

CREATE DATABASE UNIFEOB;<br>
USE UNIFEOB;<br>
CREATE TABLE `cadastro` (<br>
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'Primary Key',<br>
  `registro` varchar(100) DEFAULT NULL,<br>
  `senha` varchar(255) DEFAULT NULL,<br>
  PRIMARY KEY (`id`)<br>
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci,<br>

CREATE TABLE `pessoa` (<br>
  `Id` int NOT NULL AUTO_INCREMENT,<br>
  `NOME` varchar(50) NOT NULL,<br>
  `SEXO` enum('M','F','Outro') NOT NULL,<br>
  `DATA_NASCIMENTO` date DEFAULT NULL,<br>
  `NOME_GENITOR` varchar(50) DEFAULT NULL,<br>
  `NOME_GENITORA` varchar(50) DEFAULT NULL,<br>
  `cadastro_id` int DEFAULT NULL,<br>
  PRIMARY KEY (`Id`),<br>
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci,<br>

CREATE TABLE `registro` (<br>
  `Id` int NOT NULL AUTO_INCREMENT,<br>
  `TERMO` int NOT NULL,<br>
  `LIVRO` varchar(10) NOT NULL,<br>
  `FOLHA` int NOT NULL,<br>
  `DATA_REGISTRO` date DEFAULT NULL,<br>
  `Id_PESSOA` int DEFAULT NULL,<br>
  PRIMARY KEY (`Id`),<br>
  KEY `FK_PESSOA_REGISTRO` (`Id_PESSOA`),<br>
  CONSTRAINT `FK_PESSOA_REGISTRO` FOREIGN KEY (`Id_PESSOA`) REFERENCES `pessoa` (`Id`)<br>
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci,<br>

🔹 Ajuste as configurações em routes.py:<br>

   Endereço do servidor: app.config['MYSQL_HOST'] = 'localhost'<br>
   Usuário do servidor: app.config['MYSQL_USER'] = '(COLOQUE SEU USUÁRIO)'<br>
   Senha do servidor: app.config['MYSQL_PASSWORD'] = '(COLOQUE SUA SENHA)'<br>
   Banco de dados do servidor: app.config['MYSQL_DB']='unifeob' <br>

3️⃣ inicie o arquivo main.py.<br>
copie o Running on http://127.0.0.1:5000<br>
cole no navegador.<br>

📌 Conclusão<br>
Este projeto demonstra uma aplicação web básica com autenticação e persistência de dados. É um 
bom exemplo do uso de Flask com MySQL e pode ser expandido com funcionalidades como 
edição, exclusão de registros e controle de usuários

🚀 Tecnologias utilizadas:
✅ Python com Flask
✅ Banco de Dados MySQL
✅ HTML, CSS

👥 Desenvolvedores<br>
Arthur Lima de Queiroz RA 1012023200044 <br>
Paulo Henrique Esberci RA 1012023200070<br>
vinícius da silva fernandes RA 24001801 <br>
Gabriel Silva Claro Batista RA 1012023200171

