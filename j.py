from jina import Flow

import os

os.environ['JINA_HUB_NO_IMAGE_REBUILD'] = '1'

f: Flow = (
    Flow()
    #.config_gateway(port=12345, protocol='http') \
    .add(uses='jinahub+docker://TransformerTorchEncoder') \
    .add(
        uses='jinahub+docker://SimpleIndexer',
        uses_metas={'workspace': './mydb'},
        uses_with = {'table_name': 'my_custon_table_name'}
    )
)

f.to_kubernetes_yaml('./kbe')