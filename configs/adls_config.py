def adls_config(spark,dbutils):
  access_key = dbutils.secrets.get(scope="azure", key="adls-key")
  account_storage = dbutils.secrets.get(scope="azure", key="adls-account-name")

  spark.conf.set(
    f"fs.azure.account.key.{account_storage}.dfs.core.windows.net",
    access_key
  )