# pharma-flow

## Propósito geral

- Construção de um ecossistema digital orientado à inovação, concebido para planejar, acompanhar e registrar processos clínicos e fabris em ciclos iterativos.

- Integração entre tecnologia, sustentabilidade e regulação, em consonância com diretrizes internacionais.

📌 Requisitos Funcionais (RF)

- [x] Deve ser possível se cadastrar (pesquisador, gestor ou auditor);

- [x] Deve ser possível se autenticar;

- [x] Deve ser possível obter o perfil de um usuário logado;

- [ ] Deve ser possível registrar, armazenar e versionar dados clínicos e fabris;

- [ ] Deve ser possível consultar trilhas de auditoria das operações realizadas;

- [ ] Deve ser possível aplicar algoritmos de estratificação de pacientes;

- [ ] Deve ser possível detectar outliers em séries temporais de dados clínicos ou fabris;

- [ ] Deve ser possível prever falhas ambientais na linha de produção;

- [ ] Deve ser possível cadastrar e acompanhar indicadores ambientais (como consumo energético por lote e volume de solventes recuperados);

- [ ] Deve ser possível gerar relatórios de sprint que incluam indicadores regulatórios e ambientais;

- [ ] Deve ser possível acessar módulos educacionais interativos sobre boas práticas ambientais;

- [ ] Deve ser possível emitir certificados de conclusão de treinamentos após participação completa.

📌 Regras de Negócio (RN)

- [x] O usuário não deve poder se cadastrar com um e-mail duplicado;

- [ ] Todo acesso ao sistema deve ser registrado em log de auditoria com data, hora e identidade do usuário;

- [ ] Alterações em dados clínicos não podem sobrescrever registros anteriores, apenas criar nova versão;

- [ ] Indicadores ambientais devem ser registrados por lote produzido;

- [ ] Certificados de conclusão de módulos ambientais só podem ser emitidos após 100% de participação;

- [ ] O sistema deve impedir a exclusão definitiva de dados, permitindo apenas arquivamento;

- [ ] O check de conformidade ambiental deve seguir o ciclo PDCA (Plan, Do, Check, Act).

📌 Requisitos Não Funcionais (RNF)

- [ ] Os dados clínicos e fabris devem ser armazenados de forma confiável e persistente;

- [ ] Cada função deve ser acompanhada de análise assintótica de complexidade (notação Big-O) e de suíte de testes unitários com cobertura superior a 80%;

- [ ] O sistema deve operar de acordo com os princípios de Engenharia de Software Ágil, permitindo ciclos iterativos e inspeção contínua;

- [ ] O sistema deve respeitar a conformidade com normas GxP (GLP, GCP, GMP) e requisitos do FDA 21 CFR Part 11;

- [ ] O desempenho deve permitir processamento de dados clínicos e fabris de forma eficiente;

- [ ] Trilhas de auditoria e registros devem ser mantidos de forma imutável.


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

