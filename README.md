# pharma-flow

## 1. Requisitos Funcionais

- [ ] O sistema deve permitir registro, armazenamento e versionamento seguro de dados clínicos, laboratoriais e fabris.
- [ ] Deve haver controle de acesso por perfis de usuário (pesquisador, gestor, auditor, etc.).
- [ ] O sistema deve manter trilhas de auditoria imutáveis de todas as operações.
- [ ] O sistema deve oferecer assinaturas eletrônicas em conformidade com FDA 21 CFR Part 11.
- [ ] Deve incluir módulos de análise de dados clínicos com bibliotecas em Python (machine learning, detecção de outliers, predição de falhas ambientais).
- [ ] O sistema deve registrar indicadores ambientais críticos (ex.: consumo energético, volume de solventes recuperados).
- [ ] Deve gerar relatórios automáticos de conformidade com GxP (GLP, GCP, GMP).
- [ ] Deve oferecer módulos educacionais interativos para capacitação ambiental (ecopedagogia, ética, sustentabilidade).
- [ ] O sistema deve emitir certificados de conclusão para treinamentos realizados na plataforma.
- [ ] Deve haver dashboards de acompanhamento com indicadores de sustentabilidade e métricas de desenvolvimento (velocity, burndown chart).
- [ ] O sistema deve permitir diagnóstico e planos de mitigação ambiental, seguindo o ciclo PDCA.


## 2. Requisitos Não Funcionais

- [ ] O sistema deve garantir integridade e rastreabilidade dos dados.
- [ ] Deve utilizar autenticação criptográfica para acessos e assinaturas.
- [ ] A plataforma deve ser modular e escalável, suportando evolução incremental.
- [ ] O desempenho dos algoritmos deve ser analisado em complexidade Big-O.
- [ ] Testes unitários devem alcançar cobertura mínima de 80%.
- [ ] O sistema deve ser ambientalmente responsável, com foco em reduzir pegada de carbono e riscos de descarte inadequado.


## 📌 Regras de Negócio

- [ ] Conformidade regulatória obrigatória: o sistema só é válido se atender integralmente às normas GxP e FDA 21 CFR Part 11.
- [ ] Rastreabilidade total: nenhuma operação pode ser registrada sem trilha de auditoria imutável.
- [ ] Segurança de dados: apenas usuários autorizados, com autenticação criptográfica, podem acessar dados sensíveis.
- [ ] Educação ambiental obrigatória: todos os colaboradores devem realizar treinamentos disponíveis na plataforma e obter certificação.
- [ ] Medição de sustentabilidade contínua: cada sprint e ciclo produtivo deve registrar indicadores ambientais (emissões evitadas, economia de recursos).
- [ ] Validação de algoritmos: qualquer modelo de machine learning só pode ser liberado após análise de desempenho e aprovação regulatória.
- [ ] PDCA obrigatório: planos ambientais só serão aceitos se seguirem as etapas do ciclo Plan, Do, Check, Act.
- [ ] Cobertura de testes: nenhuma funcionalidade pode ser homologada se não tiver pelo menos 80% de cobertura em testes unitários.
- [ ] Backlog integrado: requisitos regulatórios e ambientais devem estar presentes no backlog e ser revisados a cada sprint.
- [ ] Relatórios de conformidade e sustentabilidade devem ser entregues a cada iteração, como parte obrigatória do processo ágil.


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

