from utils import normalize_path


def test_normalize_path():
    test_data = ['/', 'hello', 'hello/', '/xxx/']
    expected = ['/', 'hello/', 'hello/', '/xxx/']

    for i in range(4):
        t = test_data[i]
        e = expected[i]
        g = normalize_path(t)

        assert g == e, f"path '{t}' normalized to '{g}', while '{e}' expected"
