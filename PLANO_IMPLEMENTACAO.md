# PLANO DE IMPLEMENTAÇÃO - SISTEMA DE CREDENCIAMENTO

## ✅ CONCLUÍDO

### 1. Migração do Banco de Dados
- ✅ Campos adicionados em `users`:
  - entity_id (ID da instituição/RPPS)
  - is_active (usuário ativo/inativo)
  - reset_token (token para redefinição de senha)
  - reset_token_expires (expiração do token)
  - last_login (último acesso)
  - user_number (número do usuário 1-5 na entidade)

- ✅ Campos adicionados em `processes`:
  - is_authorized (processo autorizado pelo RPPS)
  - authorized_by (ID do usuário que autorizou)
  - authorized_at (data/hora da autorização)
  - ai_pre_analysis (JSON com análise prévia da IF)
  - ai_full_analysis (JSON com análise completa do RPPS)
  - ai_analysis_date (data da análise)

- ✅ Campos adicionados em `documents`:
  - has_signature (documento tem assinatura digital)
  - signature_valid (assinatura é válida)
  - signature_info (JSON com informações do certificado)

## 🔨 EM DESENVOLVIMENTO

### 2. Portal Administrativo - Gerenciar Usuários

#### Funcionalidades Necessárias:
1. **Lista de Entidades (RPPS e IFs)**
   - Ver todas as instituições cadastradas
   - Filtrar por tipo (RPPS/Financial)
   - Buscar por nome

2. **Gerenciar Usuários de uma Entidade**
   - Listar os 5 slots de usuários
   - Adicionar novo usuário (até 5 por entidade)
   - Editar usuário existente
   - Desativar/Reativar usuário
   - Gerar token de redefinição de senha
   - Visualizar último acesso

3. **Rotas API Necessárias:**
```python
GET  /api/admin/entities              # Listar todas entidades
GET  /api/admin/entity/<id>/users     # Listar usuários de uma entidade
POST /api/admin/entity/<id>/users     # Criar novo usuário
PUT  /api/admin/users/<id>            # Atualizar usuário
POST /api/admin/users/<id>/reset-token  # Gerar token de redefinição
DELETE /api/admin/users/<id>          # Desativar usuário
```

### 3. Sistema de Autorização IF → RPPS

#### Fluxo:
1. IF cria processo e escolhe RPPS de destino
2. RPPS recebe notificação de novo processo NÃO AUTORIZADO
3. RPPS vê modal perguntando se reconhece a IF e o processo
4. Para autorizar, deve:
   - Confirmar que conhece a IF
   - Inserir sua senha de usuário
   - Clicar em "Autorizar Processo"
5. Processo muda status para AUTORIZADO
6. IF pode ver que processo foi autorizado

#### Implementação:
- ✅ Campo `is_authorized` em processes
- ⏳ Modal de autorização no portal RPPS
- ⏳ Rota `/api/rpps/authorize-process/<id>`
- ⏳ Badge visual de "Aguardando Autorização"
- ⏳ Notificação para IF quando autorizado

### 4. Personalização dos Portais

#### Mostrar nome da entidade logada:
- Header deve exibir: "Bem-vindo, [Nome da Instituição]"
- Usuário logado: "João Silva (Usuário 1/5)"
- Logo da instituição (se houver)

### 5. Análise de IA dos Documentos

#### 5.1 Pré-Análise no Portal IF
- Botão "Analisar com IA" antes de enviar
- Gemini analisa cada documento
- Retorna: ✅ Válido / ⚠️ Atenção / ❌ Inválido
- Mostra resumo dos achados
- Salva em `ai_pre_analysis`

#### 5.2 Análise Automática no Portal RPPS
- Quando processo chega (status: submitted)
- Análise completa e robusta automaticamente
- Salva em `ai_full_analysis`
- RPPS vê análise detalhada no modal
- Inclui:
  - Validação de cada documento
  - Verificação de assinaturas
  - Conformidade com requisitos
  - Recomendações

### 6. Validação de Assinaturas Digitais

#### Biblioteca: pyHanko ou cryptography
- Verificar certificados ICP-Brasil
- Extrair dados do certificado
- Validar cadeia de certificação
- Verificar validade temporal
- Salvar em `signature_info`

## 📋 PRÓXIMOS PASSOS

1. ⏳ Criar interface admin para gerenciar usuários
2. ⏳ Implementar sistema de tokens de redefinição
3. ⏳ Criar modal de autorização RPPS
4. ⏳ Implementar personalização dos portais
5. ⏳ Adicionar botão de pré-análise IA (IF)
6. ⏳ Implementar análise automática IA (RPPS)
7. ⏳ Validação de assinaturas digitais
8. ⏳ Testes completos do fluxo

## 🎯 ORDEM DE IMPLEMENTAÇÃO

1. **PRIORIDADE 1:** Portal Admin - Gerenciar Usuários
2. **PRIORIDADE 2:** Sistema de Autorização IF→RPPS
3. **PRIORIDADE 3:** Personalização dos Portais
4. **PRIORIDADE 4:** Análise de IA (Pré + Automática)
5. **PRIORIDADE 5:** Validação de Assinaturas
