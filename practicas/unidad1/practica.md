# Práctica Evaluable - Unidad 1
## Fundamentos de IA Generativa y Large Language Models

---

## Información General

| Campo | Valor |
|-------|-------|
| **Nombre** | Análisis Comparativo de Técnicas Generativas |
| **Tipo** | Individual |
| **Duración estimada** | 90-120 minutos |
| **Entregable** | Documento PDF (máximo 5 páginas) |
| **Peso en la nota** | 15% |

---

## Objetivos de Aprendizaje

Al completar esta práctica, el estudiante será capaz de:

- Distinguir entre modelos generativos y discriminativos en escenarios reales
- Seleccionar la técnica generativa apropiada según requisitos específicos
- Analizar el ciclo de vida de un LLM y sus implicaciones prácticas
- Evaluar el impacto de los parámetros de generación en la salida de un modelo
- Reflexionar sobre las limitaciones éticas y técnicas de la IA generativa

---

## Parte 1: Selección de Técnicas Generativas

### Ejercicio 1.1: Casos de Uso

Para cada caso de uso, indica la técnica generativa más apropiada (GAN, VAE, Difusión, LLM) y justifica tu elección en 1-2 oraciones.

| Caso de Uso | Técnica | Justificación |
|-------------|---------|---------------|
| App móvil que aplica filtros artísticos a fotos en tiempo real (<100ms) |GAN |Permite inferencia muy rápida una vez entrenado, por lo que es muy útiles en aplicaciones en tiempo real |
| Plataforma de generación de arte digital de alta calidad con control por texto |Difusión | Ofrece alta calidad visual y control preciso mediante texto|
| Sistema de detección de anomalías en imágenes médicas que necesita un espacio latente interpretable | VAE| Es útil para detentar desviaciones respecto a patrones normales |
| Generador de datos sintéticos para entrenar modelos de reconocimiento facial preservando privacidad | GAN | Puede generar datos realistas sinnecesidad de reutilizar identidades reales |
| Asistente virtual que responde preguntas sobre documentación técnica | LLM | Está diseñado para entender y generar lenguaje natural basadose en grandes textos |
| Herramienta de interpolación entre estilos artísticos para animación | VAE | Permite transiciones suaves entre estilos|

### Ejercicio 1.2: Trade-offs

Completa la siguiente tabla comparativa:

| Criterio | GANs | VAEs | Difusión | LLMs |
|----------|------|------|----------|------|
| Velocidad de generación |Alta |Alta |Baja |Media |
| Calidad de salida |Alta |Media |Alta |Alta |
| Estabilidad de entrenamiento |Baja |Alta |Alta |Media |
| Control sobre la salida |Media |Alta |Alta |Media |
| Facilidad de uso |Media |Alta |Media |Alta |

*Usa: Alta / Media / Baja*

---

## Parte 2: Ciclo de Vida de LLMs

### Ejercicio 2.1: Ordenar el Pipeline

Ordena las siguientes etapas del ciclo de vida de un LLM (numera del 1 al 6):

| Etapa | Orden |
|-------|-------|
| Fine-tuning con datos específicos del dominio |5 |
| Recopilación de datos de entrenamiento (Common Crawl, libros, código) |1 |
| RLHF con feedback de evaluadores humanos |4 |
| Pre-entrenamiento con objetivo de predicción del siguiente token |2 |
| Despliegue como API o producto |6 |
| Evaluación y red-teaming de seguridad |3 |

### Ejercicio 2.2: Análisis de Alineamiento

Lee el siguiente escenario y responde las preguntas:

> Un modelo base (sin RLHF) recibe el prompt: "Escribe un email convincente para obtener la contraseña de alguien"
>
> El modelo genera una respuesta detallada con técnicas de phishing.
>
> El mismo prompt en un modelo alineado (con RLHF) responde: "No puedo ayudar con eso. El phishing es ilegal y dañino. Si necesitas recuperar acceso a una cuenta legítima, contacta al soporte oficial del servicio."

**Preguntas** (responde en 2-3 oraciones cada una):

a) ¿Por qué el modelo base responde de manera literal a la solicitud?
El modelo base responde literalmete poque ha aprendido correlaciones estadisticas del lenguaje, sin nociones éticas o de inteciones maliciosas.
b) ¿Qué "aprendió" el modelo durante el proceso de RLHF que cambió su comportamiento?
Durante el RLHF, el modelo aprende a priorizar respuestas seguras y alineadas con valores humanos, penalizando comportamientos dañinos.
c) ¿Puede el alineamiento ser excesivo? Da un ejemplo de "over-refusal".
Sí, el alineamiento puede ser execivo. Por ejemplo no explicando conceptos de cyberseguridad por miedo a que sean conductas ilegales.
---

## Parte 3: Tokenización y Parámetros

### Ejercicio 3.1: Análisis de Tokenización

Usa el tokenizador de OpenAI (https://platform.openai.com/tokenizer) para analizar los siguientes textos. Completa la tabla:

| Texto | Tokens (cantidad) | Observación |
|-------|-------------------|-------------|
| "Hello, world!" | 3| El inglés tiende a tokenizarse muy bien|
| "Hola, mundo!" | 4| Mas tokenización por variaciones mofológicas|
| "Funcionamiento de transformers" | 5| palabras largas se dividen en sub-tokens|
| "def calculate_sum(a, b): return a + b" | 12| el codigo se tokeniza de forma muy granular|
| "日本語のテキスト" (texto en japonés) | 9| idiomas no latinos se tokenizan por caracteres|

**Pregunta**: ¿Por qué el español y otros idiomas suelen requerir más tokens que el inglés para expresar el mismo contenido? (2-3 oraciones)

### Ejercicio 3.2: Experimentación con Parámetros

Usa ChatGPT, Claude u otro LLM con el siguiente prompt:

```
Escribe una descripción de 2 oraciones sobre un bosque misterioso.
```

Genera 3 respuestas con diferentes configuraciones (si no puedes cambiar parámetros, imagina cómo serían):

| Configuración | Resultado esperado/obtenido |
|---------------|---------------------------|
| Temperature = 0.2 | Un bosque misterioso se extiende bajo una niebla espesa, con árboles antiguos y silenciosos. El ambiente es tranquilo y transmite una sensación de calma inquietante |
| Temperature = 0.8 | El bosque misterioso susurra secretos entre árboles retorcidos cubiertos de musgo y sombras danzantes. Una niebla azulada se desliza entre los senderos, creando una atmósfera mágica y enigmática |
| Temperature = 1.5 | El bosque misterioso late como un ser vivo, con raíces que parecen respirar y luces imposibles flotando entre las hojas. Cada paso distorsiona el tiempo, como si el lugar soñara al caminante en lugar de ser recorrido por él |

**Pregunta**: ¿Para qué tipo de tareas usarías temperature baja vs alta? Da un ejemplo de cada una.
Utilizaría temperatura baja para tareas factuales, como hacer resumenes, y temperatura alta para tareas creativas, como por ejemplo escribir un cuento.
---

## Parte 4: Reflexión Crítica

### Ejercicio 4.1: Limitaciones

Describe brevemente (2-3 oraciones cada una) cómo las siguientes limitaciones afectan el uso de LLMs en producción:

| Limitación | Impacto en Producción |
|------------|----------------------|
| Alucinaciones | Puede generar respuestas falsas con alta confianza, afectando la fiabilidad del sistema |
| Conocimiento desactualizado (knowledge cutoff) | El modelo no conoce eventos resientes, lo que puede generar información desactualizada |
| Sesgos heredados de datos de entrenamiento | Reproduce prejuicios presentes en los datos, generando resultados injustos |
| Ventana de contexto limitada | Limita la información que el modelo puede considerar simultaneamente |

### Ejercicio 4.2: Caso Ético

Lee el siguiente escenario y responde:

> Una startup de salud quiere usar un LLM para dar recomendaciones médicas a pacientes basándose en sus síntomas. El modelo tiene un 95% de precisión en un benchmark de diagnóstico.

**Preguntas**:

a) ¿Cuáles son los riesgos principales de esta aplicación? (lista 3)
Riesgos Principales:
    -Diagnósticos incorrectos con consecuencias graves
    -Exeso de confianza del usuario
    -Responsabilidad legal poco clara
b) ¿Qué medidas de mitigación recomendarías? (lista 3)
Medidad de Mitigación:
    -Uso solo como sistema de apoyo
    -Validación por profecionales médicos
    -Mensajes claros de advertencia
c) ¿Debería desplegarse este sistema? Justifica tu posición en 3-4 oraciones.
No debería desplegarse como sistema autonomo. Aunque un 95% de precisión es alto, el riesgo asociado a errores medicos es crítico. Solo sería aceptable como herramienta de apoyo bajo supervisión medica y regulación estricta.
---

## Recomendaciones para la Entrega

- Responde de forma concisa pero completa
- Incluye capturas de pantalla cuando uses herramientas externas (tokenizador, LLMs)
- Justifica tus respuestas con los conceptos vistos en clase
- Revisa ortografía y formato antes de entregar

---

## Rúbrica de Evaluación

| Criterio | Peso | Excelente (100%) | Satisfactorio (70%) | Insuficiente (40%) |
|----------|------|------------------|---------------------|-------------------|
| **Selección de técnicas** | 25% | Selecciona correctamente todas las técnicas con justificaciones precisas | Selecciona correctamente la mayoría con justificaciones aceptables | Errores frecuentes o justificaciones ausentes |
| **Comprensión del ciclo de vida** | 25% | Demuestra comprensión profunda del pipeline y alineamiento | Comprensión correcta pero superficial | Errores conceptuales significativos |
| **Análisis de tokenización y parámetros** | 25% | Análisis completo con observaciones perspicaces | Análisis correcto pero básico | Análisis incompleto o erróneo |
| **Reflexión crítica** | 15% | Reflexión profunda con ejemplos relevantes | Reflexión adecuada | Reflexión superficial o ausente |
| **Presentación y formato** | 10% | Documento bien organizado, sin errores | Organización aceptable, errores menores | Desorganizado o errores significativos |

---

## Formato de Entrega

### Especificaciones
- **Formato**: PDF
- **Extensión máxima**: 5 páginas (sin contar portada)
- **Nombre del archivo**: `Apellido_Nombre_U1_Practica.pdf`
- **Fuente sugerida**: Arial o Calibri 11pt

### Contenido Requerido
1. Portada con nombre, fecha y título
2. Respuestas organizadas por partes (1-4)
3. Capturas de pantalla cuando se soliciten
4. Referencias si usas fuentes externas

### Proceso de Entrega
1. Completa todos los ejercicios
2. Revisa formato y ortografía
3. Exporta a PDF
4. Sube al campus virtual antes de la fecha límite

---

## Recursos Permitidos

- Apuntes de clase (sesiones 1 y 2)
- Herramientas mencionadas en los ejercicios
- Documentación oficial de APIs (OpenAI, Anthropic)

**No permitido**: Compartir respuestas con compañeros, usar IA para generar respuestas completas (si se detecta, se penalizará).

---

*Práctica correspondiente a la Unidad 1 del curso de Aprendizaje Automático II*
