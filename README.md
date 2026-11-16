# Diccionario Medicina · Carlota🥰

Diccionario de estudio en español, como web estática independiente. No necesita cuentas, backend, conexión a ChatGPT, claves de API ni dependencias externas. El contenido, la interfaz y el buscador están integrados en `dist/index.html`.

## Contenido

- 103 familias de raíces, prefijos y sufijos.
- 509 palabras únicas: 604 apariciones de ejemplos del diccionario fuente, reunidas sin perder pertenencias ni variantes de definición.
- 612 fichas con enlaces entre palabras y familias.
- Búsqueda por nombre, raíz o significado, sin exigir tildes.
- Índice por letras, filtro de tipo y paginación.
- Orden por frecuencia editorial orientativa en tres niveles; no es un recuento estadístico.
- Fichas guardadas en el navegador, enlaces directos y botón «Sorpréndeme» para descubrir palabras al azar.

## Uso

Publicar el contenido de `dist/` en cualquier alojamiento estático. También se puede abrir `dist/index.html` directamente en un navegador. No es necesario instalar paquetes.

Para reconstruir después de editar contenido o diseño:

```sh
python3 build.py
```

Los datos están en `data.json`; el diseño, en `styles.css`; y la estructura y comportamiento, en `template.html`. La fuente es el Diccionario médico de bolsillo A6, edición de noviembre de 2026. Las páginas originales se conservan en cada ficha.

## Publicación en GitHub Pages

Crear un repositorio público, subir `dist/index.html` y `dist/.nojekyll` a su raíz y seleccionar `main` y `/ (root)` en Settings → Pages. Alternativamente, publicar la carpeta `dist/` con un flujo de despliegue estático.

## Verificación realizada

Se han validado los 604 enlaces de ejemplos y sus relaciones inversas, los 612 identificadores de ficha y las 46 palabras con variantes de definición. Se ha probado la búsqueda, apertura y navegación entre fichas, filtro alfabético, orden por frecuencia, estado sin resultados y persistencia de guardadas. Se revisó la composición en escritorio y en un marco de 390 px.

La clasificación de frecuencia es orientativa. Las definiciones proceden del material original; esta conversión no constituye una nueva auditoría clínica integral.
