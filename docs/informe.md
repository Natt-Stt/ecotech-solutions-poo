# Informe Técnico: Optimización de Sistema en EcoTech Solutions

**Asignatura:** Programación Orientada a Objetos 
**Estudiante:** Natalia Trejo Tallón 
**Docente:** Rubén Schnettler  
**Institución:** INACAP Valparaíso

____________________________________________

## Índice
1. Introducción
2. Sección 1: Análisis Conceptual
3. Sección 2: Diseño del Sistema (Modelo Estructural UML)
4. Sección 3: Uso de Herramientas de IA Generativa
5. Sección 4: Mejoras Aplicadas y Principios de Diseño
6. Conclusiones y Reflexión
7. Referencias Bibliográficas

____________________________________________

## Introducción
La empresa **EcoTech Solutions**, dedicada al desarrollo de tecnologías sostenibles, ha presentado problemas de administración debido a su crecimiento acelerado. Actualmente utiliza sistemas aislados y planillas de cálculo, provocando duplicidad de datos, errores en asignación de proyectos, falta de trazabilidad en horas y vulnerabilidades en la seguridad de datos personales.

El objetivo general de este proyecto es diseñar un modelo conceptual y estructural orientado a objetos y enfocado en **POO Seguro**, utilizando la notación UML como base arquitectónica para solucionar las deficiencias del sistema actual mediante un diseño robusto, mantenible y escalable.

____________________________________________

## 2. Sección 1: Análisis Conceptual

### 2.1 Identificación y Jerarquización de las 6 Entidades del Dominio

Para solucionar integralmente el caso de EcoTech Solutions, se han identificado y jerarquizado 6 entidades del sistema:

1. **`Empleado` (Entidad Principal):** Representa al talento humano.
   - *Atributos:* 
   `id: int`, 
   `nombre: str`, 
   `correo: str`, 
   `_salario: float` (privado), 
   `_rut: str` (privado),
   `direccion: str`, 
   `nro_telefono: int`,
   `fechaInicioContrato: int`.

   - *Responsabilidad:* Mantener los datos personales del trabajador de forma segura.


2. **`Departamento` (Entidad Organizacional):** Agrupa áreas de la empresa.
   - *Atributos:* 
   `id_depto: int`, 
   `nombre: str`, 
   `gerente: Empleado`.

   - *Responsabilidad:* Organizar estructuralmente a los empleados sin destruir sus registros si la área cierra.

3. **`Proyecto` (Entidad Operativa):** Proyectos sostenibles de la empresa.
   - *Atributos:* 
   `id_proyecto: int`, 
   `nombre: str`, 
   `descripción: str`, 
   `fecha_inicio: str`.

   - *Responsabilidad:* Controlar las iniciativas activas de la organización.

4. **`RegistroTiempo` (Entidad Transaccional):** Trazabilidad del trabajo.
   - *Atributos:* 
   `id_registro: int`, 
   `fecha: str`, 
   `horas: float`, 
   `descripcion: str`.

   - *Responsabilidad:* Garantizar la imputación exacta de horas trabajadas por empleado y por proyecto.

5. **`Usuario` (Entidad de Seguridad / POO Seguro):** Manejo de accesos e identidad.
   - *Atributos:* 
   `id_usuario: int`, 
   `username: str`, 
   `_password_hash: str`, 
   `rol: str`.

   - *Responsabilidad:* Autenticar usuarios, validar permisos e impedir accesos no autorizados.

6. **`Informe` (Entidad de Salida / Reportabilidad):** Generación de reportes.
   - *Atributos:* 
   `id_informe: int`, 
   `tipo_informe: str`, 
   `fecha_generacion: str`, 
   `formato: str`.

   - *Responsabilidad:* Sintetizar la información transaccional y exportarla a PDF o Excel.

### 2.2 Vinculación de Problemas con Fundamentos de POO

* **Encapsulamiento y POO Seguro:** El atributo `salario` en `Empleado` y `password_hash` en `Usuario` se declaran **privados** (`-` o `_`). Esto evita modificaciones indebidas desde afuera sin pasar por métodos de validación, cumpliendo las normativas de privacidad.
* **Abstracción:** Se descartan atributos irrelevantes del empleado (color de pelo, opinión política) y se conservan únicamente los elementos relevantes para la operación de EcoTech.
* **Composición vs Agregación:** Se diferencia técnicamente la relación entre un `Departamento` y un `Empleado` (Agregación: el empleado sobrevive si el departamento se borra) frente a la de un `Empleado` y sus `RegistroTiempo` (Composición: las horas no existen si el empleado se elimina).
