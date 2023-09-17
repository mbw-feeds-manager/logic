import os
import json

with open("config.json", "w") as f:
  f.write(
    json.dumps(
      dict(
        is_local_data=True,
        data_base_dir=f"{ os.environ.get('BASE_DIR') }",
        data_store_dir=f"{ os.environ.get('STORE_DIR') }",
        data_staging_dir=f"{ os.environ.get('STAGING_DIR')}",
      ), 
      indent=2
    )
  )