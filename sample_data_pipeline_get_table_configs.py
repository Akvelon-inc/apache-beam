def get_table_configs():
    """
    return a list of tables that should go from cloud sql to bigquery
    :return:
    """
    dim_tables = [
        {
            'table': 'Office',
            'key_field': 'Id',
            'schema': [
                {'name': 'Id', 'type': 'STRING', 'mode': 'NULLABLE'},
                {'name': 'Name', 'type': 'STRING', 'mode': 'NULLABLE'},
            ]
        },
    ]

    fact_tables = []
    export_tables = dim_tables + fact_tables
    tables = []

    sql_conn_id = Variable.get('SQL-CONNECTION-ID', default_var='default')
    gcp_conn_id = Variable.get('GCP-CONNECTION-ID', default_var='default')
    export_bucket = Variable.get('GCP-BUCKET-NAME', default_var='default')

    for table in export_tables:
        cfg = TableConfig(sql_conn_id=sql_conn_id,
                          export_table=table['table'],
                          export_bucket=export_bucket,
                          gcp_conn_id=gcp_conn_id,
                          table_schema=table['schema'],
                          key_field=table['key_field']
                          )
        tables.append(cfg)
    return tables
