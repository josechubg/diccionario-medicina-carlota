# Diccionario Medicina · Carlota🥰

Web pública: https://josechubg.github.io/diccionario-medicina-carlota/

Diccionario de estudio en español, como web estática independiente. No necesita cuentas, backend, conexión a ChatGPT, claves de API ni dependencias externas. El contenido, la interfaz y el buscador están integrados en `dist/index.html`.

## Contenido

- 103 familias de raíces, prefijos y sufijos.
- 509 palabras únicas: 604 apariciones de ejemplos del diccionario fuente, reunidas sin perder pertenencias ni variantes de definición.
- Dos apartados: el diccionario principal contiene exclusivamente las 103 familias; «Buscar una palabra» consulta los 509 términos completos.
- Cada raíz o afijo muestra su significado y todos sus ejemplos explicados. Cada palabra enlaza con sus familias relacionadas.
- Búsqueda por raíz o significado en el primer apartado y por palabra o definición en el segundo, sin exigir tildes. Intro abre una coincidencia exacta o el único resultado.
- Índice por letras, paginación y orden por frecuencia para las raíces y afijos. La frecuencia es editorial y orientativa, en tres niveles; no es un recuento estadístico.
- Fichas guardadas en el navegador y filtradas por apartado, enlaces directos compatibles con los anteriores y botón «Sorpréndeme» para descubrir una ficha del apartado actual.

## Uso

Publicar el contenido de `dist/` en cualquier alojamiento estático. También se puede abrir `dist/index.html` directamente en un navegador. No es necesario instalar paquetes.

Para reconstruir después de editar contenido o diseño:

```sh
python3 build.py
```

Los datos están en `data.json`; el diseño, en `styles.css`; y la estructura y comportamiento, en `template.html`. El constructor actualiza tanto `dist/index.html` para la previsualización como `index.html` en la raíz para la publicación. La fuente es el Diccionario médico de bolsillo A6, edición de noviembre de 2026. Las páginas originales se conservan en cada ficha.

La interfaz usa un estilo de cuaderno ilustrado, un cerebro decorativo animado, tarjetas por colores y texto ampliado. El botón de pausa detiene las animaciones y recuerda la preferencia en este navegador. Se respeta también la preferencia de movimiento reducido del dispositivo. La ilustración es decorativa y no pretende representar la anatomía real.

## Publicación en GitHub Pages

El repositorio público `josechubg/diccionario-medicina-carlota` publica automáticamente desde `main` y `/ (root)` en GitHub Pages. Después de ejecutar `python3 build.py`, incluir `index.html` y los archivos fuente modificados en el commit. Para otros alojamientos estáticos se puede publicar el contenido de `dist/`, excluyendo los archivos temporales de revisión `qa-*.html`.

## Verificación realizada

Se han validado los 604 enlaces de ejemplos y sus relaciones inversas, los 612 identificadores de ficha y las 46 palabras con variantes de definición. Se ha probado la separación de los dos apartados, la búsqueda de «-filo» y sus seis ejemplos, la consulta de «anemia» con Intro y sus enlaces a «a- / an-» y «-emia», la recarga de enlaces directos, la búsqueda «acidofilos» y el paso del diccionario al buscador de palabras. El índice y la frecuencia muestran exclusivamente raíces y afijos. Se revisó la composición en escritorio y en un marco de 390 px.

La clasificación de frecuencia es orientativa. Las definiciones proceden del material original; esta conversión no constituye una nueva auditoría clínica integral.
