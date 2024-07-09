# photobooth

`photobooth` es un lenguaje específico de dominio que permite manipular y transformar imágenes y videos desde una terminal.

## 🏗️ Tabla de contenidos

<!-- TOC -->
* [photobooth](#photobooth)
  * [🏗️ Tabla de contenidos](#-tabla-de-contenidos)
  * [Consideraciones generales](#consideraciones-generales)
    * [Asignar variables](#asignar-variables)
    * [Uso de la opción `output`](#uso-de-la-opción-output)
  * [📷 Manipulación de imágenes](#-manipulación-de-imágenes)
    * [Cortar imagen](#cortar-imagen)
    * [Establecer aspect-ratio](#establecer-aspect-ratio)
  * [📽️ Manipulación de videos](#-manipulación-de-videos)
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

### Uso de la opción `output`
La opción `output` especifica el nombre del archivo donde se guardará la imagen modificada.
````
output="image_path.jpg"
````
- Puede ser utilizada agregándola al final de cualquier comando.
- La opción `output` es opcional, a menos que se especifique lo contrario.
- Si la opción `output` no es especificada, la imagen original será sobrescrita.

## 📷 Manipulación de imágenes

### Cortar imagen
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

## 📽️ Manipulación de videos

## 🕹️ Demo

## 🔨 Herramientas utilizadas

## ✍️ Autor

- [@gonzalobarrazueta](https://www.github.com/gonzalobarrazueta)