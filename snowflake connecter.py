import snowflake.connector as snow
#conn = snow.connect() // you need to pass required account info and credentials here


conn = snowflake.connector.connect(
    user='pthakar',
    password='Newlearning@123',
    account='BV83940',
    warehouse='COMPUTE_WH'
    )

connection.cursor().execute("put file://my_third_file.txt @demo_db.public.my_internal_named_stage")
