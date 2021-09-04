try:
    import h5py
except ImportError:
    no_h5py = True
else:
    no_h5py = False

try:
    import h5pyd
except ImportError:
    no_h5pyd = True
else:
    no_h5pyd = False


def File(path, mode='a', **kwargs):
    """Either h5py.File or h5pyd.File depending on path."""
    if isinstance(path, str):
        if path.startswith(('http://', 'https://', 'hdf5://')) or 'endpoint' in kwargs:
            if no_h5pyd:
                raise ImportError(
                    'h5pyd package is required for: {}'.format(path))
            return h5pyd.File(path, mode, **kwargs)

    if no_h5py:
        raise ImportError('h5py package is required for {}'.format(path))
    return h5py.File(path, mode, **kwargs)
