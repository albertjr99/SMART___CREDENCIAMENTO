# Configuração da Análise Inteligente com IA (GPT-4)

## 📋 O que foi implementado

O sistema agora possui duas camadas de análise:

### 1️⃣ **Análise Básica (Sempre ativa)**
- Verificação de estrutura dos documentos
- Extração e validação de datas
- Contagem de campos preenchidos
- Verificações de formato

### 2️⃣ **Análise Avançada com GPT-4 (Requer configuração)**
- ✅ Análise semântica profunda do conteúdo
- ✅ Verificação se o documento trata do assunto correto
- ✅ Validação se menciona a instituição correta
- ✅ Detecção de informações rasas ou genéricas
- ✅ Análise de completude e coerência informacional
- ✅ Identificação inteligente de problemas

## 🔑 Como Configurar a API OpenAI (Opcional mas Recomendado)

### Passo 1: Obter API Key da OpenAI

1. Acesse: https://platform.openai.com/api-keys
2. Crie uma conta ou faça login
3. Clique em "Create new secret key"
4. Copie a chave gerada

### Passo 2: Configurar no Sistema

**Opção A: Variável de Ambiente (Recomendado)**

No Windows PowerShell:
```powershell
$env:OPENAI_API_KEY = "sua-chave-aqui"
```

Para tornar permanente, adicione nas variáveis de ambiente do sistema:
1. Painel de Controle → Sistema → Configurações Avançadas
2. Variáveis de Ambiente
3. Nova variável do sistema:
   - Nome: `OPENAI_API_KEY`
   - Valor: sua chave da OpenAI

**Opção B: Arquivo .env**

Crie um arquivo `.env` na pasta SISTEMA_WEB_PYTHON:
```
OPENAI_API_KEY=sua-chave-aqui
```

### Passo 3: Reiniciar o Sistema

Após configurar a chave, reinicie o servidor Flask para a IA avançada funcionar.

## 🎯 Como Funciona

### COM API OpenAI Configurada:
- 🧠 GPT-4 analisa profundamente cada documento
- 🎯 Identifica problemas específicos de conteúdo
- 📊 Fornece score detalhado (0-100)
- ✍️ Gera resumo da análise
- 🚫 Rejeita documentos inadequados

### SEM API OpenAI:
- ⚙️ Usa análise baseada em regras
- ✅ Verificações básicas funcionam
- ⚠️ Menos preciso na detecção de problemas de conteúdo
- 💰 Gratuito (sem custos de API)

## 💰 Custos Estimados

- Modelo usado: **GPT-4**
- Custo aproximado: **$0.03 por 1K tokens**
- Análise média por documento: **~2000 tokens**
- Custo por documento: **~$0.06 (R$ 0,30)**

Para uso moderado (50 documentos/mês): **~R$ 15,00/mês**

## 🔍 Como Saber se a IA Está Ativa

Na análise do documento, procure por:
- 🧠 "Análise realizada com IA Avançada (GPT-4)"

Se aparecer apenas:
- ⚠️ "Análise avançada com IA não disponível - usando análise básica"

Significa que a API não está configurada.

## 🛠️ Solução de Problemas

### Erro: "API OpenAI não configurada"
- Verifique se a variável de ambiente está definida
- Reinicie o servidor Flask
- Verifique se a chave está correta

### Erro: "Rate limit exceeded"
- Você excedeu o limite de requisições
- Aguarde alguns minutos
- Considere upgrade no plano OpenAI

### Erro: "Invalid API key"
- A chave está incorreta ou expirada
- Gere uma nova chave no painel OpenAI

## 📊 Diferença nas Análises

### Exemplo com IA Básica:
```
⚠️ A apresentação não parece mencionar a instituição
⚠️ Não foi possível identificar a data
Pontuação: 40/100
```

### Exemplo com IA Avançada (GPT-4):
```
❌ Documento Rejeitado
🚫 Motivo: O documento apresentado não é uma apresentação institucional 
da empresa "XYZ Investimentos". O conteúdo trata de relatório trimestral 
de resultados, não de apresentação da empresa. Além disso, não há informações 
sobre histórico, serviços, diferenciais competitivos ou dados institucionais 
relevantes para credenciamento junto ao RPPS.

📊 Pontuação: 15/100
🧠 Análise realizada com IA Avançada (GPT-4)

Problemas identificados:
❌ Tipo de documento incorreto (não é apresentação institucional)
❌ Ausência de informações institucionais relevantes
❌ Conteúdo não adequado ao propósito de credenciamento
```

## 🎓 Conclusão

A configuração da API OpenAI é **opcional**, mas **altamente recomendada** para:
- ✅ Análises mais precisas
- ✅ Melhor detecção de problemas
- ✅ Feedback mais detalhado
- ✅ Economia de tempo na revisão manual

**O sistema funciona perfeitamente sem a API**, mas com precisão reduzida na análise de conteúdo.
