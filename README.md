# 📋 TaskFlow

## Sobre o Projeto

O TaskFlow é um sistema web de gerenciamento de tarefas desenvolvido para a disciplina de Engenharia de Software.

O projeto simula o desenvolvimento de um software para uma startup de logística, utilizando práticas de Engenharia de Software, metodologias ágeis, versionamento de código e integração contínua.

---

## Objetivo

Desenvolver um sistema simples que permita:

- Criar tarefas
- Editar tarefas
- Excluir tarefas
- Marcar tarefas como concluídas
- Definir prioridade das tarefas

---

## Tecnologias Utilizadas

- Python
- Flask
- HTML5
- CSS3
- Git
- GitHub
- GitHub Actions
- Pytest

---

## Metodologia Ágil

Foi utilizada a metodologia Kanban através do GitHub Projects.

O fluxo do projeto foi organizado em três etapas:

- To Do
- In Progress
- Done

Todas as atividades foram controladas pelo quadro Kanban.

---

## Estrutura do Projeto

```
taskflow/

app.py

requirements.txt

src/

templates/

static/

tests/

docs/

.github/
```

---

## Testes Automatizados

Os testes foram implementados utilizando Pytest.

O objetivo foi validar as principais funcionalidades do sistema, como cadastro e exclusão de tarefas.

Todos os testes são executados automaticamente pelo GitHub Actions sempre que ocorre um push para o repositório.

---

## Integração Contínua

O projeto utiliza GitHub Actions para:

- instalar dependências
- executar testes
- validar a aplicação

Essa prática garante maior confiabilidade durante o desenvolvimento.

---

## Mudança de Escopo

Durante o desenvolvimento foi realizada uma alteração no escopo inicialmente definido.

Inicialmente o sistema permitia apenas cadastrar tarefas.

Após uma nova solicitação do cliente foi adicionada a funcionalidade de definição de prioridade das tarefas (Alta, Média e Baixa), permitindo uma melhor organização das atividades.

O quadro Kanban foi atualizado para refletir essa mudança.

---

## Autor

Gustavo Teles

Disciplina: Engenharia de Software

UniFECAF