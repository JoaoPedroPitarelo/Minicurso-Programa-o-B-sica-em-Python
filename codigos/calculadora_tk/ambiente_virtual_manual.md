Este é um arquivo em formato MarkDown, caso esteja abrindo pelo VSCode, instale a extensão [MarkDown Preview Enhanced](https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced) e clique no ícone de leitura no canto superior direito para ter uma melhor experiência de leitura.


## Manual de criação do ambiente virtual Python
## (Windows e Linux)

**OBS**: Esse manual se destina à aqueles que desejam entender melhor porque usar ambientes virtuais em Python e qual sua importância na fase de desenvolvimento. Caso não tenha interesse em saber como funciona pule para a seção [[#Como criar um ambiente virtual Python?]]

---

### O que é um ambiente virtual em Python?

Um ambiente virtual em Python é como se fosse um "caixinha isolada" onde você instala bibliotecas e pacotes python somente para aquele projeto que se esta desenvolvendo. Esse recurso é extremamente importante pois caso você instale todos os pacotes no Python "Geral", sem o ambiente virtual, da sua máquina a chance de conflito de versões de pacotes é grande, pois não é possível ter duas versões diferentes rodando juntas no mesmo lugar.

**Exemplo dessa problemática:**
* Projeto A precisa do biblioteca X na versão 3.2
* Projeto B precisa dessa mesma biblioteca X na versão 4.0
* No seu computador está instalado somente a versão 4.0
* **Resultado: O projeto A NÃO funcionará pois há conflito de versões de dependências, que nesse exemplo é a biblioteca X.**

---

### Como um ambiente virtual funciona?

Tecnicamente, um ambiente virtual em Python (venv, virtualenv, uv, etc.) não é como uma máquina virtual ou Docker. Ele é basicamente, e de forma bem resumida, um diretório dentro que do seu projeto que contém:

* **Um interpretador Python "clonado" ou "linkado"**
	* A venv cria uma cópia (ou link) do executável python dentro da pasta do ambiente.
	* Quando você ativa o ambiente, seu terminal passa a usar esse executável específico em vez do Python global da sua máquina.
	
* **Um diretório de pacotes separado**
	* A venv cria um diretório próprio de pacotes dentro dele `(venv/lib/.../site-packages)`
	* Assim, quando você instala algo como pip, com o ambiente virtual ativado, os pacotes vão para esse diretório isolado e não para o do sistema `(C:\Users\usuario\AppData\Local\Programs\Python\Python313\...\site-packages)`
	
* **Alteração de variáveis de ambiente**
	* Ao realizar a instalação do Python, seja Windows ou Linux, o sistema operacional adiciona às variáveis de ambiente o executável Python e seus pacotes para que seja possível o acesso pelo terminal.
	* Ao ativar o ambiente virtual, com `.\venv\Scripts\Activate.ps1` para Windows ou `source venv/bin/activate` para sistemas Linux, o script muda essa variáveis de ambiente para  que apontem primeiramente para o binário da venv e não do sistema, realizando assim o isolamento citado.

---

### Como criar um ambiente virtual Python?

###

#### Para Windows (PowerShell):
```
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install pyside6
```

**OBS:** No PowerShell, por padrão, ele não permite a execução de scripts externos, caso de ERRO nos comandos acima basta executar esse comando no seu terminal:
`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

Esse comando irá permitir a execução de scripts externos somente para seu usuário

###

#### Para sistemas Linux (bash, zsh)
```
# Caso não esteja instalado (Substitua X pela versão instalada em sua máquina)
sudo apt install python3.X-venv

python3 -m venv venv
source ./venv/bin/activate
pip install pyside6
```
