function exportar(reporte, tipo){
  /** 
   * Exportar hará una promesa que generará el archivo solicitado.
  */

  // Se rescatan los parámetros del reporte elegido.
  // En la mayoría de los casos pueden ser:
  // • Todos, último año, último mes, última semana, excluidos.
  let param = document.getElementById(reporte).value;


  alert(`Exportando ${tipo} de ${reporte}.\nParametro: ${param}`);
}