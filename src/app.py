import streamlit as st
from basedatos import (
    crear_empleado, listar_empleados,
    crear_departamento, listar_departamentos,
    crear_proyecto, listar_proyectos,
    crear_registro_tiempo, listar_registros_tiempo,
)

st.set_page_config(page_title="EcoTech Solutions", layout="wide")
st.title("EcoTech Solutions - Sistema de Gestión Interna")

# Menú lateral para elegir sección
seccion = st.sidebar.radio("Ir a:", ["Empleados", "Departamentos", "Proyectos", "Registro de Tiempo"])

if seccion == "Empleados":
    st.header("Gestión de Empleados")

    with st.form("form_empleado", clear_on_submit=True):
        nombre = st.text_input("Nombre")
        direccion = st.text_input("Dirección")
        telefono = st.text_input("Teléfono")
        mail = st.text_input("Correo")
        fecha_inicio = st.date_input("Fecha de inicio")
        salario = st.number_input("Salario", min_value=0.0, step=1000.0)

        enviado = st.form_submit_button("Guardar empleado")

        if enviado:
            if nombre and direccion and telefono and mail:
                nuevo_id = crear_empleado(
                    nombre, direccion, telefono, mail, str(fecha_inicio), salario
                )
                if nuevo_id:
                    st.success(f"Empleado creado con ID {nuevo_id}")
                else:
                    st.error("No se pudo crear el empleado. Revisa la terminal para más detalle.")
            else:
                st.warning("Completa todos los campos obligatorios.")

    st.subheader("Empleados registrados")
    empleados = listar_empleados()
    if empleados:
        st.dataframe(empleados)
    else:
        st.info("Aún no hay empleados registrados.")

elif seccion == "Departamentos":
    st.header("Gestión de Departamentos")

    with st.form("form_departamento", clear_on_submit=True):
        nombre = st.text_input("Nombre del departamento")
        descripcion = st.text_area("Descripción")
        gerente = st.text_input("Gerente")

        enviado = st.form_submit_button("Guardar departamento")

        if enviado:
            if nombre and descripcion:
                nuevo_id = crear_departamento(nombre, descripcion, gerente)
                if nuevo_id:
                    st.success(f"Departamento creado con ID {nuevo_id}")
                else:
                    st.error("No se pudo crear el departamento (¿el nombre ya existe?).")
            else:
                st.warning("Completa nombre y descripción.")

    st.subheader("Departamentos registrados")
    departamentos = listar_departamentos()
    if departamentos:
        st.dataframe(departamentos)
    else:
        st.info("Aún no hay departamentos registrados.")

elif seccion == "Proyectos":
    st.header("Gestión de Proyectos")

    with st.form("form_proyecto", clear_on_submit=True):
        nombre = st.text_input("Nombre del proyecto")
        descripcion = st.text_area("Descripción")
        fecha_inicio = st.date_input("Fecha de inicio")

        enviado = st.form_submit_button("Guardar proyecto")

        if enviado:
            if nombre and descripcion:
                nuevo_id = crear_proyecto(nombre, descripcion, str(fecha_inicio))
                if nuevo_id:
                    st.success(f"Proyecto creado con ID {nuevo_id}")
                else:
                    st.error("No se pudo crear el proyecto (¿el nombre ya existe?).")
            else:
                st.warning("Completa nombre y descripción.")

    st.subheader("Proyectos registrados")
    proyectos = listar_proyectos()
    if proyectos:
        st.dataframe(proyectos)
    else:
        st.info("Aún no hay proyectos registrados.")

elif seccion == "Registro de Tiempo":
    st.header("Registro de Horas Trabajadas")

    empleados = listar_empleados()
    proyectos = listar_proyectos()

    if not empleados or not proyectos:
        st.warning("Necesitas al menos un empleado y un proyecto creados antes de registrar horas.")
    else:
        # Diccionarios para mostrar el nombre pero guardar el id
        opciones_empleado = {e["nombre"]: e["id"] for e in empleados}
        opciones_proyecto = {p["nombre"]: p["id"] for p in proyectos}

        with st.form("form_registro_tiempo", clear_on_submit=True):
            nombre_empleado = st.selectbox("Empleado", opciones_empleado.keys())
            nombre_proyecto = st.selectbox("Proyecto", opciones_proyecto.keys())
            fecha = st.date_input("Fecha")
            horas = st.number_input("Horas trabajadas", min_value=0.5, step=0.5)

            enviado = st.form_submit_button("Guardar registro")

            if enviado:
                id_empleado = opciones_empleado[nombre_empleado]
                id_proyecto = opciones_proyecto[nombre_proyecto]
                nuevo_id = crear_registro_tiempo(str(fecha), horas, id_empleado, id_proyecto)
                if nuevo_id:
                    st.success(f"Registro de tiempo guardado con ID {nuevo_id}")
                else:
                    st.error("No se pudo guardar el registro.")

    st.subheader("Registros existentes")
    registros = listar_registros_tiempo()
    if registros:
        st.dataframe(registros)
    else:
        st.info("Aún no hay registros de tiempo.")