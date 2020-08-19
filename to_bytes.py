def to_bytes(text: Union[str, bytes]) -> bytes:
    if isinstance(text, bytes):
        return text
    if not isinstance(text, str):
        raise ValueError(f"cannot conver {type(text)} to bytes")

    result = text.encode()
    return result