# Mi enfoque de ingeniería de software e inteligencia artificial

Mi interés está en construir sistemas que resuelvan problemas reales, no en acumular herramientas ni generar código sin comprenderlo. Meridian Research Lab es un espacio donde documento mi forma de pensar, las decisiones de arquitectura y las tecnologías que exploro en mis proyectos.

## Ingeniería de agentes

Trabajo sobre la idea de un agente autónomo que investiga antes de construir. El objetivo es combinar planificación, delegación de subtareas, workers especializados, colas, concurrencia y verificación. Un grafo de dependencias permite controlar cuándo puede ejecutarse cada tarea; un registro de eventos permite explicar qué ocurrió y detectar fallos.

Me interesa integrar servidores MCP y herramientas externas con contratos estructurados, permisos de mínimo privilegio y trazabilidad. Para la ejecución de código, distingo entre un subproceso y un sandbox: el primero administra un proceso, pero no garantiza aislamiento de seguridad. Plataformas como Daytona y E2B son opciones de infraestructura que deben evaluarse según sus límites de ejecución, red, almacenamiento y recursos.

También exploro Vercel AI SDK para integrar modelos, streaming, llamadas a herramientas y respuestas estructuradas, manteniendo el núcleo de negocio independiente de los proveedores.

## Por qué estoy desarrollando y entrenando mi propio asistente de IA

Mi motivación nace del mismo problema que describo en el README: no quiero una IA que genere código automáticamente cuando todavía no comprende la tarea. Quiero investigar cómo enseñarle a reconocer incertidumbre, consultar evidencia, planificar y verificar antes de responder.

He realizado experimentos con un Transformer pequeño desarrollado en PyTorch y tokenización BPE. También he trabajado en el ajuste fino supervisado (SFT) de modelos base de la familia Qwen mediante LoRA. Son dos enfoques diferentes: experimentar con una arquitectura desde cero y adaptar un modelo preentrenado. No afirmo haber preentrenado un modelo fundacional de gran escala.

En mi proceso de investigación trabajo con:

- Datasets versionados y estructurados, deduplicación, revisión de calidad y separación de entrenamiento, validación y prueba para reducir fugas de información.
- Tokenizadores BPE, vocabulario, tokens especiales y análisis de longitud de secuencias. Un tokenizador nuevo no se sustituye sin más en un modelo preentrenado: debe ser compatible con sus embeddings y pesos.
- Arquitecturas Transformer, mecanismos de atención, parámetros entrenables, funciones de pérdida, optimizadores y gradientes.
- Ajuste fino SFT y LoRA; estudio también QLoRA y cuantización para reducir los recursos necesarios.
- Checkpoints, adaptadores, pesos y recuperación de estados de entrenamiento para conservar y comparar experimentos.
- Evaluación mediante conjuntos independientes, pruebas de código, métricas de pérdida y revisión de regresiones. Una pérdida menor no basta para afirmar que el modelo programa mejor.
- Embeddings, búsqueda semántica y RAG como mecanismos externos de recuperación de contexto, distintos del aprendizaje de los pesos.
- Inferencia, ventanas de contexto, consumo de memoria y latencia.

Mi objetivo es desarrollar un ciclo de mejora: evaluar el modelo, detectar debilidades, preparar nuevos ejemplos y ejemplos de repaso, entrenar un candidato y volver a evaluarlo antes de aprobarlo. No presento este ciclo como una automatización terminada, ni doy por certificada una versión solo porque se hayan generado pesos. Parte de los experimentos de entrenamiento se ha realizado; la evaluación comparativa y la validación del comportamiento research-first siguen pendientes.

No publico datasets privados, pesos ni detalles internos innecesarios de mis proyectos en este laboratorio.

## Sistemas empresariales e infraestructura

Me interesa conectar la inteligencia artificial con sistemas de trabajo reales: CRM, ERP, APIs, bases de datos, automatización de procesos y webhooks. Diseño estas integraciones pensando en autenticación, aislamiento por organización, validación de datos, idempotencia, auditoría y recuperación ante fallos.

Mi entorno tecnológico incluye Python, TypeScript, Node.js, React, Next.js, PostgreSQL, Prisma y Supabase, junto con plataformas de despliegue como Vercel y Railway. La elección de una tecnología debe responder al problema, sus restricciones y su coste operativo.

## Calidad sin depender de GitHub Actions

Mi criterio es investigar, implementar, revisar y medir antes de integrar un cambio. Las comprobaciones pueden ejecutarse localmente o en un entorno autorizado sin depender de runners de GitHub Actions.

Para Python, contemplo pruebas con pytest, análisis estático con Ruff, comprobación de tipos con mypy, criterios de aceptación Gherkin y pruebas de mutación cuando aporten valor. Antes de integrar cambios importantes, revisaría dependencias, riesgos, permisos y resultados de pruebas. Estas herramientas representan una estrategia de calidad, no una afirmación de que todas estén configuradas o hayan sido ejecutadas en este repositorio.

## Alcance público

Este laboratorio documenta mis líneas de trabajo sin divulgar código propietario, datos de clientes ni credenciales. Las propuestas, los prototipos y las capacidades validadas se mantienen diferenciados. No pretendo construir una demostración para cada concepto: la documentación también sirve para explicar decisiones, limitaciones y aprendizajes.

Referencias internas: [diseño del runtime autónomo](research-first-agent-runtime.md), [arquitectura de Meridian API](meridian-api-architecture.md) y [MCP y control de herramientas](mcp-context-and-tools.md).
