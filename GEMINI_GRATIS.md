# 🆓 Configuração Rápida - Google Gemini (GRATUITO)

## ⚡ 3 Passos Simples (5 minutos)

### Passo 1: Obter API Key do Gemini (GRÁTIS)

1. Acesse: **https://makersuite.google.com/app/apikey**
2. Faça login com sua conta Google
3. Clique em **"Create API Key"**
4. Copie a chave gerada (algo como: `AIzaSy...`)

### Passo 2: Criar arquivo `.env`

Crie um arquivo chamado `.env` na pasta `SISTEMA_WEB_PYTHON` com este conteúdo:

```env
GEMINI_API_KEY=AIzaSy_sua_chave_aqui
AI_PROVIDER=gemini
```

**Substitua** `AIzaSy_sua_chave_aqui` pela sua chave real.

### Passo 3: Reiniciar o servidor

No terminal onde está rodando o Flask:
1. Pressione **Ctrl+C** para parar
2. Execute: `py app.py`

## ✅ Pronto!

A IA avançada está ativa e **100% GRATUITA**!

---

## 🎯 Como Testar

1. Envie um documento **errado de propósito**:
   - Tipo: "Apresentação Institucional"
   - Arquivo: Um termo de credenciamento

2. O sistema vai **REJEITAR** e explicar:
   ```
   ❌ Documento Rejeitado
   🚫 Motivo: Documento enviado é 'Termo de Credenciamento',
   não 'Apresentação Institucional'
   ```

---

## 💰 Limites Gratuitos do Gemini

- ✅ **60 requisições por minuto**
- ✅ **Sem custo** (completamente gratuito)
- ✅ **Sem necessidade de cartão**

Perfeito para desenvolvimento e testes!

---

## 🔄 Atualizar para GPT-4 depois?

Quando quiser mais precisão, execute:
```bash
py setup_ai.py
```

E configure OpenAI GPT-4 (mais preciso, mas pago).

---

## ❓ Problemas?

**Erro ao criar .env?**
- Crie um arquivo de texto novo
- Salve como `.env` (com o ponto)
- Cole o conteúdo acima

**Chave não funciona?**
- Verifique se copiou completa
- Sem espaços antes/depois
- Use a chave que começa com `AIzaSy`

**Gemini não está ativo?**
- Confirme que reiniciou o servidor
- Veja se o arquivo `.env` está na pasta correta
- Deve estar em: `SISTEMA_WEB_PYTHON\.env`
