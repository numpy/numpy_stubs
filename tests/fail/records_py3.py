from datetime import datetime

import numpy.core.records as records

# Testing various incompatible args
records.fromarrays(dict(a=1))  # E: Argument 1 to "fromarrays" has incompatible type "Dict[str, int]"
records.fromarrays(datetime(1970, 1, 1))  # E: Argument 1 to "fromarrays" has incompatible type "datetime"

records.fromarrays([[1]], dtype=dict(a=1))  # E: Argument "dtype" to "fromarrays" has incompatible type
records.fromarrays([[1]], formats=dict(a=1))  # E: Argument "formats" to "fromarrays" has incompatible type
records.fromarrays([[1]], names=dict(a=1))  # E: Argument "names" to "fromarrays" has incompatible type
records.fromarrays([[1]], titles=dict(a=1))  # E: Argument "titles" to "fromarrays" has incompatible type
records.fromarrays([[1]], aligned=1)  # E: Argument "aligned" to "fromarrays" has incompatible type
records.fromarrays([[1]], byteorder=1)  # E: Argument "byteorder" to "fromarrays" has incompatible type
