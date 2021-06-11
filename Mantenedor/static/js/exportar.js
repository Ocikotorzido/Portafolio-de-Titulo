async function exportar(reporte, tipo){
  /** 
   * Exportar hará una 'promesa' que generará el archivo solicitado.
  */

  // Se rescatan los parámetros del reporte elegido.
  // En la mayoría de los casos pueden ser:
  // • Todos, último año, último mes, última semana, excluidos.
  let param = document.getElementById(reporte).value;

  // Se indica la url de la API que genera los informes.
  let url = `${window.location.origin}/Mantenedor/api/v1/`;
  let query = `${reporte}/${param}/${tipo}/`
  alert(`Exportando ${tipo} de ${reporte}.\nParametro: ${param}\nAPI: ${url+query}`);

  fetch(url+query)
    .then(response => {
      return response.text();
    })
    .then(data => {
      window.open(data);
    })
    .catch(function (error) {
      console.log('Error con la petición', error);
    });
}