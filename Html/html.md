## Que es html

Es el documento que lee el navegador está escrito en un **lenguaje de marcado** llamado HTML, que son las siglas de **HyperText Markup Language** (Lenguaje de marcas de hipertexto), o lo que es lo mismo, un lenguaje de etiquetas que permite incluir o hacer referencia a todo tipo de información.

### Estructura de etiqueta HTML

La estructura básica de una etiqueta HTML se compone de dos partes:

1.- **Etiqueta de apertura**:
  - Se escribe utilizando el nombre de la etiqueta entre los símbolos ```<``` y ```>```.
  - Se recomienda escribir las etiquetas en minúsculas, aunque los navegadores modernos no duelen tener problemas con las mayúsculas.
  - Algunas etiquetas, como ```<br>```, no requieren una etiqueta de cierre.

2.- **Etiqueta de cierre**:
  - Indica el final del elemento HTML.
  - Se escribe utilizando el nombre de la etiqueta seguido de una barra ```/``` y los simbolos ```>```.
  - No es necesario para todas las etiquetas como ```<br>```.

3.- **Atributos**:

Las etiquetas HTML también pueden incluir atributos, que proporcionan información adicional sobre el elemento. Los atributos se escriben dentro de la etiqueta de aprtura, separados por espacios y con el nombre del atributo seguido de un signo igual ```=``` y el valor del atributo entre comillas dobles ```" "``` o comillas simples ```'```.

## Estructura básica de una página HTML.

  - ```<!DOCTYPE html>```: Declara el tipo de documento HTML.
  - ```<html>```: Define el inicio del documento HTML.
  - ```<head>```: Contiene información meta sobre la página, como el título y las hojas de estilo.
  - ```<title>```: Especifica el título de la página.
  - ```<body>```: Contiene el contenido principal de la página, que es lo que se muestra al usuario.
  - ```</body>```: Marca el final del cuerpo de la página.
  - ```</html>```: Marca el final del documento HTML.


### Ejemplo
```html
<!DOCTYPE html>
<html>
  <head>
    <title> Mi página web </title>
  </head>
  <body>
    <h1>Título de la página </h1>
    <p>Este es un párrafo de texto.</p>
    <img src='imagen.jpg' alt='Descripción de la imagen'>
  </body>
  </html>
``` 

## Etiquetas de cabecera
Las etiquetas de la cabecera de un documento HTML, también conocidas como "metaetiquetas" o "etiquetas head", se encuentran dentro de la sección ```<head>``` del documento y proporcionan información meta sobre la página, la cual no se muestra directamente al usuario, pero es utilizada por los navegadores y motores de búsqueda para comprender mejor el contenido de la página.

  - ```<title>```: Define el título de la página, el cual se muestra en la barra de título del navegador y en los resultados de búsqueda. Es crucial para el **SEO** *(Search Engine Optimization)*.


    ```html
    <title> Mi Página web </title>
    ```

  - ```meta charset='utf-8'>```: Especifica la codificación de caracteres del documento, lo que garantiza que los caractereses de muestren correctamente en dieferentes navegadores y dispositivos.

    ```html
    <meta charset='utf-8'>
    ```
  - ```<meta name='description' content='Descripción de la página'>```: Proporciona una breve descripción del contenido de la página, la cual se utiliza en los snippets de los resultados de búsqueda.

    ```html
    <meta name='description' content='descripción de la página'>
    ```

  - ```<meta name='keywords' content='Palabras Clave, Frase clave'>```: Define palabras claves relevantes para el contenido de la página, las cuales son utilizadas por los motores de búsqueda para indexar la página.

    ```html
    <meta name='keywords' content='Palabras clave, frase clave'>
    ```

  - ```<link rel='stylesheet' href='estilo.css'>```: Carga una hoja de estilos CSS externa para definir el estilo de la página.

    ```html
    <link rel='stylesheet' href='estilo.css'>
    ```

  - ```<script src='script.js'></script>```: Carga un archivo JavaScript para agregar funcionalidad interactiva a la página.

    ```html
    <script src='script.js'></script>
    ```  

Las etiquetas de cabecera deben colocarse dentro de la sección ```<head>``` del documento HTML.

## Etiquetas HTML de agrupación

Las etiquetas de agrupación HTML, también conocidas como "etiquetas de bloque" o "etiquetas contenedoras", se utilizan para agrupar y organizar elementos HTML dentro de un documento. Estas etiquetas definen secciones semánticas en la estructura de la página, lo que facilite su compresión y mantenimiento, además de permitir aplicar estilos CSS de manera organizada.

  - ```<div>```: Define una división genérica de contenido. Es la etiqueta de agrupación más utilizada.
  - ```<header>```: Define el encabezado de la página, generalmente utilizado para contener el logotipo, el título y la barra de navegación.
  - ```<main>```: Define el contenido principal de la página, donde se presenta la información esencial.
  - ```<aside>```: Define contenido secundario que complementa al contenido principal, como barras laterales o información adicional.
  - ```<footer>```: Define el pie de página, generalmente utilizado para mostrar informacion de copyright, contacto o enlaces legales.

***Ejemplo***:

```html
        <div class='contenedor'>
          <header>
            <h1>Mi página web</h1>
          </header>
        <main>
          <p>Este es el contenido principal de la página</a>
        </main>
        <aside>
          <p>Información adicional</p>
        </aside>
          <footer>
            <p>&copy; 2024 Mi Página web</p>
          </footer>
        </div>
```

  - ```<hr>```: También conocida como "regla horizontal" o "separador horizontal", se utiliza para insertar una línea horizontal en un documento HTML. Esta linea se extiende a lo ancho del contenedor en el que se encuentra y se utiliza para separar secciones de contenido o para indicar un cambio de tema.
  - ```<ol>```: Tambien conocida como "lista ordenada", se utiliza para crear listas de elementos con una numeración o secuencia especifica. Esta etiqueta es útil para organizar y presentar información de manera estructurada y clara, especialmente cuando se trata de pasos, instrucciones o elementos que deben seguir un orden determinado.

  ```html
  <ol>
    <li>Elemento 1</li>
    <li>Elemento 2</li>
    <li>Elemento 3</li>
  </ol>
  ```

  - ```ul```: también conocida como "lista no ordenada" o "lista de viñetas", se utiliza para crear una lista de elementos que no tienen un orden especifico. Los elementos de la lista se presentan con viñetas, como guiones, puntos o imágenes, para facilitar su visualización y comprensión.

      ```html
      <ul>
        <li>Elemento 1</li>
        <li>Elemento 2</li>
        <li>Elemento 3</li>
      </ul>
      ```
  - ```li```: Se utiliza para definir cada uno de los elementos dentro de una lista no ordenada o una lista ordenada. estas listas se crean utilizando las etiquetas ```<ul>``` y ```<ol>``` respectivamente.

  - ```<pre>```: Se utiliza para mostrar un bloque de texto preformateado dentro de un documento HTML. Esto significa que el texto se conserva tal cual se escribe, incluyendo los espacion en blanco, las tabulaciones, los saltos de línea y otros caracteres especiales.

      ```html
      <pre>Texto preformateado</pre>
      ```

  - ```<blockquote>```: También conocida como "cita de bloque", se utiliza para mostrar un bloque de texto que es una cita de otra fuente, como un libro, un artículo, una persona, etc. esta etiqueta permite resaltar y diferenciar las citas extensas, mantieniendo la estructura y semántica del contenido.

```html
  <blockquoote>texto de la cita</blockquote>
```

  - ```<dl>```: Se utiliza para crear listas de términos y sus definiciones correspondientes. Esta etiqueta es útil para presentar información de manera clara y organizada, especialmente cuando se trata de vocabularios, glosarios o términos técnicos.

```html
  <dl>
    <dt>Termino 1</dt>
    <dd>Definición del termino 1</dd>
    <dt>Termino 2</dt>
    <dd>Definición del termino 2</dd>
    <dt>Termino 3</dt>
    <dd>Definición del termino 3</dd>
  </dl>
```
  - ```<dt>```: Se utiliza para definir el término o concepto que se va a explicar dentro de una lista de definiciones. Esta lista se crea utilizando la etiqueta ```<dl>```.

```html
<dt>Término a definir</dt>
```

  - ```<dd>```: Se utiliza para definir la descripción de un término dentro de una lista de definiciones. Esta lista se crea utilizando la etiqueta ```<dl>``` junto con la etiqueta ```<dt>``` para especificar el término que se está definido.

```html
<dd>Descripción del término</dd>
```

  - ```<figure>```: Se utiliza para agrupar y etiquetar contenido multimedia, como imágenes, videos, audios o fragmentos de código, y presentarlo de manera destacada dentro de una página web. Esta etiqueta permite separar el contenido multimedia del flujo principal del texto, mejorando la legibilidad y la accesibilidad del contenido.

```html
<figure>
  <img src='imagen.jpg' alt='descripción de la imagen'>
  <figcaption>Pie de foto de la imagen</figcaption>
</figure>
```

  - ```<figcaption>```: Se utiliza para proporcionar un título o pie de foto a un elemento de figura ```<figure>```. Por lo general, se coloca dentro del elemento ```<figure>``` y puede aparecer antes o después del contenido de la figura. El propósito de una ```<figcaption>``` es proporcionar contexto o explicación adicional para la figura, como una descripción de la imagen, la fuente de la información o una cita relevante.

```html
<figure>
  <img src='imagen.jpg' alt='Descripción de la imagen'>
  <figcaption>Pie de foto para la imagen</figcaption>
</figure>
```