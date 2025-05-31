## Sistema WEB de Registro com frontend, python e MySQL

📋 Sobre o Projeto

Este projeto é um Sistema Web de registro de cartório desenvolvido com o Framework Flask, Frontend HTML5, CSS3 e backend python e MySQL<br>para armazenar os dados. Ele permite cadastrar usuarios, registros e visualizar o ultimo registro de forma intuitiva.

📌 Funcionalidades

 ✅Login de Administrador: Acesso ao painel de registro através de login com credenciais fixas.<br>
 ✅Cadastro de Usuários: Criptografia de senha com bcrypt e armazenamento seguro no banco.<br>
 ✅Registro de Nascimento: Entrada de dados como livro, folha, termo, data de nascimento, nome 
dos pais e etc.<br>
 ✅Exibição de Último Registro: Apresenta o último registro adicionado diretamente na interface.<br>
 ✅Mensagens de Validação: Utiliza flash() para fornecer feedback ao usuário.<br>

📌 Estrutura do Código

O projeto segue os princípios da Programação Orientada a Objetos (POO), aplicando Abstração, Herança, Polimorfismo e Encapsulamento.

📂 src/<br>
 ├── 📂 Controller/<br>
 │    ├── RegistroController.java
 <br>├── 📂 Dao/<br>
 │    ├── RegistroDao.java
 <br>├── 📂 Models/<br>
 │    ├── Pessoa.java<br>
 │    ├── Registro.java<br>
 │    ├── Conexao.java
 <br>├── 📂 View/<br>
 │    ├── RegistroGUI.java<br>
 │    ├── EntradaView.java

📌 Aplicação dos Conceitos de POO

1️⃣ Abstração
Definição: A abstração permite criar classes genéricas que modelam conceitos do mundo real, escondendo detalhes internos e expondo apenas funcionalidades essenciais.

📌 No código: Criamos a classe abstrata Pessoa, que define atributos comuns para qualquer pessoa (nome, data de nascimento, sexo). Essa classe serve como modelo para a classe Registro, garantindo que todas as pessoas cadastradas tenham essas características básicas.

public abstract class Pessoa {
    protected String nome;
    protected LocalDate dataNascimento;
    protected String sexo;

    public Pessoa(String nome, LocalDate dataNascimento, String sexo) {
        this.nome = nome;
        this.dataNascimento = dataNascimento;
        this.sexo = sexo;
    }

    public abstract void exibirInformacoes(); // Método abstrato


➡ Benefício: Permite que outras classes derivem dessa estrutura sem precisar duplicar código.

2️⃣ Herança
Definição: A herança permite que uma classe reutilize atributos e métodos de outra classe.

📌 No código: A classe Registro herda de Pessoa, aproveitando seus atributos e adicionando novas informações específicas, como termo, livro e datas.
public class Registro extends Pessoa {
    private int termo;
    private String livro;
    private int folha;
    private LocalDate dataRegistro;
    private String nomeGenitor;
    private String nomeGenitora;

    public Registro(int termo, String livro, int folha, LocalDate dataRegistro, 
                    String nome, String nomeGenitor, String nomeGenitora, 
                    LocalDate dataNascimento, String sexo) {
        super(nome, dataNascimento, sexo); // Chama o construtor da superclasse (Pessoa)
        this.termo = termo;
        this.livro = livro;
        this.folha = folha;
        this.dataRegistro = dataRegistro;
        this.nomeGenitor = nomeGenitor;
        this.nomeGenitora = nomeGenitora;
    }

➡ Benefício: Evita duplicação de código e mantém uma estrutura organizada.

3️⃣ Polimorfismo
Definição: O polimorfismo permite que um mesmo método funcione de maneira diferente dependendo da classe que o implementa.

📌 No código:

A classe RegistroDao aceita qualquer objeto do tipo Pessoa no método save(), mas só insere no banco se for um Registro.
Isso permite futuras expansões, como o cadastro de outros tipos de pessoas (exemplo: Funcionário, Cliente, etc.).<br>
public void save(Pessoa pessoa) {<br>
    if (pessoa instanceof Registro) {<br>
        Registro registro = (Registro) pessoa;<br>
        String sql = "INSERT INTO registro (termo, livro, folha, data_registro, nome, nome_genitor, nome_genitora, data_nascimento, sexo) " +<br>
                     "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)";

        try (PreparedStatement ps = connection.prepareStatement(sql)) {
            ps.setInt(1, registro.getTermo());
            ps.setString(2, registro.getLivro());
            ps.setInt(3, registro.getFolha());
            ps.setDate(4, java.sql.Date.valueOf(registro.getDataRegistro()));
            ps.setString(5, registro.getNome());
            ps.setString(6, registro.getNomeGenitor());
            ps.setString(7, registro.getNomeGenitora());
            ps.setDate(8, java.sql.Date.valueOf(registro.getDataNascimento()));
            ps.setString(9, registro.getSexo());

            ps.executeUpdate();
            System.out.println("✅ Registro salvo com sucesso!");
        } catch (SQLException ex) {
            ex.printStackTrace();
        }
    }

➡ Benefício: Aumenta a flexibilidade do código, permitindo reutilização e expansão.

4️⃣ Encapsulamento
Definição: O encapsulamento protege os dados dentro das classes, permitindo o acesso somente por meio de métodos específicos.

📌 No código:

Todos os atributos das classes são privados (private).<br>
O acesso aos atributos é feito por métodos get e set, garantindo controle sobre os dados.<br>
public int getTermo() {<br>
    return termo;<br>
}

public String getLivro() {<br>
    return livro;<br>
}

public int getFolha() {<br>
    return folha;<br>
}

public LocalDate getDataRegistro() {
    return dataRegistro;
}
➡ Benefício: Impede alterações indesejadas nos dados e melhora a segurança do sistema.<br>
📌 Como Executar o Projeto<br>
🔹 Pré-requisitos<br>
Java 8+<br>
MySQL<br>
Bibliotecas JDBC<br>
IDE (IntelliJ, VS Code, NetBeans, Eclipse)<br>

🔹 Passo a passo<br>
1️⃣ Clone o repositório<br>
git clone https://github.com/ArthurLimaQz/PROJETO-UNIFEOB.git<br>
inicie o arquivo RegistroGUI

Abra o MySQL Workbench<br>

Conecte ao seu servidor MySQL (usualmente chamado de “Local instance MySQL”)<br>

Clique em "create a new sql tab for executing queries” (ícone do SQL com um +)<br>

execute o código a seguir<br>

2️⃣ Configure o banco de dados MySQL

CREATE DATABASE UNIFEOB;<br>
USE UNIFEOB;<br>
CREATE TABLE PESSOA (<br>
    ID INT PRIMARY KEY AUTO_INCREMENT,<br>
    Nome VARCHAR(50) NOT NULL,<br>
    Sexo ENUM('M', 'F', 'Outro') NOT NULL,<br>
    Data_nascimento DATE,<br>
    Nome_genitor VARCHAR(50),<br>
    Nome_genitora VARCHAR(50)<br>
);<br>
CREATE TABLE REGISTRO (<br>
    ID INT PRIMARY KEY AUTO_INCREMENT,<br>
    Termo INT NOT NULL,<br>
    Livro VARCHAR(10) NOT NULL,<br>
    Folha INT NOT NULL,<br>
    Data_registro DATE NOT NULL,<br>
    Id_Pessoa INT NOT NULL,<br>
    CONSTRAINT FK_PESSOA_REGISTRO FOREIGN KEY (Id_Pessoa) REFERENCES PESSOA(ID) ON DELETE CASCADE<br>
);<br>

3️⃣ Compile e execute a interface gráfica
javac src/View/RegistroGUI.java
java src/View/RegistroGUI

📌 Conclusão
Este projeto implementa os conceitos fundamentais de POO (Programação Orientada a Objetos) em um sistema funcional de registro de cartório.

🚀 Tecnologias utilizadas:
✅ Java com Swing
✅ Banco de Dados MySQL
✅ Arquitetura MVC

ALUNOS:<br>
Arthur Lima de Queiroz RA 1012023200044 <br>
Paulo Henrique Esberci RA 1012023200070<br>
Matheus Ribeiro Ferreira RA 1012023100592<br>
Gabriel Silva Claro Batista RA 1012023200171

