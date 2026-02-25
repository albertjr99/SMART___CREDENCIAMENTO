# 🏛️ Sistema de Credenciamento RPPS - Versão Web

Sistema web completo para credenciamento de instituições financeiras junto aos Regimes Próprios de Previdência Social (RPPS).

## 🚀 Funcionalidades

### Para Instituições Financeiras:
- ✅ Criar processos de credenciamento (Gestor, Administrador, Distribuidor)
- 📤 Upload de documentos em PDF
- 🔍 Análise automática de documentos
- 🔐 Validação de assinatura digital via TCE-ES
- 📊 Acompanhamento do status do processo

### Para RPPS:
- 📋 Visualizar todos os processos recebidos
- 🔍 Análise detalhada de documentos
- ✅ Aprovar ou rejeitar credenciamentos
- 📝 Adicionar pareceres técnicos
- 📦 Arquivar processos finalizados
- 🗑️ Excluir processos arquivados

## 📋 Requisitos

- Python 3.8 ou superior
- Navegador web moderno

## 🔧 Instalação

1. **Clone ou acesse o diretório do projeto:**
```bash
cd "C:\Users\Computador\OneDrive\Desktop\Sistema de Credenciamento\SISTEMA_WEB_PYTHON"
```

2. **Crie um ambiente virtual (recomendado):**
```bash
python -m venv venv
```

3. **Ative o ambiente virtual:**
```bash
# Windows
venv\Scripts\activate
```

4. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

## ▶️ Executar o Sistema

```bash
python app.py
```

O sistema estará disponível em: **http://localhost:5000**

## 🔑 Credenciais de Teste

### RPPS (Análise de Credenciamento)
- **Email:** rpps@teste.com
- **Senha:** rpps123

### Instituição Financeira (Solicitação de Credenciamento)
- **Email:** financeira@teste.com
- **Senha:** financeira123

## 🎯 Como Usar

### Fluxo Completo:

1. **Instituição Financeira:**
   - Faça login com a conta de instituição financeira
   - Clique em "Novo Credenciamento"
   - Selecione o tipo (Gestor, Administrador ou Distribuidor)
   - Faça upload dos documentos necessários
   - O sistema analisará automaticamente cada documento
   - Validação de assinatura será feita no site do TCE-ES
   - Quando todos os documentos estiverem enviados, clique em "Enviar para Análise"

2. **RPPS:**
   - Faça login com a conta RPPS
   - Visualize todos os processos recebidos
   - Clique em um processo para ver os detalhes
   - Analise todos os documentos e suas validações
   - Adicione um parecer técnico
   - Aprove ou rejeite o credenciamento
   - Arquive processos finalizados

## 🔐 Validação de Assinatura Digital

O sistema integra com o site do TCE-ES (Tribunal de Contas do Estado do Espírito Santo) para validar assinaturas digitais em documentos PDF:

- Verifica se o documento possui assinatura digital
- Valida a autenticidade da assinatura
- Verifica a integridade do documento
- Extrai informações técnicas do PDF

## 📁 Estrutura do Projeto

```
SISTEMA_WEB_PYTHON/
│
├── app.py                      # Aplicação Flask principal
├── requirements.txt            # Dependências Python
├── README.md                   # Este arquivo
│
├── templates/                  # Templates HTML
│   ├── base.html              # Template base
│   ├── login.html             # Página de login
│   ├── register.html          # Página de cadastro
│   ├── financial_home.html    # Home da instituição financeira
│   ├── financial_new_process.html   # Novo processo
│   ├── financial_process_detail.html # Detalhes do processo
│   ├── rpps_home.html         # Home do RPPS
│   └── rpps_process_detail.html # Análise do processo
│
├── uploads/                    # Arquivos enviados (criado automaticamente)
└── credenciamento.db          # Banco de dados SQLite (criado automaticamente)
```

## 🛠️ Tecnologias Utilizadas

- **Backend:** Flask (Python)
- **Banco de Dados:** SQLite
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **Validação PDF:** PyPDF2
- **Web Scraping:** BeautifulSoup4, Requests
- **Segurança:** Werkzeug (hash de senhas)

## 🔄 Diferenças da Versão Mobile

Esta é uma adaptação completa do aplicativo React Native original para a web:

### Removido:
- ❌ Módulo de treinamento (não fazia sentido)
- ❌ Dependências React Native/Expo
- ❌ AsyncStorage (substituído por SQLite)

### Melhorado:
- ✅ Validação de assinatura real via TCE-ES
- ✅ Banco de dados persistente (SQLite)
- ✅ Interface web responsiva e moderna
- ✅ Análise de documentos mais robusta
- ✅ Sistema de arquivamento de processos

## 🌐 Deploy

### PythonAnywhere:

1. Crie uma conta em [www.pythonanywhere.com](https://www.pythonanywhere.com)
2. Faça upload dos arquivos do projeto
3. Configure um novo Web App (Flask)
4. Instale as dependências no console virtual
5. Configure o WSGI file para apontar para `app.py`
6. Reload o web app

### Heroku:

1. Crie um arquivo `Procfile`:
```
web: python app.py
```

2. Ajuste o `app.py` para usar porta do Heroku:
```python
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
```

3. Deploy via Git:
```bash
heroku create nome-do-app
git push heroku main
```

## 📞 Suporte

Para dúvidas ou problemas, verifique:
- Se todas as dependências estão instaladas
- Se a porta 5000 está disponível
- Se o Python 3.8+ está instalado
- Se tem permissão para criar arquivos no diretório

## 📄 Licença

Este é um sistema desenvolvido para uso em RPPS (Regimes Próprios de Previdência Social) para gestão de credenciamento de instituições financeiras.

---

**Desenvolvido com 💙 para revolucionar a gestão de investimentos em RPPS**
