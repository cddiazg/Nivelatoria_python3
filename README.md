# Sistema de Gestión Académica para Estudiantes

Este programa en Python es una herramienta sencilla y efectiva diseñada para la gestión de información académica de estudiantes en una institución educativa. Permite realizar operaciones fundamentales como registrar nuevos estudiantes, consultar sus datos, actualizar sus calificaciones, eliminar registros y visualizar un listado completo de todos los estudiantes con sus promedios.

## Características Principales

* **Registro de Estudiantes**: Permite añadir nuevos estudiantes al sistema, capturando su nombre completo, un número de identificación único, su edad y una lista de al menos tres notas académicas.
* **Consulta de Estudiantes**: Facilita la búsqueda de un estudiante específico mediante su número de identificación. Al encontrarlo, muestra todos sus datos relevantes, incluyendo su edad, el detalle de sus notas y el cálculo de su promedio.
* **Actualización de Notas**: Ofrece la funcionalidad para modificar las notas de un estudiante ya registrado en el sistema, permitiendo mantener la información académica al día.
* **Eliminación de Estudiantes**: Permite remover el registro completo de un estudiante del sistema, utilizando su número de identificación.
* **Listado General**: Proporciona una vista general de todos los estudiantes inscritos, presentando su nombre y el promedio general de sus notas de manera clara y organizada.
* **Validación de Entrada**: El programa incluye validaciones robustas para asegurar que los datos ingresados por el usuario sean correctos y consistentes.
* **Menú Interactivo**: La interfaz es un menú basado en texto que guía al usuario a través de las diferentes opciones de manera intuitiva.

## Requisitos del Sistema

* **Python 3.x**: El programa está desarrollado en Python 3 y requiere una instalación compatible (versión 3.6 o superior es recomendada) para su correcto funcionamiento.

## Cómo Ejecutar el Programa

1.  **Guarda el código**: Copia el código Python proporcionado y guárdalo en un archivo con extensión `.py`. Por ejemplo, puedes nombrarlo `gestion_academica.py`.
2.  **Abre una terminal o línea de comandos**: Navega hasta el directorio donde guardaste el archivo.
3.  **Ejecuta el programa**: En la terminal, escribe el siguiente comando y presiona Enter:

    ```bash
    python gestion_academica.py
    ```

## Manual de Usuario

Una vez que el programa se inicie, te recibirá con un menú de opciones. Simplemente ingresa el número correspondiente a la acción que deseas realizar y presiona Enter.

A continuación, se detalla el uso de cada opción:

### 1. Registrar estudiante

* **Acción**: Ingresa `1` y presiona Enter.
* **Proceso**:
    * El sistema te pedirá el **número de identificación** del estudiante. Este ID debe ser único; si ya existe, se te notificará.
    * Luego, solicita el **nombre completo** del estudiante (no puede estar vacío).
    * Después, ingresa la **edad** del estudiante (debe ser un número entero positivo).
    * Finalmente, se te preguntará **cuántas notas** deseas ingresar. Deben ser al menos 3. Por cada nota, ingresa un valor entre `0` y `5`.
* **Resultado**: Si todos los datos son válidos, el estudiante será añadido al sistema.

### 2. Consultar estudiante

* **Acción**: Ingresa `2` y presiona Enter.
* **Proceso**:
    * Se te pedirá el **número de identificación** del estudiante a consultar.
* **Resultado**:
    * Si el estudiante existe, se mostrará su nombre, identificación, edad, la lista detallada de sus notas y su promedio general.
    * Si el estudiante no se encuentra en el sistema, se mostrará un mensaje de error.

### 3. Actualizar notas

* **Acción**: Ingresa `3` y presiona Enter.
* **Proceso**:
    * Ingresa el **número de identificación** del estudiante cuyas notas deseas actualizar.
    * Si el estudiante es encontrado, verás sus notas actuales.
    * El sistema te guiará para ingresar las **nuevas notas**, una por una. Asegúrate de que estén entre `0` y `5`.
* **Resultado**: Las notas antiguas del estudiante serán reemplazadas por las nuevas ingresadas.

### 4. Eliminar estudiante

* **Acción**: Ingresa `4` y presiona Enter.
* **Proceso**:
    * Ingresa el **número de identificación** del estudiante que deseas eliminar.
* **Resultado**:
    * Si el estudiante existe, su registro será removido permanentemente del sistema y se te confirmará la eliminación.
    * Si el estudiante no se encuentra, se mostrará un mensaje de error.

### 5. Ver todos los estudiantes

* **Acción**: Ingresa `5` y presiona Enter.
* **Proceso**:
    * Esta opción no requiere entradas adicionales.
* **Resultado**:
    * El programa mostrará un listado claro de todos los estudiantes registrados, incluyendo su identificación, nombre y su promedio general de notas.
    * Si no hay estudiantes registrados, se indicará que la lista está vacía.

### 6. Salir

* **Acción**: Ingresa `6` y presiona Enter.
* **Resultado**: El programa finalizará su ejecución.

---
Espero que este programa y su manual de usuario te sean de gran ayuda para tu taller. ¿Te gustaría que se añadiera alguna otra funcionalidad o tienes alguna pregunta específica sobre el código?