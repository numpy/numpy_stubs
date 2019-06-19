from typing import Optional, Sequence, Union

import numpy as np

def fromarrays(
    arrayList: Sequence[Union[Sequence, np.ndarray]],
    dtype: np._DtypeLike = ...,
    shape: np._ShapeLike = ...,
    formats: Union[str, Sequence[str]] = ...,
    names: Union[str, Sequence[str]] = ...,
    titles: Sequence[str] = ...,
    aligned: Optional[bool] = ...,
    byteorder: Optional[str] = ...,
) -> np.ndarray: ...
