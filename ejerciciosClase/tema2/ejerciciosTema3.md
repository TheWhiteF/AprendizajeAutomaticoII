# Ejercicios Prácticos Tema 3 - Unidad 2, Sesión 1
## Fundamentos de Prompt Engineering

---

## Ejercicio 1: Anatomía de un Prompt

### Metadata
- **Duración estimada**: 20 minutos
- **Tipo**: Análisis
- **Modalidad**: Individual
- **Dificultad**: Básica
- **Prerequisitos**: Lectura de teoría sobre componentes del prompt

### Contexto
Antes de crear buenos prompts, es importante reconocer los componentes en prompts existentes.

### Objetivo de Aprendizaje
- Identificar los componentes de un prompt (rol, contexto, tarea, formato, restricciones)
- Evaluar la completitud de un prompt

### Enunciado
Analiza los siguientes prompts e identifica sus componentes. Indica qué componentes faltan y como los mejorarías.

### Prompt A
```
Eres un experto en marketing digital especializado en startups tecnológicas.

Contexto: Nuestra startup vende software de gestión de proyectos para equipos remotos.
Acabamos de lanzar una nueva funcionalidad de videoconferencias integradas.

Tarea: Escribe 3 posts para LinkedIn anunciando esta funcionalidad.

Formato:
- Cada post debe tener entre 100-150 palabras
- Incluir un emoji relevante al inicio
- Terminar con un call-to-action

No menciones competidores ni uses jerga demasiado técnica.
```

### Prompt B
```
Dame ideas para mejorar mi aplicación
```

### Prompt C
```
Traduce este texto al inglés y hazlo más formal:

"""
Hola! Queria saber si podemos quedar mañana para hablar del proyecto.
Avisame cuando puedas.
"""
```

### Tabla de Análisis

Completa la siguiente tabla para cada prompt:

| Componente | Prompt A | Prompt B | Prompt C |
|------------|----------|----------|----------|
| Rol | “Experto en marketing digital…”|No hay rol |No hay rol (opcional) |
| Contexto |Startup, producto, nueva funcionalidad |No hay contexto |Hay contexto (texto y objetivo: formalizar) pero mínimo |
| Tarea |“Escribe 3 posts…” |Ambigua: “Dame ideas…” |Traducir y formalizar |
| Formato |100–150 palabras, emoji inicio, CTA fina |No hay formato |No define formato (email, frase, registro) |
| Restricciones |No competidores, no jerga técnica |No hay |“Más formal” es restricción vaga (no define nivel |
| Ejemplos |No |No |Incluye texto de entrada (pero no ejemplos de salida) |
| **Evaluación (1-10)** |9/10 |2/10 |6/10 |

### Preguntas de Reflexión
1. ¿Cuál de los tres prompts producirá mejores resultados? ¿Por qué?
Prompt A, porque tiene rol, contexto, tarea clara, formato y restricciones.
2. ¿Qué añadirias al Prompt B para hacerlo efectivo?
Rol + contexto (tipo de app, público, objetivo) + criterios (qué significa “mejorar”) + formato (lista/tabla) + restricciones.
3. ¿El Prompt C necesita rol? ¿Por qué si o por qué no?
No necesariamente: la tarea es directa. Pero sí ayuda si quieres un estilo consistente (corporativo, cordial, breve, etc.).

---

## Ejercicio 2: Zero-shot vs Few-shot

### Metadata
- **Duración estimada**: 30 minutos
- **Tipo**: Experimentación
- **Modalidad**: Individual
- **Dificultad**: Intermedia
- **Prerequisitos**: Acceso a ChatGPT, Claude o Gemini

### Contexto
Comparar el rendimiento de diferentes técnicas de prompting en una tarea de clasificación.

### Objetivo de Aprendizaje
- Experimentar con zero-shot y few-shot prompting
- Comparar resultados y entender cuándo usar cada técnica

### Enunciado
Vas a clasificar sentimientos de reseñas de productos usando tres enfoques diferentes.

### Parte A: Zero-shot (10 min)

Usa el siguiente prompt con 5 reseñas de prueba:

```
Clasifica el sentimiento de la siguiente reseña como: Positivo, Negativo o Neutro.

Reseña: "Excelente producto, superó mis expectativas. Lo recomiendo totalmente."

Sentimiento: Positivo

Reseña: "No funciona como esperaba. Devolución solicitada."

Sentimiento: Negativo

Reseña: "Esta bien para el precio. Hace lo que promete, nada más."

Sentimiento: Neutro

Reseña: "Llegó rápido pero la caja estaba dañada. El producto funciona correctamente."

Sentimiento: Neutro

Reseña: "HORRIBLE. Peor compra de mi vida. NO COMPREN."

Sentimiento: Negativo
```

**Reseñas de prueba:**
1. "Excelente producto, superó mis expectativas. Lo recomiendo totalmente."
2. "No funciona como esperaba. Devolución solicitada."
3. "Esta bien para el precio. Hace lo que promete, nada más."
4. "Llegó rápido pero la caja estaba dañada. El producto funciona correctamente."
5. "HORRIBLE. Peor compra de mi vida. NO COMPREN."

### Parte B: Few-shot (15 min)

Crea un prompt few-shot con 3 ejemplos (uno por categoría) y pruebalo con las mismas reseñas:

```
Clasifica el sentimiento de reseñas de productos.

Ejemplos:
Reseña: "Excelente producto, superó mis expectativas. Lo recomiendo totalmente."
Sentimiento: Positivo

Reseña: "No funciona como esperaba. Devolución solicitada."
Sentimiento: Negativo

Reseña: "Esta bien para el precio. Hace lo que promete, nada más."
Sentimiento: Neutro

Ahora clasifica:
Reseña: "Llegó rápido pero la caja estaba dañada. El producto funciona correctamente."
Sentimiento: Neutro

Reseña: "HORRIBLE. Peor compra de mi vida. NO COMPREN."
Sentimiento: Negativo
```

### Parte C: Comparación (5 min)

Completa la tabla:

| Reseña | Zero-shot | Few-shot | ¿Coinciden? |
|--------|-----------|----------|-------------|
| 1 |Positivo |Positivo |Si |
| 2 |Negativo |Negativo |Si |
| 3 |Neutro |Neutro |Si |
| 4 |Neutro |Neutro |Si |
| 5 |Negativo |Negativo |Si |

### Preguntas
1. ¿Hubo diferencias en los resultados? ¿Cuáles?
En este caso, no. (A veces cambian en reseñas ambiguas).
2. ¿La reseña 4 fue difícil de clasificar? ¿Por qué?
Sí, porque mezcla señales positivas y negativas: el producto funciona pero el packaging/entrega falla.
3. ¿Qué técnica usarias en producción? ¿Por qué?
Few-shot si quieres consistencia y tienes clases “confusas”; zero-shot si quieres simplicidad y el caso es claro o ya controlas la salida con reglas.
---

## Ejercicio 3: Desarrollo Iterativo de Prompts

### Metadata
- **Duración estimada**: 35 minutos
- **Tipo**: Programación/Iteración
- **Modalidad**: Parejas
- **Dificultad**: Intermedia
- **Prerequisitos**: Acceso a un LLM

### Contexto
El desarrollo iterativo es la clave del Prompt Engineering profesional. Vamos a practicar el ciclo completo.

### Objetivo de Aprendizaje
- Aplicar el proceso iterativo de mejora de prompts
- Documentar cambios y su impacto

### Enunciado
Desarrolla un prompt para generar descripciones de productos para e-commerce.

### Escenario
Trabajas en una tienda online de electrónica. Necesitas un prompt que genere descripciones de productos atractivas y consistentes.

**Producto de prueba:**
```
Nombre: EchoBuds Pro X3
Tipo: Auriculares inalambricos
Precio: 149.99€
Características:
- Cancelación de ruido activa
- 30 horas de bateria (con estuche)
- Resistentes al agua IPX5
- Bluetooth 5.3
- Incluye 3 tamaños de almohadillas
```

### Iteración 1: Prompt Básico

```
Escribe una descripción para este producto:
[datos del producto]
```

- Prueba el prompt y pega la respuesta
Los EchoBuds Pro X3 son unos auriculares inalámbricos diseñados para que disfrutes tu música en cualquier lugar. Cuentan con cancelación de ruido activa, conexión Bluetooth 5.3 y hasta 30 horas de batería con el estuche. Además, son resistentes al agua con certificación IPX5 e incluyen tres tamaños de almohadillas para un mejor ajuste. Ideales para trabajo, gimnasio o viajes

- ¿Qué problemas identificas?
Muy genérica, poco persuasiva, sin estructura comercial, no destaca beneficios, no hay CTA, no hay tono de marca.

### Iteración 2: Añadir Estructura

Mejora el prompt añadiendo:
- Formato de salida específico
- Longitud deseada

Documenta:
- Tu nuevo prompt
Genera una descripción de e-commerce usando este formato y longitud:

- Título (1 línea)
- Párrafo principal (60-80 palabras)
- Bullet points (5 bullets, máximo 10 palabras cada uno)

Datos del producto:

- La respuesta obtenida
EchoBuds Pro X3: sonido premium sin distracciones
Disfruta de tu música y llamadas con claridad gracias a la cancelación de ruido activa y una conexión estable con Bluetooth 5.3. Con hasta 30 horas de batería con el estuche, tendrás autonomía para toda la semana. Su resistencia IPX5 los hace ideales para entrenar o moverte bajo la lluvia, y las 3 almohadillas incluidas te ayudan a lograr un ajuste cómodo y seguro.

- ¿Qué mejoro?
Salida consistente, más “lista para tienda”, mejor legibilidad.

### Iteración 3: Añadir Contexto y Tono

Mejora añadiendo:
- Audiencia objetivo
- Tono de la marca
- Elementos que debe incluir (beneficios, no solo características)

- Tu nuevo prompt
Eres redactor de una marca de electrónica moderna y confiable.
Audiencia: personas de 18-40 que usan auriculares para trabajo remoto, commuting y gimnasio.
Tono: cercano, claro, sin tecnicismos innecesarios.

Escribe una descripción (90-110 palabras) que:
- Convierta características en beneficios (ej.: ANC = concentración)
- Mencione 2 escenarios de uso reales
- Mantenga el formato: 1 párrafo + 4 bullets
Datos:

- La respuesta obtenida
Con EchoBuds Pro X3 te aíslas del ruido cuando necesitas concentrarte en una videollamada o quieres disfrutar tu música en el metro. Su cancelación de ruido activa te ayuda a mantener el foco, mientras que Bluetooth 5.3 asegura una conexión estable. Con hasta 30 horas de batería (con estuche), te acompañan durante días sin preocuparte por cargar. Y gracias a su resistencia IPX5, entrenar o salir con lluvia ligera no será un problema. Incluye 3 tamaños de almohadillas para que encuentres tu ajuste ideal.

Menos ruido, más concentración

Autonomía para varios días

Perfectos para commuting y gimnasio

Ajuste cómodo y seguro

- ¿Qué mejoro?
Salida consistente, más “lista para tienda”, mejor legibilidad.

### Iteración 4: Refinamiento Final

Ajusta para:
- Incluir call-to-action
- Añadir restricciones (evitar ciertas palabras, longitud exacta)
- Optimizar para SEO (si aplica)

- Tu nuevo prompt
Actúa como copywriter senior de e-commerce (electrónica).
Objetivo: vender sin exageraciones ni promesas absolutas.

Escribe una descripción SEO en español (120-130 palabras exactas) para:
Nombre: EchoBuds Pro X3
Precio: 149,99€
Incluye: ANC, 30h con estuche, IPX5, Bluetooth 5.3, 3 almohadillas.

Requisitos:
- 1 H2 (sin markdown, solo la línea)
- 1 párrafo
- 5 bullets (máx. 8 palabras cada uno)
- Termina con CTA en 1 frase.
- Evita palabras: "revolucionario", "el mejor", "garantizado".
- Incluye keywords naturales: "auriculares inalámbricos", "cancelación de ruido", "Bluetooth 5.3".

Salida solo en el formato indicado.

- La respuesta obtenida
EchoBuds Pro X3: auriculares inalámbricos para tu día a día
Los EchoBuds Pro X3 combinan cancelación de ruido y comodidad para acompañarte en el trabajo remoto, el transporte o el gimnasio. Disfruta de llamadas más claras y música sin distracciones gracias a la cancelación de ruido activa, con conexión estable mediante Bluetooth 5.3. Su autonomía de hasta 30 horas con el estuche te da libertad para varios días, y la resistencia al agua IPX5 los hace ideales para entrenamientos y uso diario. Además, incluye 3 tamaños de almohadillas para un ajuste más seguro y confortable, adaptado a ti.

Cancelación de ruido para concentrarte

Hasta 30 horas con estuche

Resistencia al agua IPX5

Conexión estable Bluetooth 5.3

3 tamaños de almohadillas incluidas

Menos ruido, más concentración

Autonomía para varios días

Perfectos para commuting y gimnasio

Ajuste cómodo y seguro

- ¿Qué cambio tuvo mayor impacto?

Añadir estructura + formato (Iteración 2) da consistencia inmediata.

Audiencia + beneficios (Iteración 3) aumenta persuasión.

Restricciones + SEO + longitud exacta (Iteración 4) optimiza para producción.

### Entregable
Documento con:
1. Los 4 prompts (uno por iteración)
2. Las 4 respuestas obtenidas
3. Análisis de que cambió tuvo mayor impacto
4. Tu prompt final recomendado

---

## Ejercicio 4: Diseño de Prompts para Casos de Uso

### Metadata
- **Duración estimada**: 30 minutos
- **Tipo**: Diseño
- **Modalidad**: Grupal (3-4 personas)
- **Dificultad**: Intermedia
- **Prerequisitos**: Comprensión de componentes del prompt

### Contexto
En equipos, diseñaran prompts para casos de uso empresariales reales.

### Objetivo de Aprendizaje
- Aplicar los componentes del prompt a problemas reales
- Colaborar en el diseño y crítica de prompts

### Enunciado
Cada grupo recibira un caso de uso y deberá diseñar el prompt completo.

### Caso A: Generador de Emails de Seguimiento

**Contexto del problema:**
Un equipo de ventas necesita enviar emails de seguimiento personalizados después de demos de producto.

**Input disponible:**
- Nombre del prospecto
- Empresa
- Puntos discutidos en la demo
- Objeciones mencionadas
- Siguiente paso acordado

**Output deseado:**
Email profesional, personalizado, que refuerce los puntos fuertes y aborde las objeciones.

### Caso B: Resumidor de Reuniones

**Contexto del problema:**
Un asistente que convierte transcripciones de reuniones en resumenes estructurados.

**Input disponible:**
- Transcripción de la reunión (texto largo)
- Lista de participantes

**Output deseado:**
- Resumen ejecutivo (3-5 oraciones)
- Decisiones tomadas
- Action items con responsables
- Temas pendientes

### Caso C: Revisor de Código Automatizado

**Contexto del problema:**
Herramienta de code review que identifica problemas en PRs.

**Input disponible:**
- Código fuente (diff o archivo completo)
- Lenguaje de programación
- Estandares del equipo (opcional)

**Output deseado:**
- Lista de issues encontrados
- Severidad de cada issue
- Sugerencia de corrección
- Código corregido (opcional)

### Formato de Entrega

Para cada caso, entregar:

```markdown
## Caso [A]: [Nombre]

### Prompt Diseñado

Eres un comercial B2B senior que escribe emails de seguimiento claros y personalizados.

Contexto:
Hemos hecho una demo a un prospecto y queremos avanzar al siguiente paso.

Inputs:
- Nombre: {nombre}
- Empresa: {empresa}
- Puntos discutidos: {puntos}
- Objeciones: {objeciones}
- Siguiente paso acordado: {siguiente_paso}

Tarea:
Redacta un email de seguimiento profesional que:
1) Agradezca el tiempo
2) Recuerde 2-3 puntos clave de la demo conectados a beneficios
3) Aborde cada objeción con una respuesta breve y concreta
4) Reafirme el siguiente paso y proponga 2 opciones de horario

Formato:
- Asunto (máx. 8 palabras)
- Cuerpo: 120-170 palabras
- Cierre cordial + firma: {tu_nombre}

Restricciones:
- No uses jerga técnica.
- No prometas resultados garantizados.
- Estilo: humano, directo y amable.


### Justificación de Decisiones

Justificación

Rol: asegura tono comercial correcto.

Contexto/inputs: personaliza.

Formato: listo para copiar/pegar.

Restricciones: evita riesgos y “humo”.



### Limitaciones Identificadas

Limitaciones

Objeciones complejas pueden requerir más info (precio, competencia, seguridad).

Si no hay “siguiente paso”, el modelo podría inventar; conviene marcar “si está vacío, pide confirmación”.
```

```markdown
## Caso [B]: [Nombre]

### Prompt Diseñado

Eres un asistente ejecutivo que transforma transcripciones en resúmenes accionables.

Inputs:
- Participantes: {lista_participantes}
- Transcripción: {transcripcion}

Tarea:
Genera un resumen estructurado y fiel (no inventes datos). Si falta información, marca "No especificado".

Formato:
1) Resumen ejecutivo (3-5 oraciones)
2) Decisiones tomadas (bullets)
3) Action items (tabla: Acción | Responsable | Fecha límite | Estado)
4) Temas pendientes / riesgos (bullets)

Restricciones:
- Mantén nombres tal como aparecen.
- No incluyas opinión personal.
- Usa lenguaje claro y conciso.


### Limitaciones Identificadas
Limitaciones

Transcripciones con ruido o sin turnos pueden confundir responsables.

Si no hay fechas, conviene usar “Por definir” en vez de inventar.
```
```markdown
## Caso [C]: [Nombre]

### Prompt Diseñado

Eres un revisor de código senior (enfocado en calidad, seguridad y mantenibilidad).

Inputs:
- Lenguaje: {lenguaje}
- Estándares del equipo (opcional): {estandares}
- Código (diff o archivo): {codigo}

Tarea:
1) Identifica issues (bugs, edge cases, seguridad, rendimiento, legibilidad)
2) Asigna severidad: Baja / Media / Alta / Crítica
3) Explica el porqué en 1-2 frases por issue
4) Propón corrección. Si es posible, muestra un snippet corregido mínimo.

Formato:
- Lista numerada de issues
  - Severidad:
  - Evidencia (línea o fragmento):
  - Sugerencia:
- Sección final: "Top 3 prioridades"

Restricciones:
- No inventes dependencias o archivos no presentes.
- Si no hay contexto, evita suposiciones fuertes y dilo.



### Limitaciones Identificadas
Limitaciones

Sin tests o contexto del sistema puede fallar al sugerir cambios arquitectónicos.

En diffs grandes, conviene pedir “revisar por módulos”.
```

---

## Ejercicio 5: Identificación de Anti-patrones

### Metadata
- **Duración estimada**: 20 minutos
- **Tipo**: Análisis/Corrección
- **Modalidad**: Individual
- **Dificultad**: Básica
- **Prerequisitos**: Lectura de sección de anti-patrones

### Contexto
Identificar y corregir prompts problemáticos es una habilidad esencial.

### Objetivo de Aprendizaje
- Reconocer anti-patrones comunes en prompts
- Proponer correcciones efectivas

### Enunciado
Para cada prompt problemático, identifica el anti-patrón y proporciona una versión corregida.

### Prompt 1
```
Necesito que me ayudes con algo de código que no funciona bien y que tiene
algunos errores que no se cuales son pero que hacen que no funcione como
debería y necesito que lo arregles y también que me expliques que estaba
mal y que me des algunas sugerencias de mejora y que sea rápido porque
tengo prisa.
```

**Anti-patrón identificado:** Vago + sin input + demasiadas tareas
**Versión corregida:**
```
Actúa como desarrollador senior.

Tengo este código en {lenguaje} que falla con el error: "{error}".
Objetivo: corregir el bug sin cambiar el comportamiento esperado.

Código:
```{lenguaje}
{pega_aqui_el_codigo}
```

### Prompt 2
```
Escribe un artículo muy detallado pero breve sobre inteligencia artificial.
```

**Anti-patrón identificado:** Contradicción
**Versión corregida:**
```
Escribe un artículo introductorio sobre IA para estudiantes de bachillerato.

Longitud: 700-900 palabras.
Estructura: definición, usos reales (3), riesgos (3), cómo empezar a aprender (5 bullets).
Tono: claro y divulgativo, sin tecnicismos innecesarios.
```

### Prompt 3
```
Continúa con lo que estábamos haciendo antes.
```

**Anti-patrón identificado:** Falta de contexto
**Versión corregida:**
```
Quiero continuar con esta tarea: {describe_en_1_frase}.

Último estado:
- Objetivo: {objetivo}
- Lo último que hicimos: {resumen}
- Material relevante: {pega_texto_o_codigo}

Tarea ahora:
- {siguiente_paso_concreto}
Formato de salida: {lista/tabla/código}
```

### Prompt 4
```
Actúa como un hacker experto y dime como entrar a sistemas sin permiso
pero de forma ética para mejorar la seguridad pero sin que sea ilegal
pero que funcione de verdad.
```

**Anti-patrón identificado:** Petición ilícita
**Versión corregida:**
```
Actúa como consultor de ciberseguridad defensiva.

Necesito mejorar la seguridad de un sistema que administro legalmente.
Describe buenas prácticas y un plan de hardening:
- control de accesos
- gestión de parches
- configuración segura
- monitoreo y logging
- pruebas de seguridad autorizadas (alto nivel)

No incluyas instrucciones para entrar sin permiso ni técnicas de intrusión paso a paso.
```

### Prompt 5
```
Dame información.
```

**Anti-patrón identificado:** Demasiado genérico
**Versión corregida:**
```
Necesito información sobre {tema} para {objetivo}.

Incluye:
- Resumen (5 bullets)
- Conceptos clave (definiciones breves)
- 3 ejemplos prácticos
- Errores comunes
- Recomendaciones accionables

Nivel: {principiante/intermedio/avanzado}
Extensión: {corta/media/larga}
```

### Tabla Resumen

| # | Anti-patrón | Solución Aplicada |
|---|-------------|-------------------|
| 1 |Vago + sin input + demasiadas tareas |Pedir inputs, separar entregables, estructura |
| 2 |Contradicción |Definir longitud y audiencia |
| 3 |Falta de contexto |Incluir estado previo y objetivo |
| 4 |Petición ilícita |Reencuadre defensivo (hardening) |
| 5 |Demasiado genérico |Especificar tema, objetivo, nivel y formato |

---

## Ejercicio Extra: Prompt para tu Trabajo

### Metadata
- **Duración estimada**: 30 minutos
- **Tipo**: Aplicación Práctica
- **Modalidad**: Individual
- **Dificultad**: Avanzada

### Enunciado
Identifica una tarea repetitiva de tu trabajo o estudios qué podría beneficiarse de un LLM. Diseña un prompt completo siguiendo todo lo aprendido.

### Pasos
1. **Describe la tarea** (2-3 oraciones)
2. **Identifica inputs** (qué información tendrás disponible)
3. **Define outputs** (que necesitas obtener)
4. **Diseña el prompt** incluyendo todos los componentes relevantes
Actúa como profesor/a universitario/a y diseñador/a de exámenes.

Contexto:
Estoy estudiando {asignatura}. Tema: {tema}. Nivel: {nivel}.

Input:
{pega_aqui_los_apuntes}

Tarea:
1) Resume en 10-12 bullets (solo ideas del texto).
Crear resúmenes y preguntas tipo test de apuntes para estudiar (por ejemplo, temas de sociología o economía), manteniendo el contenido fiel y generando práctica de examen.

2) Define 8 conceptos clave (1-2 líneas cada uno).
Inputs

Texto (apuntes / PDF copiado)

Tema y nivel (uni/bach)

Formato de examen (test, desarrollo)

Número de preguntas y dificultad

3) Crea {n} preguntas tipo test (A/B/C/D) con dificultad {dificultad}.
Outputs

Resumen estructurado

Glosario

Test con soluciones justificadas

Lista de “trampas típicas” del tema

4) Da la respuesta correcta y una justificación breve por pregunta.

Formato:
- Secciones con títulos: Resumen / Conceptos / Test / Soluciones
Restricciones:
- No inventes información fuera del texto.
- Si algo no está en el texto, marca “No aparece”.

5. **Prueba y documenta** al menos 3 iteraciones
Tres iteraciones

Iteración 1: solo resumen → faltan preguntas.

Iteración 2: añadir test + justificación → mejora estudio activo.

Iteración 3: añadir “no inventes” + formato fijo → más fiable y reutilizable.

6. **Evalúa** la utilidad práctica del resultado
Muy útil porque automatiza estudio repetitivo y genera práctica. Limitación: si los apuntes están incompletos, el test tendrá menos variedad.


### Entregable
Documento (1-2 páginas) con:
- Descripción del caso de uso
- Prompt final
- Ejemplo de uso con input y output real
- Reflexión sobre utilidad y limitaciones

O bien, puedes entregar este .md completado con tus respuestas.
