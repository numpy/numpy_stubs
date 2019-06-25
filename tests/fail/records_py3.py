from datetime import datetime

import numpy.core.records as records

# Testing various incompatible args for fromarrays
records.fromarrays(dict(a=1))  # E: Argument 1 to "fromarrays" has incompatible type "Dict[str, int]"
records.fromarrays(datetime(1970, 1, 1))  # E: Argument 1 to "fromarrays" has incompatible type "datetime"

records.fromarrays([[1]], dtype=dict(a=1))  # E: Argument "dtype" to "fromarrays" has incompatible type
records.fromarrays([[1]], formats=dict(a=1))  # E: Argument "formats" to "fromarrays" has incompatible type
records.fromarrays([[1]], names=dict(a=1))  # E: Argument "names" to "fromarrays" has incompatible type
records.fromarrays([[1]], titles=dict(a=1))  # E: Argument "titles" to "fromarrays" has incompatible type
records.fromarrays([[1]], aligned=1)  # E: Argument "aligned" to "fromarrays" has incompatible type
records.fromarrays([[1]], byteorder=1)  # E: Argument "byteorder" to "fromarrays" has incompatible type


# Testing various incompatible args for fromrecords
records.fromrecords(dict(a=1))  # E: Argument 1 to "fromrecords" has incompatible type "Dict[str, int]"
records.fromrecords(datetime(1970, 1, 1))  # E: Argument 1 to "fromrecords" has incompatible type "datetime"

records.fromrecords([(1,)], dtype=dict(a=1))  # E: Argument "dtype" to "fromrecords" has incompatible type
records.fromrecords([(1,)], formats=dict(a=1))  # E: Argument "formats" to "fromrecords" has incompatible type
records.fromrecords([(1,)], names=dict(a=1))  # E: Argument "names" to "fromrecords" has incompatible type
records.fromrecords([(1,)], titles=dict(a=1))  # E: Argument "titles" to "fromrecords" has incompatible type
records.fromrecords([(1,)], aligned=1)  # E: Argument "aligned" to "fromrecords" has incompatible type
records.fromrecords([(1,)], byteorder=1)  # E: Argument "byteorder" to "fromrecords" has incompatible type
