async function exportar(reporte, tipo){
  /** 
   * Exportar generará el archivo solicitado.
  */

  // Se rescatan los parámetros del reporte elegido.
  // En la mayoría de los casos pueden ser:
  // • Todos, último año, último mes, última semana, excluidos.
  let param = document.getElementById(reporte).value;

  // Se indica la url de la API que genera los informes.
  let url = `${window.location.origin}/Mantenedor/generar_informe/`;
  let query = `${reporte}/${param}/${tipo}/`

  // Para debuggear, descomentar esto:
  // alert(`Exportando ${tipo} de ${reporte}.\nParametro: ${param}\nAPI: ${url+query}`);

  // Finalmente se le envía al usuario el archivo generado.
  //window.open(`http://127.0.0.1:8000/Mantenedor/generar_informe/${reporte}/${param}/${tipo}/`);
  window.open(`${url}${query}`)

  // Se podía haber usado una promesa, pero era más engorroso.
  /* fetch(url+query)
    .then(response => {
      return response.text();
    })
    .then(data => {
      window.open(data);
    })
    .catch(function (error) {
      console.log('Error con la petición', error);
    }); */
}