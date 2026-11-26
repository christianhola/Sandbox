# Mi enfoque de ingeniería de software e inteligencia artificial

Mi interés está en construir sistemas que resuelvan problemas reales, no en acumular herramientas ni generar código sin comprenderlo. Meridian Research Lab es un espacio donde documento mi forma de pensar, las decisiones de arquitectura y las tecnologías que exploro en mis proyectos.

## Ingeniería de agentes

Trabajo sobre la idea de un agente autónomo que investiga antes de construir. El objetivo es combinar planificación, delegación de subtareas, workers especializados, colas, concurrencia y verificación. Un grafo de dependencias permite controlar cuándo puede ejecutarse cada tarea; un registro de eventos permite explicar qué ocurrió y detectar fallos.

Me interesa integrar servidores MCP y herramientas externas con contratos estructurados, permisos de mínimo privilegio y trazabilidad. Para la ejecución de código, distingo entre un subproceso y un sandbox: el primero administra un proceso, pero no garantiza aislamiento de seguridad. Plataformas como Daytona y E2B son opciones de infraestructura que deben evaluarse según sus límites de ejecución, red, almacenamiento y recursos.

También exploro Vercel AI SDK para integrar modelos, streaming, llamadas a herramientas y respuestas estructuradas, manteniendo el núcleo de negocio independiente de los proveedores.

## Ingeniería de modelos

Mi línea de estudio comprende el ciclo de vida de los modelos, desde los datos hasta la inferencia:

- Preparación de datasets, deduplicación, separación de entrenamiento, validación y prueba, y detección de contaminación entre conjuntos.
- Tokenización: vocabulario, segmentación, tokens especiales y algoritmos como BPE.
- Embeddings: representación vectorial, similitud semántica, indexación, recuperación de información y RAG.
- Transformers: atención, capas, parámetros entrenables, funciones de pérdida, optimización y checkpoints.
- Entrenamiento y ajuste fino: diferencias entre preentrenamiento, fine-tuning y técnicas como LoRA; evaluación de generalización y sobreajuste.
- Inferencia: ventanas de contexto, latencia, memoria, cuantización y coste.

Distingo entre investigar estos conceptos, realizar experimentos de pequeña escala y entrenar modelos de producción. La integración de un proveedor de IA no equivale a entrenar un modelo propio; tampoco un checkpoint por sí solo demuestra calidad.

## Sistemas empresariales e infraestructura

Me interesa conectar la inteligencia artificial con sistemas de trabajo reales: CRM, ERP, APIs, bases de datos, automatización de procesos y webhooks. Diseño estas integraciones pensando en autenticación, aislamiento por organización, validación de datos, idempotencia, auditoría y recuperación ante fallos.

Mi entorno tecnológico incluye Python, TypeScript, Node.js, React, Next.js, PostgreSQL, Prisma y Supabase, junto con plataformas de despliegue como Vercel y Railway. La elección de una tecnología debe responder al problema, sus restricciones y su coste operativo.

## Calidad sin depender de GitHub Actions

Mi criterio es investigar, implementar, revisar y medir antes de integrar un cambio. Las comprobaciones pueden ejecutarse localmente o en un entorno autorizado sin depender de runners de GitHub Actions.

Para Python, contemplo pruebas con pytest, análisis estático con Ruff, comprobación de tipos con mypy, criterios de aceptación Gherkin y pruebas de mutación cuando aporten valor. Antes de integrar cambios importantes, revisaría dependencias, riesgos, permisos y resultados de pruebas. Estas herramientas representan una estrategia de calidad, no una afirmación de que todas estén configuradas o hayan sido ejecutadas en este repositorio.

## Alcance público

Este laboratorio documenta mis líneas de trabajo sin divulgar código propietario, datos de clientes ni credenciales. Las propuestas, los prototipos y las capacidades validadas se mantienen diferenciados. No pretendo construir una demostración para cada concepto: la documentación también sirve para explicar decisiones, limitaciones y aprendizajes.

Referencias internas: [diseño del runtime autónomo](research-first-agent-runtime.md), [arquitectura de Meridian API](meridian-api-architecture.md) y [MCP y control de herramientas](mcp-context-and-tools.md).
