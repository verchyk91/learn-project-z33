def normalize_path(path: str) -> str:
    # normalized_path = path
    #
    # if normalized_path[-1] != "/":
    #     normalized_path = f"{normalized_path}/"
    #
    # return normalized_path
    if path == "/":
        return path

    normalized_path = path.split("/")
    return normalized_path[1]