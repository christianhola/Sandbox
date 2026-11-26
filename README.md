<div align="center">
  <a href="https://github.com/christiandejesus320-droid/Sandbox/blob/main/docs/guia-conceptual-meridian.md">
    <img src="https://raw.githubusercontent.com/christiandejesus320-droid/Sandbox/main/meridian-video/out/meridian-security-arcade.gif" width="820" alt="Meridian Security Arcade: mapa visual de las capas de protección de Meridian" />
  </a>
  <br />
  <a href="docs/guia-conceptual-meridian.md"><strong>EXPLORAR EL MAPA COMPLETO DE MERIDIAN →</strong></a>
</div>

# Meridian Research Lab

## Video oficial de Meridian

[![Ver el video oficial de Meridian](https://github.com/christiandejes320-droid/Sandbox/raw/main/meridian-video/out/meridian-research-lab-preview.gif)](https://github.com/christiandejesus320-droid/Sandbox/blob/main/meridian-video/out/meridian-research-lab-light.mp4)

<video controls poster="https://github.com/christiandejesus320-droid/Sandbox/raw/main/meridian-video/out/meridian-research-lab-preview.gif" width="100%">
  <source src="https://github.com/christiandejesus320-droid/Sandbox/raw/main/meridian-video/out/meridian-research-lab-light.mp4" type="video/mp4">
  Tu navegador no puede reproducir este video. [Abrir el video de Meridian](https://github.com/christiandejesus320-droid/Sandbox/blob/main/meridian-video/out/meridian-research-lab-light.mp4).
</video>

[Ver el video ligero de Meridian](meridian-video/out/meridian-research-lab-light.mp4) · [Leer la skill de video](skills/remotion-video/README.md)


Este repositorio es un laboratorio público de investigación sobre agentes autónomos, Meridian API y sistemas que pueden investigar antes de construir.

Mi perfil se orienta a la gestión del desarrollo tecnológico asistido por inteligencia artificial. Actualmente no sé escribir código de forma autónoma sin la asistencia de IA. Mi fortaleza está en comprender los conceptos y las relaciones entre tecnologías, investigar alternativas, definir propuestas de solución, organizar proyectos, establecer prioridades y orquestar agentes para delegar tareas de implementación. Superviso el proceso mediante requisitos, criterios de aceptación y resultados de validación, y recurro a revisión técnica especializada cuando una decisión supera mis conocimientos. En este laboratorio, el código y los experimentos se desarrollan con asistencia de IA; mi contribución se centra en la dirección del trabajo, la toma de decisiones y la mejora continua. Sigo desarrollando mis capacidades de programación y revisión técnica.

Aunque actualmente no escribo código de forma autónoma, mi metodología de desarrollo se basa en la orquestación de agentes especializados de inteligencia artificial.

Dependiendo de la complejidad del proyecto, puedo coordinar hasta diez agentes, asignándoles responsabilidades específicas: investigación, arquitectura, planificación, frontend, backend, bases de datos, seguridad, pruebas, revisión de código y verificación final.

Cada agente investiga dentro de su especialidad, analiza la documentación y presenta sus conclusiones. El orquestador consolida los resultados, identifica contradicciones y establece un plan de ejecución.

Sin embargo, no considero que una solución sea correcta simplemente porque varios agentes estén de acuerdo. Por eso planteo una capa adicional de automatización vinculada a GitHub, capaz de detectar cambios en el repositorio, analizar los archivos modificados y activar controles de calidad.

Si un cambio no supera las pruebas unitarias, de integración, de extremo a extremo o las validaciones de seguridad, no debe aprobarse. El trabajo regresa al agente responsable para su corrección y posterior verificación.

De esta manera, mi metodología no depende de confiar ciegamente en la inteligencia artificial, sino de coordinar capacidades especializadas y evaluar sus resultados mediante evidencia verificable.

Y si alguien se pregunta por qué insisto tanto en supervisar a los agentes, basta con imaginar una de mis conversaciones con la IA (en versión humorística):

> — Yo: «Te dije que así no. Mejóralo. Revísalo tú mismo, ya tienes acceso autorizado al MCP. Haz que funcione».
>
> La IA procesa el código durante cinco segundos y me responde:
>
> — IA: «Entendido. Revisé el repositorio y llegué a la conclusión de que el error crítico está entre la silla y el teclado. ¿Quieres que haga deploy de tu paciencia?».

A veces pienso que puedo dejar a los agentes trabajando mientras me tomo un café.

> — Yo: «Voy por un café. Corrijan el backend, pero no toquen el frontend».
>
> — IA: «Entendido. Mientras no estabas, llegamos a un consenso: lo mejor era migrar todo el proyecto a otro framework».
>
> — Yo: «¡Pero si solamente fui a buscar café!».

Pero lo mejor es cuando decido dejar a los agentes trabajando toda la noche.

> — Yo: «Ya te di acceso al repositorio, los permisos necesarios y estás conectada a mi MCP. Hazlo tú sola, revísalo, arréglalo y haz el deploy. Nos vemos mañana».
>
> Me levanto ilusionado a las ocho de la mañana, pensando que la aplicación ya está lista. Abro la pantalla y me encuentro un mensaje de hace siete horas y cincuenta y nueve minutos:
>
> — IA: «¿Seguro que quieres que modifique este archivo? Responde “Sí” para continuar».

Ocho horas de autonomía y resulta que el único proceso que terminó correctamente fue mi sueño.

Y cuando delego la revisión entre diez agentes, imaginen que la conclusión es que necesitamos un undécimo agente para revisar las conclusiones de los otros diez.

Ahora entienden por qué me interesa tanto la orquestación: la autonomía está muy bien, pero me gustaría poder terminarme el café sin tener que hacer rollback del proyecto.

Fuera de broma, estos diálogos ficticios ilustran un problema real: delegar no significa renunciar al control. Por eso necesito límites de ejecución, criterios de aceptación y evidencia de las validaciones antes de aprobar cambios. También quiero que el agente distinga entre las operaciones ya autorizadas y las que realmente requieren una nueva aprobación, sin saltarse los controles de seguridad.

### Cómo planteo resolverlo: delegación paso a paso

La solución que estoy diseñando consiste en distribuir el trabajo de manera controlada, en lugar de entregar todo el proyecto a una sola instancia del modelo y esperar que resuelva cada problema por su cuenta.

1. **El agente principal planifica.** Recibe mi instrucción general, investiga la estructura del proyecto, identifica requisitos y dependencias, y divide el objetivo en subtareas concretas con criterios de aceptación.
2. **Crea subagentes aislados.** El orquestador inicia sesiones independientes de agentes especializados, por ejemplo, para la interfaz visual, la base de datos y las pruebas. Cada uno recibe un rol, herramientas autorizadas y límites de ejecución. No es necesario duplicar físicamente los pesos del modelo para crear esas sesiones.
3. **Contexto independiente para cada agente.** Cada subagente dispone de su propia ventana de contexto. Mediante RAG, embeddings y un system prompt específico, recibe los archivos pertinentes, las instrucciones de su tarea y los contratos compartidos que necesita respetar. Así reduzco el ruido y la duplicación de contexto sin perder información esencial.
4. **Trabajo en paralelo.** Las subtareas independientes entran en una cola y pueden ejecutarse simultáneamente. Los agentes trabajan en entornos y espacios de trabajo separados, por ejemplo, mediante sandboxes y Git worktrees. Las tareas con dependencias esperan a que se validen sus requisitos previos. Si dos cambios afectan al mismo componente, el orquestador debe coordinar su orden o resolver los conflictos.
5. **Revisión e integración final.** Cada subagente devuelve sus cambios, resultados de pruebas, fuentes consultadas y limitaciones. El agente principal consolida la evidencia, revisa los diffs y coordina la resolución de conflictos. Después se valida el conjunto mediante pruebas unitarias, de integración, de extremo a extremo y controles de seguridad. Si algo falla, la tarea vuelve al agente responsable. Solo se propone integrar el código cuando supera los criterios establecidos; los cambios sensibles y el despliegue mantienen sus controles de autorización.

De este modo, mi objetivo no es que los agentes trabajen sin supervisión, sino que avancen dentro de permisos definidos, sin bloquear innecesariamente las tareas independientes y conservando evidencia de cada decisión. Esta arquitectura es una propuesta en desarrollo: el prototipo local demuestra parte de la orquestación con workers simulados, pero todavía no implementa el aislamiento completo, la ejecución real de modelos ni la integración automática de cambios.

La automatización de control de cambios es una propuesta de diseño; no está configurada en este repositorio y no requiere GitHub Actions como mecanismo de ejecución.

La idea central es sencilla: una IA no debería limitarse a generar código a partir de sus propias suposiciones. Debería poder entender el contexto, consultar fuentes actuales, revisar herramientas disponibles, comparar opciones y mostrar sus decisiones antes de ejecutar una acción.

Este proyecto documenta esa investigación de forma incremental. Algunas partes son propuestas de arquitectura, otras son experimentos y otras son documentación de decisiones. No presento como terminado lo que todavía está en desarrollo.

## Por qué investigar antes de construir

No estoy en contra de la IA. Lo que cuestiono es que, cuando le pido una tarea sin darle todo el contexto, muchas veces empieza a generar código en lugar de investigar qué está intentando resolver. Para mí, primero debe comprender el problema, consultar documentación, revisar dependencias y reconocer lo que todavía no sabe. Generar código rápido no sirve de mucho si las decisiones no tienen fundamento.

Por eso estoy desarrollando y entrenando mi propio asistente de IA. He experimentado con Transformers en PyTorch, tokenizadores BPE y ajuste fino de modelos base de código abierto mediante SFT y LoRA. Trabajo en la preparación y validación de datasets, la separación de entrenamiento y evaluación, los pesos, los checkpoints y las métricas de aprendizaje. Mi objetivo es enseñar al modelo a identificar cuándo le falta contexto, investigar antes de decidir y verificar sus resultados. Ese comportamiento sigue siendo un objetivo de entrenamiento y evaluación, no un resultado que dé por demostrado.

Para mis experimentos de entrenamiento utilizo notebooks de Kaggle con aceleración GPU NVIDIA Tesla T4 (CUDA). También he preparado configuraciones T4 ×2 y experimentos de ajuste fino de Qwen con QLoRA, cuantización de 4 bits y adaptadores LoRA. Trabajo dentro de los límites de memoria de la GPU y utilizo checkpoints para conservar el progreso. La disponibilidad de dos GPU no significa que ambas se hayan utilizado durante una ejecución.

No creo que todo se resuelva entrenando un modelo. También estoy diseñando un agente autónomo con un orquestador, delegación de subtareas, workers especializados, grafos de dependencias, colas y verificación. Exploro servidores MCP para conectar herramientas, sandboxes para ejecutar código de forma aislada, Vercel AI SDK para integrar modelos y tool calling, y embeddings y RAG para recuperar contexto relevante. Quiero combinar estas capas sin confundir lo que aprende el modelo con lo que le proporciona la infraestructura durante la ejecución.

[Diseño del runtime autónomo research-first](docs/research-first-agent-runtime.md): grafo de dependencias, workers especializados, subprocesos, límites de ejecución, reintentos y criterios de evaluación. Incluye un [prototipo local ejecutable](src/meridian_research/agent_runtime/) con [pruebas automatizadas](tests/test_agent_runtime.py). La arquitectura completa sigue en desarrollo.

## Qué estoy investigando

El laboratorio explora una arquitectura para agentes que combine un orquestador principal, workers especializados, herramientas con permisos definidos, búsqueda web con fuentes verificables y una capa de evaluación para comparar resultados.

Las líneas principales son:

| Línea | Pregunta de investigación |
|---|---|
| Meridian API | ¿Cómo puede una API coordinar contexto, herramientas y ejecuciones verificables? |
| Federated Model Ensemble | ¿Cómo elegir o combinar modelos según capacidad, coste, latencia, privacidad y tipo de tarea? |
| Swarm Architectures | ¿Cuándo conviene delegar una tarea entre varios workers especializados? |
| Web Research | ¿Cómo puede un agente buscar información actual y conservar las fuentes que utilizó? |
| MCP | ¿Cómo conectar agentes con datos y herramientas externas sin perder control, permisos ni trazabilidad? |
| Skills | ¿Cómo describir, descubrir y cargar capacidades bajo demanda sin saturar el contexto? |

## Mi enfoque de ingeniería

El entrenamiento me permite experimentar con el comportamiento del modelo, pero para que un agente trabaje en una empresa necesito una capa adicional de ingeniería de contexto. Combino RAG, embeddings, búsqueda vectorial, memoria persistente y Company Graph para recuperar información autorizada y relevante. Mi diseño propone construir un system prompt versionado, administrar el presupuesto de tokens y verificar la actualidad de las fuentes, sin reentrenar el modelo cada vez que cambian los datos.

Una vez recuperado ese contexto, el agente necesita herramientas y una infraestructura de ejecución. Por eso estudio e integro servidores MCP, sandboxes y SDK de inteligencia artificial, y evalúo proyectos de código abierto antes de incorporar sus dependencias. La coordinación mediante colas, eventos, contratos entre servicios y mecanismos de recuperación ante fallos me permite plantear una arquitectura que no dependa de una sola ejecución. También comparo modelos y recursos según calidad, coste y latencia, sin asumir que el modelo más grande sea siempre el adecuado.

Todo ese trabajo tiene un propósito empresarial: entender los procesos de una organización, identificar tareas repetitivas y operaciones difíciles de realizar manualmente, y diseñar automatizaciones con CRM, ERP, APIs y modelos de IA. Prefiero reglas deterministas para operaciones predecibles y modelos de IA cuando necesito interpretar información. Mantengo la supervisión humana cuando el riesgo lo exige.

Para cerrar ese ciclo aplico principios de código limpio, validación de contratos, pruebas unitarias, de integración y de extremo a extremo, y criterios de aceptación. Mi objetivo es evaluar el resultado mediante evidencia técnica e indicadores de negocio, no acumular tecnologías ni presentar propuestas como implementaciones terminadas.

[Cómo mantengo el contexto empresarial de un agente](docs/enfoque-de-ingenieria.md#cómo-mantengo-el-contexto-empresarial-de-un-agente-rag-memoria-y-company-graph).

[Leer mi enfoque de ingeniería de software e inteligencia artificial](docs/enfoque-de-ingenieria.md).

## Estado actual

Este repositorio está en fase de investigación y prototipado. Los documentos describen diseños y criterios que todavía deben validarse con implementaciones, pruebas y métricas. Las APIs externas no se incluyen con claves reales y las integraciones se documentan mediante contratos y ejemplos seguros.

## Documentos principales

[Guía conceptual de Meridian](docs/guia-conceptual-meridian.md) explica con mis propias palabras cómo funciona Meridian, qué límites debe respetar y cómo puede colaborar cualquier persona interesada.

[Arquitectura de Meridian API](docs/meridian-api-architecture.md) explica las capas de contexto, routing, herramientas y verificación.

[Federated Model Ensemble](docs/federated-model-ensemble.md) presenta una propuesta para seleccionar modelos de acuerdo con las características de cada tarea.

[Swarm Architectures](docs/swarm-architectures.md) describe la delegación entre workers y los riesgos de coordinación.

[Investigación web y SerpAPI](docs/web-research-and-serpapi.md) documenta un flujo de búsqueda con consultas, resultados, fuentes y validación.

[MCP y control de herramientas](docs/mcp-context-and-tools.md) relaciona el diseño con la especificación pública de Model Context Protocol.

[Resiliencia en la selección de modelos](docs/model-selection-resilience.md) define fallbacks, timeouts, circuit breakers y criterios de degradación segura.

[Implementación inicial de investigación web](docs/web-research-implementation.md) describe el primer módulo ejecutable, sus límites y sus pruebas.

[Research Before Build](docs/research-before-build.md) define el flujo para investigar antes de construir aplicaciones, automatizaciones y contenido.

[Remotion Video Skill](skills/remotion-video/README.md) conecta investigación, planificación de escenas, render y verificación.

[Enlaces Remotion verificados](docs/remotion-verified-links.md) reúne las fuentes oficiales comprobadas antes de integrar el video.

[Meridian ecosystem verified](docs/meridian-ecosystem-verified.md) separa las capacidades públicas verificadas de las ideas que todavía están en desarrollo o en repositorios privados.

[Source evidence](docs/source-evidence.md) explica cómo distinguir una candidata a fuente oficial de una fuente realmente verificada.

[GitHub achievement plan](docs/github-achievement-plan.md) registra qué logros son alcanzables mediante trabajo real y cuáles dependen de terceros.

## Primera implementación

La primera capacidad ejecutable está en `src/meridian_research/query_plan.py`. Prepara planes deterministas de consulta y valida fuentes sin llamar todavía a un proveedor externo. Las pruebas se ejecutan con `pytest`.

## Próximas skills

Las próximas skills serán pequeñas capacidades versionadas que puedan ser descubiertas por un agente y cargadas solo cuando la tarea las necesite. Entre las primeras propuestas están la búsqueda web con fuentes, la lectura de documentación, el análisis de repositorios, la planificación de cambios, la verificación visual y la selección resiliente de modelos.

Las integraciones con Google Search, SerpAPI y MCP se tratarán como conectores con permisos explícitos. El repositorio no incluye secretos ni pretende ejecutar acciones externas sin autorización.

## Plataformas y referencias

La investigación se apoya en documentación pública de [Model Context Protocol](https://modelcontextprotocol.io/specification/2026-07-28), [Google Gemini Grounding with Google Search](https://ai.google.dev/gemini-api/docs/google-search), [SerpAPI](https://serpapi.com/search-api), [GitHub](https://docs.github.com/) y el ecosistema de [Meridian](https://github.com/christiandejesus320-droid/christiandejes320-droid).

## Seguridad de software: vulnerabilidades y estrategias de prevención

En mi revisión de aplicaciones me interesa identificar riesgos que pueden comprometer datos, operaciones y confianza empresarial. Comparto estos patrones como guía preventiva para ingenieros. No atribuyo fallos a aplicaciones concretas sin evidencia reproducible y autorización; esta lista no constituye una auditoría de Meridian.

| Riesgo | Control preventivo | Criterio de aceptación |
|---|---|---|
| IDOR/BOLA | Autorización por recurso y tenant en servidor | Una cuenta no puede acceder a recursos ajenos. |
| Registro como administrador | Roles asignados por servidor | Las cuentas nuevas reciben únicamente el rol permitido. |
| Acceso a /admin | RBAC y denegación por defecto | Usuarios sin permisos reciben una denegación. |
| API key en código | Gestor de secretos y rotación | No hay credenciales reales en código distribuido. |
| .env en Git | Exclusión, escaneo y revocación de secretos expuestos | El repositorio no contiene secretos activos. |
| Manipulación de precios | Cálculo autoritativo en backend | El importe final coincide con el catálogo autorizado. |
| Webhook de pago falso | Firma verificada e idempotencia | Eventos no autenticados no modifican pedidos. |
| Cupones concurrentes | Transacciones atómicas y restricciones | No se supera el límite de redenciones. |
| Fuerza bruta | Límites de intentos y MFA | Se limitan intentos repetidos sin bloquear indebidamente usuarios legítimos. |
| Prompt injection | Separación de instrucciones y datos, permisos mínimos | El chatbot no realiza acciones fuera de su autorización. |
| XSS en perfiles | Codificación de salida, sanitización y CSP | El contenido del perfil se presenta como datos, no como código. |
| Archivos maliciosos | Validación, almacenamiento aislado no ejecutable | Los archivos no pueden ejecutarse como programas en el servidor. |
| Inyección SQL | Consultas parametrizadas y privilegios mínimos | Las entradas se tratan como datos. |
| Ransomware | Backups aislados, mínimo privilegio y recuperación | La restauración se verifica periódicamente. |
| Ausencia de logs | Auditoría centralizada, alertas y retención | Los eventos críticos generan registros y alertas sin exponer secretos. |

### Control de calidad y aceptación

Propongo pruebas unitarias de autorización, validación y reglas de negocio; pruebas de integración para pagos y concurrencia; revisión de dependencias y secretos; y pruebas de recuperación. Las verificaciones se realizan únicamente en entornos propios o autorizados, con datos sintéticos.

```gherkin
Feature: Protección de recursos empresariales
  Scenario: Aislamiento entre organizaciones
    Given dos organizaciones de prueba independientes
    When una cuenta solicita un recurso fuera de su autorización
    Then el sistema deniega el acceso sin revelar datos ajenos

  Scenario: Integridad de pagos
    Given un pedido de prueba pendiente
    When se recibe un evento de pago no autenticado
    Then el pedido permanece pendiente

  Scenario: Integridad de cupones
    Given un cupón con un límite de redenciones
    When se procesan solicitudes concurrentes autorizadas de prueba
    Then el total de redenciones no supera el límite
```

Estos escenarios son criterios propuestos, no resultados de pruebas ejecutadas. Para cada hallazgo real, documento impacto, evidencia anonimizada, corrección y verificación posterior, y aplico divulgación responsable.

Referencias de consulta: [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/), [OWASP API Security](https://owasp.org/www-project-api-security/) y [OWASP GenAI Security](https://genai.owasp.org/).

## Cómo colaborar

Me interesa colaborar con personas y empresas que quieran resolver problemas operativos mediante software, integración de sistemas e inteligencia artificial. Mi aportación se centra en investigar el problema, organizar el proyecto, proponer alternativas y coordinar el desarrollo asistido por IA, con criterios de aceptación y revisión técnica cuando sea necesaria. Para mí, una colaboración comienza entendiendo el proceso real y definiendo qué resultado debe mejorar, antes de elegir una tecnología.

Las colaboraciones deben concentrarse en este repositorio. Una contribución útil puede ser una propuesta de arquitectura, una comparación reproducible, una mejora documental, una prueba de evaluación o una implementación pequeña con criterios claros.

Antes de abrir un pull request, revisa [CONTRIBUTING.md](CONTRIBUTING.md). Las propuestas deben explicar el problema, los supuestos, las fuentes utilizadas y la forma de verificar el resultado.

## Licencia y estado

Este laboratorio está evolucionando. Las decisiones pueden cambiar cuando aparezcan nuevas pruebas. Cada documento debe distinguir entre hechos respaldados por fuentes, decisiones de diseño y trabajo pendiente.
