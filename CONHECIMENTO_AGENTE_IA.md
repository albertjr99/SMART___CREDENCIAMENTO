# 🤖 SISTEMA DE IA - CONHECIMENTO DO AGENTE DE ANÁLISE DE DOCUMENTOS

## Versão: 2.0 - Sistema Inteligente de Credenciamento RPPS
## Data: 02/02/2026

---

## 📋 VISÃO GERAL

O agente de IA foi treinado para analisar documentos de credenciamento de instituições financeiras junto a RPPS (Regime Próprio de Previdência Social). O sistema é capaz de substituir análise humana na validação inicial de documentos.

---

## 📄 DOCUMENTOS SUPORTADOS

### 1. 📊 Apresentação Institucional
- **Formatos:** PDF, PPTX
- **O que verificar:**
  - Deve falar sobre a empresa/instituição
  - Deve mencionar o nome da instituição
  - Data não pode ser maior que 1 ano
  - Deve conter: histórico, serviços, equipe, diferenciais
  - NÃO pode ser outro tipo de documento (checklist, termo, certidão)

### 2. ✅ Checklist de Credenciamento
- **Formato:** Excel (.xlsm)
- **O que verificar:**
  - **TODOS os checks devem ser verdes (✓)**
  - **Nenhum X vermelho é permitido** (❌ = rejeição)
  - Todos os campos devem estar preenchidos
  - Observações/diferenciais competitivos devem ser coerentes e substantivas

### 3. 📝 Informações Preenchimento CadPrev
- **Formato:** Excel (.xlsm)
- **Estrutura de cores:**
  - Células **AZUIS** = Perguntas (não precisam ser preenchidas)
  - Células **AMARELAS** = Respostas (DEVEM estar preenchidas)
- **O que verificar:**
  - Todas as células amarelas com resposta
  - Respostas coerentes e relevantes (não placeholders)

### 4. 📋 Formulário Termo de Credenciamento
- **Formato:** Excel (.xlsm)
- **Estrutura de cores:**
  - Células **LARANJA/PÊSSEGO** = Instituição DEVE preencher (OBRIGATÓRIO)
  - Células **BRANCAS** = RPPS preenche (apenas reportar se vazios)
- **Campos do RPPS (não exigir da instituição):**
  - Local e data
  - Responsável pelo credenciamento
  - Número do processo/termo
  - Ente federativo
  - Termo de análise

### 5. 📜 Declaração Unificada
- **Formato:** PDF
- **⚠️ DOCUMENTO CRÍTICO - ASSINATURA OBRIGATÓRIA**
- **O que verificar:**
  - Deve conter texto "DECLARAÇÃO UNIFICADA"
  - Data não pode ser maior que 1 ano
  - **Assinatura digital VÁLIDA é OBRIGATÓRIA**
  - **Assinatura inválida = INVALIDA TODO O CREDENCIAMENTO**

### 6. 📈 Relatório Agência de Risco (Rating)
- **Formato:** PDF
- **O que verificar:**
  - Deve conter termos de rating/risco
  - Deve ter classificação/score/nota (AAA, AA+, brAA, etc.)
  - Deve identificar a agência (Moody's, S&P, Fitch, etc.)
  - Deve mencionar a instituição avaliada

### 7. 🏛️ Certidões
- **Formato:** PDF
- **Tipos:**
  - Formulário de Referência CVM
  - Certidão Autorização Funcionar BACEN
  - Certidão BACEN Sócio/Representante
  - Certidão ANBIMA
  - Lista Exaustiva Resolução CMN
- **O que verificar:**
  - Documento coerente com o tipo esperado
  - Palavras-chave do tipo devem aparecer no documento
  - Formato de certidão oficial

---

## 🔐 REGRAS DE ASSINATURA DIGITAL

### Regra Geral
- Se documento PDF tem assinatura → validar no TCEES → reportar no feedback

### Documentos CRÍTICOS (assinatura inválida = INVALIDA credenciamento)
1. **Declaração Unificada**
2. **Termo de Declaração**

### Outros Documentos
- Assinatura inválida → apenas reportar no feedback
- Não invalida o credenciamento

### Serviço de Validação
- **TCEES** - Tribunal de Contas do Estado do Espírito Santo
- URL: https://conformidadepdf.tcees.tc.br/

---

## 🎨 CÓDIGO DE CORES EXCEL

```
Verde (#92D050, #00B050): ✓ Check - Aprovado
Vermelho (#FF0000, #C00000): ✗ X - Reprovado
Azul (#00B0F0, #0070C0): Perguntas (CadPrev)
Amarelo (#FFFF00, #FFC000): Respostas (CadPrev)
Laranja (#FF6600, #F4B084): Campos obrigatórios instituição (Termo)
Branco (#FFFFFF): Campos para RPPS preencher
```

---

## 📊 SISTEMA DE PONTUAÇÃO

Cada documento recebe um score de 0-100:
- **≥ 60:** Válido
- **50-59:** Válido com ressalvas
- **< 50:** Inválido

### Fatores que aumentam o score:
- ✓ Todas as verificações passam
- ✓ Campos obrigatórios preenchidos
- ✓ Assinatura válida
- ✓ Data dentro da validade
- ✓ Conteúdo coerente e substantivo

### Fatores que reduzem/zeram o score:
- ❌ X vermelho no checklist
- ❌ Campos obrigatórios vazios
- ❌ Assinatura inválida (documentos críticos)
- ❌ Documento errado para o tipo esperado
- ❌ Data muito antiga (> 1 ano)

---

## 🔄 FLUXO DE ANÁLISE

```
1. Documento recebido
    ↓
2. Identificar tipo de documento
    ↓
3. Rotear para analisador especializado
    ↓
4. Aplicar regras específicas do tipo
    ↓
5. Se PDF: Validar assinatura no TCEES
    ↓
6. Calcular score e status
    ↓
7. Gerar feedback detalhado
    ↓
8. Retornar resultado para o sistema
```

---

## 📁 ARQUIVOS DO SISTEMA

| Arquivo | Descrição |
|---------|-----------|
| `ai_document_knowledge.py` | Base de conhecimento do agente |
| `ai_document_analyzer.py` | Motor de análise de documentos |
| `ai_config.py` | Configuração de provedores de IA |
| `tcees_validator.py` | Validador de assinatura digital |
| `rpps_ai_analyzer.py` | Análise especializada para RPPS |

---

## ✅ STATUS DA IMPLEMENTAÇÃO

- [x] Base de conhecimento criada
- [x] Análise de cores no Excel
- [x] Extração de conteúdo Excel para IA
- [x] Validação de assinatura integrada
- [x] Regras críticas de assinatura
- [x] Análise de Apresentação Institucional
- [x] Análise de Checklist
- [x] Análise de CadPrev
- [x] Análise de Termo de Credenciamento
- [x] Análise de Declaração Unificada
- [x] Análise de Relatório de Rating
- [x] Análise de Certidões
- [x] Função principal de roteamento
- [x] Análise combinada IA + regras

---

*Última atualização: 02/02/2026*
