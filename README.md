# pharma-flow

## Requisitos Funcionais (o sistema deve fazer)

- **Gestão de Estudos Clínicos**
    - [ ]  Cadastro de protocolos, pacientes, profissionais e centros de pesquisa.
    - [ ]  Registro de dados clínicos com versionamento e trilha de auditoria.
    - [ ]  Monitoramento em tempo real de métricas de eficácia, segurança e eventos adversos.
    - [ ]  Estratificação de pacientes com algoritmos de machine learning.
- **Gestão da Produção Farmacêutica**
    - [ ]  Planejamento e rastreabilidade da cadeia produtiva (matéria-prima → produto final).
    - [ ]  Controle de lotes, datas de validade e cadeia de frio.
    - [ ]  Indicadores ambientais: consumo de energia, água, solventes e reciclagem.
- **Segurança e Conformidade**
    - [ ]  Autenticação multifator.
    - [ ]  Assinatura eletrônica compatível com **FDA 21 CFR Part 11**.
    - [ ]  Controle de acesso baseado em papéis (RBAC).
    - [ ]  Trilhas de auditoria imutáveis de todas as operações.
- **Educação Ambiental**
    - [ ]  Módulo de cursos multimodais (texto, vídeo, quizzes).
    - [ ]  Registro de participação e emissão automática de certificados.
    - [ ]  Relatórios de impacto ambiental aplicados a cada processo.
- **Integração e Processamento**
    - [ ]  APIs para integração com sistemas legados.
    - [ ]  Biblioteca Python para análise de dados biomédicos (estatística, ML).
    - [ ]  Dashboards interativos para indicadores clínicos e ambientais.

---

## 2. Requisitos Não Funcionais 

- [ ]  **Performance:** processamento de séries temporais biomédicas em tempo real.
- [ ]  **Disponibilidade:** uptime mínimo de 99,9% em ambiente validado.
- [ ]  **Escalabilidade:** suporte a múltiplos estudos clínicos e plantas produtivas.
- [ ]  **Confiabilidade:** testes unitários e de integração com cobertura > 80%.
- [ ]  **Usabilidade:** interface responsiva, acessível (WCAG 2.1).
- [ ]  **Sustentabilidade:** otimização de recursos computacionais e relatórios de impacto ambiental.

---

## 3. Regras de Negócio

- [ ]  Todos os dados de pacientes devem ser **anonimizados** conforme LGPD/GDPR.
- [ ]  Alterações em registros clínicos ou produtivos **não podem sobrescrever dados anteriores**, apenas criar versões.
- [ ]  Cada usuário deve possuir **papel definido** (ex.: pesquisador, auditor, gestor, operador fabril).
- [ ]  O sistema **não deve permitir exclusão física de registros** (apenas inativação).
- [ ]  Cada estudo clínico precisa ser **associado a um protocolo aprovado por comitê de ética**.
- Certificados de conclusão de cursos ambientais só podem ser emitidos após:
    - [ ]  ≥ 70% de presença nas aulas.
    - [ ]  ≥ 60% de acertos nas avaliações.
- [ ]  Indicadores ambientais devem ser **registrados e auditados** a cada ciclo de produção.
- [ ]  Qualquer integração com sistemas legados deve registrar impacto ambiental positivo (redução de consumo, resíduos ou emissões).
- [ ]  Todo algoritmo preditivo usado em estratificação clínica deve ser acompanhado de **relatório de acurácia e limitações**.
- [ ]  Dados e logs devem ser armazenados por, no mínimo, **15 anos**, conforme normas de pesquisa clínica.


pharma-flow/
│
├── docs/                     # Documentação do projeto (ABNT, manuais, diagramas)
├── config/                   # Configurações globais (YAML, JSON, .env)
│   ├── settings.py
│   └── logging.conf
│
├── src/                      # Código-fonte principal
│   ├── core/                 # Núcleo (domínio e regras de negócio)
│   │   ├── entities/         # Entidades de negócio (Paciente, Estudo, Lote)
│   │   ├── services/         # Casos de uso / lógica de aplicação
│   │   └── validators/       # Regras de validação
│   │
│   ├── clinical/             # Módulo de gestão de pesquisa clínica
│   │   ├── models/           # Modelos de dados (ORM, schemas)
│   │   ├── ml/               # Algoritmos de machine learning
│   │   ├── pipelines/        # ETL, pré-processamento de dados
│   │   └── api/              # Endpoints da API para clínica
│   │
│   ├── manufacturing/        # Módulo de gestão fabril
│   │   ├── models/
│   │   ├── monitoring/       # Indicadores ambientais e fabris
│   │   └── api/
│   │
│   ├── education/            # Módulo de educação ambiental
│   │   ├── content/          # Materiais multimodais
│   │   └── certificates/     # Emissão de certificados
│   │
│   ├── shared/               # Recursos compartilhados
│   │   ├── utils/            # Funções auxiliares
│   │   ├── security/         # Autenticação, criptografia
│   │   └── database/         # Conexão com bancos de dados
│   │
│   └── app.py                # Ponto de entrada da aplicação
│
├── tests/                    # Testes unitários e de integração
│   ├── clinical/
│   ├── manufacturing/
│   └── education/
│
├── scripts/                  # Scripts auxiliares (migrações, ETL, devops)
│
├── requirements.txt          # Dependências do projeto
├── pyproject.toml            # Configuração (poetry/pipenv)
├── setup.py                  # Caso o projeto seja empacotado
├── README.md                 # Descrição do projeto
└── .gitignore

