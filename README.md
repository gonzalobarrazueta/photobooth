# photobooth

`photobooth` es un lenguaje específico de dominio que permite manipular y transformar imágenes y videos desde una terminal.

## 🏗️ Tabla de contenidos

<!-- TOC -->
* [photobooth](#photobooth)
  * [🏗️ Tabla de contenidos](#-tabla-de-contenidos)
  * [Consideraciones generales](#consideraciones-generales)
    * [Asignar variables](#asignar-variables)
    * [Uso de la opción output](#uso-de-la-opción-output)
  * [📷 Manipulación de imágenes](#-manipulación-de-imágenes)
    * [Recortar imagen](#recortar-imagen)
    * [Establecer aspect-ratio](#establecer-aspect-ratio)
    * [Reducir el peso de la imagen](#reducir-el-peso-de-la-imagen)
    * [Transformar la imagen](#transformar-la-imagen)
    * [Aplicar filtros](#aplicar-filtros)
    * [Pintar fondo](#pintar-fondo)
    * [Difuminar fondo](#difuminar-fondo)
  * [📽️ Manipulación de videos](#-manipulación-de-videos)
    * [Recortar video](#recortar-video)
    * [Convertir a gif](#convertir-a-gif)
    * [Ajustar velocidad](#ajustar-velocidad)
    * [Extraer audio](#extraer-audio)
  * [🕹️ Demo](#-demo)
  * [🔨 Herramientas utilizadas](#-herramientas-utilizadas)
  * [✍️ Autor](#-autor)
<!-- TOC -->

## Consideraciones generales

### Asignar variables
```
set [variable_name]="string_value"
```
- El usuario puede utilizar cualquier palabra para nombrar su variable.
- Todas las variables que se crean solo pueden tomar valores de tipo `string`.

Ejemplos de uso
```
set image="path_to_name.jpg"
set out="modified_image.jpg"

compress image quality=70 output=out
```
Para mayor información sobre el comando `compress`, consulte la sección [Reducir el peso de la imagen](#reducir-el-peso-de-la-imagen).

### Uso de la opción output
La opción `output` especifica el nombre del archivo donde se guardará la imagen modificada.
````
output="image_path.jpg"
````
- Puede ser utilizada agregándola al final de cualquier comando.
- Es opcional, a menos que se especifique lo contrario.
- Si la opción no es especificada, la imagen original será sobrescrita.

## 📷 Manipulación de imágenes

### Recortar imagen
```
crop [image_path] w=100 h=250
```
- `image_path`: representa la ruta de la imagen a modificar.
- `w`: representa el ancho de la imagen resultante en píxeles.
- `h`: representa el alto de la imagen resultante en píxeles.

### Establecer aspect-ratio
Formatos disponibles para `aspect-ratio`: `1:1`, `9:16`, `16:9`, `3:4`, `4:3`
```
crop [image_path] smart aspect-ratio=1:1
```
- `image_path`: representa la ruta de la imagen a modificar.
- `aspect-ratio`: representa la relación de aspecto de la imagen resultante.
- `smart` _(opcional)_: identifica la región más relevante de la imagen y la recorta en base a la relación de aspecto especificada. Para lograr esta identificación, esta función hace uso de [Azure AI Services](https://learn.microsoft.com/en-us/rest/api/computervision/generate-thumbnail/generate-thumbnail?view=rest-computervision-v3.2&tabs=HTTP).

### Reducir el peso de la imagen
Reduce el peso del archivo en bytes.
```
compress [image_path] quality=85
```
- `quality`: representa la calidad de la imagen resultante. En este ejemplo, la calidad será comprimida al 85% de la calidad original.

### Transformar la imagen
Cambia la forma de una imagen a diferentes figuras geométricas.

Formas disponibles: `circular`, `elliptical`, `triangular`, `hexagonal`, `heart`, `star`, `rounded_rectangle`, `rhombus`, `custom`
```
transform [image_path] shape=circular
```

**Caso `shape=triangular`**

Si se selecciona la forma triangular, adicionalmente, se tendrá que especificar el tipo de tríangulo.

```
transform [image_path] shape=triangular type=[equilateral|isosceles|scalene]
```

**Caso `shape=custom`**

Si se selecciona la forma personalizada, adicionalmente, se tendrá que especificar la ruta de la imagen que se utilizará como máscara.

```
transform [image_path] shape=custom svg-path="mask.svg"
```

### Aplicar filtros

Aplica un filtro a la imagen.

Filtros disponibles: `mono`, `sepia`, `comic`, `painting`

```
apply filter=mono [image_path] 
```

### Pintar fondo

Pinta el fondo de la imagen con un color sólido.

Colores de fondo disponibles: `white`, `black`, `green`, `yellow`, `blue`

```
paint background [image_path] color=green
```

### Difuminar fondo

Detecta el objeto principal de la imagen y difumina el fondo.
```
blur background [image_path]
```

## 📽️ Manipulación de videos

### Recortar video

Recorta un video en base a un intervalo de tiempo.
```
trim video [video_path] from=1:15 to=3:15
```
- `video_path`: representa la ruta del video a modificar.
- `from`: representa el tiempo de inicio del intervalo en el formato `minutos:segundos`.
- `to`: representa el tiempo de fin del intervalo en el formato `minutos:segundos`.

### Convertir a gif

Convierte una sección del video a un gif.
```
convert video [video_path] from=1:15 to=3:15 format=gif
```

### Ajustar velocidad

Modifica la velocidad del video.

Las velocidades disponibles son: `0.25`, `0.5`, `1.25`, `1.5`, `2`.
```
adjust speed [video_path] rate=1.25
```
- `rate`: representa la velocidad del video resultante.

### Extraer audio

Obtiene el audio del video y lo guarda en un archivo `mp3`.

Por defecto, el archivo de audio se guardará con el nombre `audio.mp3`. Esto puede ser modificado utilizando la opción `output`.
```
extract audio [video_path]
```

## 🕹️ Demo

## 🔨 Herramientas utilizadas

## ✍️ Autor

- [@gonzalobarrazueta](https://www.github.com/gonzalobarrazueta)