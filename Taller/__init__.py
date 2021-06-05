try: 
  import cx_Oracle
  cx_Oracle.init_oracle_client()
except cx_Oracle.DatabaseError:
  import cx_Oracle
  try: cx_Oracle.init_oracle_client(lib_dir= r"C:\app\JackStrick\product\18.0.0\dbhomeXE\bin")
  except cx_Oracle.DatabaseError: cx_Oracle.init_oracle_client(lib_dir= r"C:\app\%USERNAME%\product\18.0.0\dbhomeXE\bin")