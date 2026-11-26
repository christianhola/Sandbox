# Mi enfoque de ingeniería de software e inteligencia artificial

Mi interés está en construir sistemas que resuelvan problemas reales, no en acumular herramientas ni generar código sin comprenderlo. Meridian Research Lab es un espacio donde documento mi forma de pensar, las decisiones de arquitectura y las tecnologías que exploro en mis proyectos.

## Ingeniería de agentes

Trabajo sobre la idea de un agente autónomo que investiga antes de construir. El objetivo es combinar planificación, delegación de subtareas, workers especializados, colas, concurrencia y verificación. Un grafo de dependencias permite controlar cuándo puede ejecutarse cada tarea; un registro de eventos permite explicar qué ocurrió y detectar fallos.

Me interesa integrar servidores MCP y herramientas externas con contratos estructurados, permisos de mínimo privilegio y trazabilidad. Para la ejecución de código, distingo entre un subproceso y un sandbox: el primero administra un proceso, pero no garantiza aislamiento de seguridad. Plataformas como Daytona y E2B son opciones de infraestructura que deben evaluarse según sus límites de ejecución, red, almacenamiento y recursos.

También exploro Vercel AI SDK para integrar modelos, streaming, llamadas a herramientas y respuestas estructuradas, manteniendo el núcleo de negocio independiente de los proveedores.

## Por qué estoy desarrollando y entrenando mi propio asistente de IA

Mi motivación nace del mismo problema que describo en el README: no quiero una IA que genere código automáticamente cuando todavía no comprende la tarea. Quiero investigar cómo enseñarle a reconocer incertidumbre, consultar evidencia, planificar y verificar antes de responder.

He realizado experimentos con un Transformer pequeño desarrollado en PyTorch y tokenización BPE. También he trabajado en el ajuste fino supervisado (SFT) de modelos base de la familia Qwen mediante LoRA. Son dos enfoques diferentes: experimentar con una arquitectura desde cero y adaptar un modelo preentrenado. No afirmo haber preentrenado un modelo fundacional de gran escala.

### Entrenamiento en Kaggle y aceleración GPU

Utilizo Kaggle Notebooks como entorno de experimentación con aceleración NVIDIA CUDA. He registrado ejecuciones de entrenamiento en Tesla T4 y preparado notebooks para la configuración T4 ×2. Cada T4 dispone de 16 GB de memoria nominal; las memorias de dos tarjetas no se combinan automáticamente. En una configuración inicial seleccioné únicamente `cuda:0`, por lo que no afirmo haber realizado entrenamiento distribuido en ambas GPU.

Mi stack experimental incluye Python, PyTorch y CUDA, modelos Qwen, ajuste fino supervisado (SFT), adaptadores LoRA y configuraciones QLoRA con cuantización NF4 de 4 bits. También he preparado configuraciones con PEFT, Accelerate y Unsloth. Antes de entrenar compruebo el dispositivo disponible y su memoria; durante los experimentos me interesa controlar el tamaño de lote, la acumulación de gradientes, la longitud de secuencia, las pérdidas y los checkpoints. La cuantización y el ajuste de adaptadores permiten reducir los requisitos de memoria frente al ajuste completo de los pesos, aunque su impacto debe evaluarse para cada modelo.

Los resultados del entrenamiento deben distinguirse de la certificación mediante benchmarks independientes. No afirmo que la configuración de dos GPU haya sido ejecutada de forma distribuida ni que todos los experimentos planificados hayan concluido correctamente.

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

## Automatización de procesos con MCP e inteligencia artificial

Mi enfoque de automatización parte de las tareas que una persona realiza diariamente dentro de una empresa. Me interesa identificar procesos repetitivos, operaciones que consumen demasiado tiempo y trabajos que, por su volumen o complejidad, una persona difícilmente podría realizar manualmente a la escala necesaria.

Para eso planteo utilizar servidores MCP (Model Context Protocol) como una capa de conexión entre los agentes y las herramientas de trabajo: APIs, CRM, ERP, bases de datos, documentos y otros servicios. MCP facilita el acceso estructurado a herramientas; la programación, los disparadores, las colas y la coordinación del flujo corresponden al motor de automatización.

No utilizo un modelo de IA para todo. Cuando una tarea tiene reglas claras, prefiero código determinista, validaciones y workflows. Integro modelos de inteligencia artificial cuando el trabajo requiere comprender documentos, clasificar información no estructurada, resumir grandes volúmenes de datos o detectar posibles inconsistencias. Las decisiones sensibles, los casos ambiguos y las excepciones deben poder escalarse a una persona.

Por ejemplo, en un proceso administrativo, un workflow puede recopilar documentos mediante herramientas MCP, validar campos con reglas explícitas, utilizar un modelo para interpretar texto y preparar un informe para revisión humana. Es un ejemplo de diseño, no una integración con un cliente que afirme tener desplegada.

Mi objetivo es reducir el trabajo manual, los errores y los tiempos operativos, manteniendo permisos, trazabilidad y responsabilidad humana. Evaluaría cada automatización mediante tiempo ahorrado, tasa de errores, coste por ejecución y proporción de casos que necesitan intervención.

## SDK, herramientas y sistemas que he explorado o integrado

En Meridian he trabajado con Vercel AI SDK para streaming, tool calling, estado del chat, transporte de eventos y adaptadores de modelos OpenAI, Anthropic y Google. También he trabajado con el SDK de Anthropic y el de Google Generative AI. Estudio OpenAI SDK, OpenAI Agents SDK y Claude Agent SDK como alternativas de integración y orquestación; no los presento como integraciones completas solo por haber utilizado sus modelos o un adaptador.

He integrado herramientas mediante Model Context Protocol y sus SDK, con descubrimiento de capacidades, esquemas de entrada, registro de herramientas y controles de aprobación. Me interesa la gestión de Agent Skills, el enrutamiento de modelos por coste y latencia, y la recuperación de contexto mediante memoria y bases vectoriales.

En ejecución remota he trabajado con Daytona, E2B y Vercel Sandbox en distintos grados de integración. Para navegación y automatización web he explorado Browserbase, Steel y Playwright; para investigación, SerpAPI. Distingo entre tener un adaptador implementado y haber comprobado su funcionamiento real con un proveedor.

## Voz e interfaces generativas

He experimentado con un sistema de síntesis de voz basado en FastAPI, Python y Piper TTS, con carga anticipada de modelos, caché y medición de latencia. También he trabajado con integraciones de voz de OpenAI y ElevenLabs, incluyendo sesiones y gestión de estados. No considero equivalentes la síntesis de voz, el reconocimiento de voz y una conversación en tiempo real.

En interfaces trabajo con React, Next.js, TypeScript, shadcn/ui, Tailwind CSS, Framer Motion, AI Elements y componentes de visualización. Me interesa representar eventos reales de herramientas y agentes, no simular actividad. También exploro editores de contenido con Tiptap, diagramas de flujos y experiencias visuales con Three.js, GSAP y Remotion.

## Seguridad, datos y operaciones

Trabajo con arquitecturas de backend basadas en NestJS y Node.js, APIs HTTP, eventos SSE, validación de esquemas con Zod, PostgreSQL, Prisma y Supabase. Considero el aislamiento multi-tenant, RLS, permisos de mínimo privilegio, autenticación, protección de credenciales, auditoría y migraciones como partes del diseño, no añadidos posteriores. He trabajado con despliegues en Vercel y Railway y explorado Docker y Cloudflare Workers. También utilizo Git para revisar diferencias, organizar ramas y documentar cambios. En automatización empresarial exploro n8n, webhooks y flujos de CRM y ERP.

Esta descripción reúne experiencias de diferentes proyectos y líneas de estudio. No afirma que todas las tecnologías estén instaladas en Sandbox, que todas las integraciones estén activas en producción ni que haya verificado nuevamente cada repositorio privado.

## Calidad sin depender de GitHub Actions

Mi criterio es investigar, implementar, revisar y medir antes de integrar un cambio. Las comprobaciones pueden ejecutarse localmente o en un entorno autorizado sin depender de runners de GitHub Actions.

Para Python, contemplo pruebas con pytest, análisis estático con Ruff, comprobación de tipos con mypy, criterios de aceptación Gherkin y pruebas de mutación cuando aporten valor. Antes de integrar cambios importantes, revisaría dependencias, riesgos, permisos y resultados de pruebas. Estas herramientas representan una estrategia de calidad, no una afirmación de que todas estén configuradas o hayan sido ejecutadas en este repositorio.

## Ejemplo: cómo automatizaría una tarea de ingeniería de software

Supongamos que una empresa necesita añadir una operación a su API para registrar una factura sin duplicarla. No empezaría pidiéndole a un modelo que genere código. Mi enfoque, inspirado en los principios de código limpio y complementado con prácticas de control de calidad, consiste en automatizar el ciclo de desarrollo sin eliminar la responsabilidad de verificar el resultado.

1. **Recepción y análisis.** El orquestador obtiene el requisito y el contexto autorizado mediante herramientas MCP. Identifico el comportamiento esperado, los criterios de aceptación, los riesgos y las restricciones. Si falta información crítica, solicito aclaración.
2. **Investigación.** Un worker revisa la documentación oficial, el repositorio, los contratos existentes y las dependencias. Registra las fuentes y los supuestos antes de diseñar una solución.
3. **Planificación y delegación.** Divido el trabajo en subtareas de arquitectura, implementación, seguridad y pruebas. El grafo de dependencias y la cola determinan cuáles pueden ejecutarse en paralelo y cuáles deben esperar.
4. **Implementación.** El worker de desarrollo trabaja en una rama y un entorno aislado autorizado, con datos ficticios. Aplico nombres claros, funciones con responsabilidades delimitadas, contratos explícitos, manejo de errores y separación de responsabilidades. Evito abstracciones innecesarias.
5. **Validación estática.** Reviso tipos, esquemas, formato, dependencias, secretos y el diff. Utilizo herramientas de análisis apropiadas para el lenguaje, sin confiar únicamente en la revisión del modelo.
6. **Pruebas unitarias y de integración.** Compruebo la lógica de validación, la idempotencia, el manejo de errores y la interacción con la API y una base de datos de pruebas. Incluyo solicitudes simultáneas cuando existe riesgo de duplicación.
7. **Pruebas de extremo a extremo (E2E).** Verifico el flujo completo desde la solicitud autenticada hasta la respuesta y el registro persistido. Compruebo escenarios válidos, datos incorrectos, duplicados y acceso no autorizado. Si existe una interfaz, puedo utilizar Playwright para verificar el recorrido de usuario.
8. **Revisión y mejora.** Un worker verificador independiente contrasta los resultados con los criterios de aceptación. Si encuentra fallos, devuelve una subtarea acotada al desarrollador; se vuelven a ejecutar las pruebas pertinentes y la suite de regresión. Considero mutation testing para comprobar que las pruebas detectan cambios defectuosos.
9. **Quality gate y aprobación.** Recopilo evidencia de pruebas, archivos modificados, riesgos pendientes y resultados de revisión. Si una comprobación obligatoria falla o no se ejecutó, no doy la tarea por aprobada. La integración o el despliegue requieren autorización según el riesgo.

### Criterios de aceptación del ejemplo (Gherkin)

```gherkin
Feature: Registro de facturas sin duplicados
  Scenario: Registrar una factura válida
    Given una persona autenticada con permiso de registro
    When envía una factura válida con una clave de idempotencia nueva
    Then la API confirma el registro
    And existe exactamente un registro de esa operación

  Scenario: Repetir la misma solicitud
    Given una factura registrada con una clave de idempotencia
    When se repite la misma solicitud con esa clave
    Then no se crea una segunda factura

  Scenario: Solicitud sin permisos
    Given una persona sin permiso de registro
    When intenta registrar una factura
    Then la API rechaza la operación
    And no se modifica la base de datos
```

Estos escenarios son criterios propuestos, no pruebas ejecutadas. Este flujo describe cómo diseñaría una automatización de ingeniería; no afirma que se haya implementado una solución de facturación electrónica ni que cumpla requisitos fiscales específicos. Las validaciones pueden ejecutarse localmente sin GitHub Actions. El modelo propone o interpreta; las herramientas de prueba y la evidencia verificable determinan si el resultado cumple los requisitos.

## Alcance público

Este laboratorio documenta mis líneas de trabajo sin divulgar código propietario, datos de clientes ni credenciales. Las propuestas, los prototipos y las capacidades validadas se mantienen diferenciados. No pretendo construir una demostración para cada concepto: la documentación también sirve para explicar decisiones, limitaciones y aprendizajes.

Referencias internas: [diseño del runtime autónomo](research-first-agent-runtime.md), [arquitectura de Meridian API](meridian-api-architecture.md) y [MCP y control de herramientas](mcp-context-and-tools.md).
