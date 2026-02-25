# 🚀 ATIVAR ANÁLISE INTELIGENTE COM IA

## ⚡ Ativação Rápida (2 minutos)

### Passo 1: Execute o configurador
```powershell
py configure_openai.py
```

### Passo 2: Siga as instruções na tela
- Cole sua chave da API OpenAI quando solicitado
- O sistema testa automaticamente se está funcionando
- Configuração salva em `.env`

### Passo 3: Reinicie o servidor
```powershell
# Pressione Ctrl+C para parar o servidor atual
py app.py
```

### ✅ Pronto! 
Agora a análise avançada com GPT-4 está ativa.

---

## 📊 Diferença na Prática

### ❌ SEM IA AVANÇADA (análise básica):
```
⚠️ Análise avançada com IA não disponível
✅ Documento válido
📊 Pontuação: 50/100
```
**Problema:** Aceita documentos errados!

### ✅ COM IA AVANÇADA (GPT-4):
```
🧠 Análise realizada com IA Avançada (GPT-4)
❌ Documento Rejeitado
🚫 Motivo: Documento enviado é um "Termo de Credenciamento", 
não uma "Apresentação Institucional". O sistema detectou 
que o tipo de documento está incorreto.
📊 Pontuação: 0/100
```
**Resultado:** Detecta e rejeita documentos inadequados!

---

## 💰 Custos

- **Custo por documento:** ~R$ 0,30
- **50 documentos/mês:** ~R$ 15,00
- **Modelo:** GPT-4 (mais preciso)

---

## 🔑 Onde conseguir a chave da API?

1. Acesse: https://platform.openai.com/api-keys
2. Crie conta ou faça login
3. Clique em "Create new secret key"
4. Copie a chave (começa com `sk-...`)

---

## ❓ Perguntas Frequentes

**Q: O sistema funciona sem a IA?**
A: Sim, mas com precisão MUITO reduzida. A análise básica não consegue detectar documentos do tipo errado.

**Q: Preciso pagar?**
A: Sim, a OpenAI cobra por uso. Mas é barato (~R$ 0,30 por documento).

**Q: Posso testar grátis?**
A: Sim! A OpenAI dá $5 de crédito grátis para novos usuários. Isso permite testar ~16 documentos.

**Q: É seguro?**
A: Sim. A chave fica salva localmente no arquivo `.env` e não é compartilhada.

---

## 🛠️ Solução de Problemas

### "Chave inválida"
- Verifique se copiou a chave completa
- A chave deve começar com `sk-`

### "Sem créditos"
- Adicione créditos em: https://platform.openai.com/account/billing

### "IA ainda não ativa"
- Reinicie o servidor Flask (Ctrl+C e `py app.py`)
- Verifique se o arquivo `.env` foi criado

---

## 🎯 Resultado Esperado

Após configurar, ao enviar um documento:

✅ O sistema detecta se é o tipo correto
✅ Verifica se fala da instituição certa  
✅ Rejeita documentos genéricos ou de outros assuntos
✅ Fornece feedback detalhado dos problemas

**Exemplo real:** Se você enviar um "Termo de Credenciamento" dizendo que é "Apresentação Institucional", o sistema vai REJEITAR e explicar o erro!
