from typing import Optional, Sequence, Union, Tuple

import numpy as np

def fromarrays(
    arrayList: Sequence[Union[Sequence, np.ndarray]],
    dtype: Optional[np._DtypeLike] = ...,
    shape: Optional[np._ShapeLike] = ...,
    formats: Optional[Union[str, Sequence[str]]] = ...,
    names: Optional[Union[str, Sequence[str]]] = ...,
    titles: Optional[Sequence[str]] = ...,
    aligned: bool = ...,
    byteorder: Optional[str] = ...,
) -> np.ndarray: ...


def fromrecords(
    recList: Sequence[Tuple],
    dtype: Optional[np._DtypeLike] = ...,
    shape: Optional[np._ShapeLike] = ...,
    formats: Optional[Union[str, Sequence[str]]] = ...,
    names: Optional[Union[str, Sequence[str]]] = ...,
    titles: Optional[Sequence[str]] = ...,
    aligned: bool = ...,
    byteorder: Optional[str] = ...,
) -> np.ndarray: ...
