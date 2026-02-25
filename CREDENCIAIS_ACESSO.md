# 🔑 CREDENCIAIS DE ACESSO - Sistema de Credenciamento RPPS

## 🌐 Acesso ao Sistema

**URL Local:** http://localhost:5000

**URL Rede Local:** http://192.168.0.125:5000

---

## 👥 PERFIS DE ACESSO

### 1️⃣ RPPS (Regime Próprio de Previdência Social)
**Função:** Análise e aprovação de credenciamentos

📧 **Email:** `rpps@teste.com`  
🔒 **Senha:** `rpps123`

**Permissões:**
- ✅ Visualizar todos os processos de credenciamento recebidos
- ✅ Analisar documentos e validações de assinatura
- ✅ Aprovar ou rejeitar credenciamentos
- ✅ Adicionar pareceres técnicos
- ✅ Arquivar processos finalizados
- ✅ Excluir processos arquivados permanentemente

---

### 2️⃣ INSTITUIÇÃO FINANCEIRA
**Função:** Solicitação de credenciamento

📧 **Email:** `financeira@teste.com`  
🔒 **Senha:** `financeira123`

**Permissões:**
- ✅ Criar novos processos de credenciamento
- ✅ Fazer upload de documentos (PDF)
- ✅ Visualizar análise automática dos documentos
- ✅ Ver validação de assinatura digital (TCE-ES)
- ✅ Enviar processo completo para análise do RPPS
- ✅ Acompanhar status do credenciamento

---

## 📋 TIPOS DE CREDENCIAMENTO DISPONÍVEIS

1. **Gestor de Recursos**
   - Credenciamento para gestão de investimentos

2. **Administrador**
   - Credenciamento para administração de carteiras

3. **Distribuidor**
   - Credenciamento para distribuição de produtos

---

## 🔐 VALIDAÇÃO DE ASSINATURA DIGITAL

O sistema valida assinaturas digitais através do site do **TCE-ES** (Tribunal de Contas do Espírito Santo).

### Checks de Conformidade Verificados:

✅ **Extensão** - Arquivo em formato PDF  
✅ **Sem senha** - Documento não protegido por senha  
✅ **Tamanho do arquivo** - Até 10MB  
✅ **Tamanho por página** - Dimensões padrão (A5 a A3)  
✅ **Assinado** - Possui assinatura digital  
✅ **Autenticidade** - Assinatura autêntica verificada  
✅ **Integridade** - Documento íntegro e não alterado  
✅ **Pesquisável** - Texto extraível (não apenas imagem)

### Resultado:
- ✅ **CONFORME** - Todas as verificações aprovadas
- ❌ **NÃO CONFORME** - Uma ou mais verificações reprovadas

---

## 🚀 COMO TESTAR O SISTEMA

### Fluxo Completo de Credenciamento:

1. **Login como Instituição Financeira**
   - Acesse: http://localhost:5000
   - Use: financeira@teste.com / financeira123
   
2. **Criar Novo Credenciamento**
   - Clique em "Novo Credenciamento"
   - Selecione o tipo (Gestor, Administrador ou Distribuidor)
   
3. **Enviar Documentos**
   - Faça upload de documentos PDF
   - O sistema analisará automaticamente
   - Validará assinatura digital no TCE-ES
   
4. **Submeter para Análise**
   - Após enviar todos os documentos
   - Clique em "Enviar para Análise do RPPS"
   
5. **Login como RPPS**
   - Faça logout e entre com: rpps@teste.com / rpps123
   
6. **Analisar Processo**
   - Visualize os processos recebidos
   - Clique no processo para ver detalhes
   - Analise todos os documentos
   - Veja os checks de conformidade TCE-ES
   
7. **Decisão Final**
   - Adicione um parecer técnico
   - Aprove ou rejeite o credenciamento
   
8. **Arquivamento (Opcional)**
   - Processos finalizados podem ser arquivados
   - Processos arquivados podem ser restaurados ou excluídos

---

## 📱 INFORMAÇÕES TÉCNICAS

**Backend:** Flask (Python 3.8+)  
**Banco de Dados:** SQLite  
**Validação:** TCE-ES API  
**Análise PDF:** PyPDF2  

**Porta:** 5000  
**Debug Mode:** Ativo (apenas desenvolvimento)

---

## ⚠️ OBSERVAÇÕES IMPORTANTES

1. **Documentos em PDF:** Apenas arquivos PDF são aceitos
2. **Assinatura Digital:** Documentos devem ter assinatura digital válida
3. **Tamanho Máximo:** 50MB por arquivo (backend) / 10MB recomendado (TCE-ES)
4. **Validação Online:** Requer conexão com internet para validar no TCE-ES
5. **Modo Offline:** Sistema faz validação local se TCE-ES não responder

---

## 🆘 PROBLEMAS COMUNS

**Não consigo fazer login:**
- Verifique se digitou corretamente o email e senha
- Use as credenciais exatas mostradas acima (case-sensitive)

**Upload de documento falha:**
- Verifique se é um arquivo PDF válido
- Verifique o tamanho do arquivo (máx 50MB)
- Certifique-se que o PDF não está corrompido

**Validação de assinatura offline:**
- Normal se não tiver internet
- Normal se site TCE-ES estiver indisponível
- Sistema faz análise local do documento

---

**Sistema desenvolvido para RPPS - Gestão de Credenciamento de Instituições Financeiras** 🏛️
