# pharma-flow

## Propósito geral

- Construção de um ecossistema digital orientado à inovação, concebido para planejar, acompanhar e registrar processos clínicos e fabris em ciclos iterativos.

- Integração entre tecnologia, sustentabilidade e regulação, em consonância com diretrizes internacionais.

📌 Requisitos Funcionais (RF)

- [x] Deve ser possível se cadastrar (pesquisador, gestor ou auditor);

- [x] Deve ser possível se autenticar;

- [x] Deve ser possível obter o perfil de um usuário logado;

- [x] Deve ser possível registrar, armazenar e versionar dados clínicos;

- [x] Deve ser possível registrar, armazenar e versionar dados fabris;

- [x] Deve ser possível consultar trilhas de auditoria das operações realizadas;

- [x] Deve ser possível aplicar algoritmos de estratificação de pacientes;

- [x] Deve ser possível detectar outliers (não se encaixa no padrão) em séries temporais de dados clínicos ou fabris;

- [x] Deve ser possível prever falhas ambientais na linha de produção;

- [x] Deve ser possível cadastrar e acompanhar indicadores ambientais (como consumo energético por lote e volume de solventes recuperados);

- [x] Deve ser possível gerar relatórios de sprint que incluam indicadores regulatórios e ambientais;

- [x] Deve ser possível acessar módulos educacionais interativos sobre boas práticas ambientais;

- [x] Deve ser possível emitir certificados de conclusão de treinamentos após participação completa.

📌 Regras de Negócio (RN)

- [x] O usuário não deve poder se cadastrar com um e-mail duplicado;

- [x] Todo acesso ao sistema deve ser registrado em log de auditoria com data, hora e identidade do usuário;

- [x] Alterações em dados clínicos não podem sobrescrever registros anteriores, apenas criar nova versão;

- [x] Indicadores ambientais devem ser registrados por lote produzido;

- [ ] Certificados de conclusão de módulos ambientais só podem ser emitidos após 100% de participação;

- [x] O sistema deve impedir a exclusão definitiva de dados, permitindo apenas arquivamento;

- [x] O check de conformidade ambiental deve seguir o ciclo PDCA (Plan, Do, Check, Act).

📌 Requisitos Não Funcionais (RNF)

- [x] Os dados clínicos e fabris devem ser armazenados de forma confiável e persistente;

- [ ] Cada função deve ser acompanhada de análise assintótica de complexidade (notação Big-O) e de suíte de testes unitários com cobertura superior a 80%;

- [x] O sistema deve operar de acordo com os princípios de Engenharia de Software Ágil, permitindo ciclos iterativos e inspeção contínua;

- [x] O sistema deve respeitar a conformidade com normas GxP (GLP, GCP, GMP) e requisitos do FDA 21 CFR Part 11;

- [x] O desempenho deve permitir processamento de dados clínicos e fabris de forma eficiente;

- [x] Trilhas de auditoria e registros devem ser mantidos de forma imutável.