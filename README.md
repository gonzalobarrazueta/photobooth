# photobooth

`photobooth` es un lenguaje específico de dominio que permite manipular y transformar imágenes y videos desde una terminal.

## 🏗️ Tabla de contenidos

<!-- TOC -->
* [photobooth](#photobooth)
  * [🏗️ Tabla de contenidos](#-tabla-de-contenidos)
  * [📝 Documentación](#-documentación)
    * [Consideraciones generales](#consideraciones-generales)
      * [Asignar variables](#asignar-variables)
      * [Uso de la opción `output`](#uso-de-la-opción-output)
    * [Manipulación de imágenes](#manipulación-de-imágenes)
    * [Manipulación de videos](#manipulación-de-videos)
  * [🕹️ Demo](#-demo)
  * [🔨 Herramientas utilizadas](#-herramientas-utilizadas)
  * [✍️ Autor](#-autor)
<!-- TOC -->

## 📝 Documentación

### Consideraciones generales

#### Asignar variables
    
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

La función `compress` reduce el peso del archivo en bytes.

#### Uso de la opción `output`
La opción `output` especifica el nombre del archivo donde se guardará la imagen modificada.
````
output="image_path.jpg"
````
- Puede ser utilizada agregándola al final de cualquier comando.
- La opción `output` es opcional, a menos que se especifique lo contrario.
- Si la opción `output` no es especificada, la imagen original será sobrescrita.

### Manipulación de imágenes

### Manipulación de videos

## 🕹️ Demo

## 🔨 Herramientas utilizadas

## ✍️ Autor

- [@gonzalobarrazueta](https://www.github.com/gonzalobarrazueta)